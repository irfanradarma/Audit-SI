import streamlit as st
import pandas as pd
import zipfile
import tempfile
from pathlib import Path
import os

st.set_page_config(page_title="UTS PG", layout="wide")
st.title("📦 ZIP → Excel → DataFrame")

uploaded_zip = st.file_uploader("Upload ZIP file yang di-email yah", type=["zip"])

A = 'A'
B = 'B'
C = 'C'
D = 'D'

answer_key = [A,B,B,D,C,D,B,A,C,D,
              A,B,C,D,C,B,B,A,C,A,
              D,D,C,B,A,A,A,C,B,D,
              C,C,A,D,B,B,D,B,C,D,
              D,D,B,A,B,C,D,C,A,D]

if uploaded_zip is not None:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # Save uploaded zip
        zip_path = tmp_path / uploaded_zip.name
        with open(zip_path, "wb") as f:
            f.write(uploaded_zip.read())

        # Extract main zip
        try:
            with zipfile.ZipFile(zip_path, "r") as z:
                z.extractall(tmp_path)
        except zipfile.BadZipFile:
            st.error("Uploaded file is not a valid ZIP.")
            st.stop()

        # Detect if there is a single folder wrapper
        extracted_items = [p for p in tmp_path.iterdir() if p.name != uploaded_zip.name]

        if len(extracted_items) == 1 and extracted_items[0].is_dir():
            working_dir = extracted_items[0]
        else:
            working_dir = tmp_path

        # Find all zip files inside
        zip_files = list(working_dir.rglob("*.zip"))

        if not zip_files:
            st.warning("No ZIP files found inside the uploaded file.")
            st.stop()

        # Prepare compiled structure
        compiled_data = {
            "names": [],
            "npm": [],
            "skor" : []
        }
        for i in range(1, 51):
            compiled_data[f"Q{i}"] = []

        # Process each inner zip
        for zp in zip_files:
            try:
                with zipfile.ZipFile(zp, "r") as z:
                    excel_files = [
                        f for f in z.namelist()
                        if f.endswith((".xlsx", ".xls"))
                    ]

                    for excel_file in excel_files:
                        # --- Read ID sheet ---
                        with z.open(excel_file) as ef:
                            df_ID = pd.read_excel(
                                ef,
                                sheet_name="ID",
                                engine="openpyxl"
                            )
                            name = df_ID.iloc[3, 3]
                            npm = df_ID.iloc[5, 3]

                        # --- Read PG sheet ---
                        with z.open(excel_file) as ef:
                            df_PG = pd.read_excel(
                                ef,
                                sheet_name="PG",
                                engine="openpyxl"
                            )

                            jawaban = df_PG.iloc[:, [0, 5]]
                            jawaban.columns = ["No", "Jawaban"]
                            jawaban = jawaban[jawaban["No"].notna()]

                        compiled_data["names"].append(name)
                        compiled_data["npm"].append(npm)

                        skor = 0
                        for _, row in jawaban.iterrows():
                            no = int(row["No"])
                            ans = row["Jawaban"]
                            compiled_data[f"Q{no}"].append(ans)
                            if ans == answer_key[no - 1]:
                                skor += 1

                        compiled_data["skor"].append(skor)

            except zipfile.BadZipFile:
                st.warning(f"Skipped invalid ZIP: {zp.name}")

        # Normalize column lengths
        max_len = len(compiled_data["names"])
        for k, v in compiled_data.items():
            if len(v) < max_len:
                v.extend([None] * (max_len - len(v)))

        compiled_df = pd.DataFrame(compiled_data)

        st.success("Processing complete")
        st.dataframe(compiled_df, use_container_width=True)
