import streamlit as st
import pandas as pd
import zipfile
import tempfile
from pathlib import Path
import os

st.set_page_config(page_title="UTS PG", layout="wide")
st.title("📦 ZIP → Excel → DataFrame")

uploaded_zip = st.file_uploader("Upload ZIP file yang di-email yah", type=["zip"])

A, B, C, D = "A", "B", "C", "D"

answer_key = {
    1:[A], 2:[B], 3:[B], 4:[D], 5:[C],
    6:[D], 7:[B], 8:[A], 9:[C], 10:[D],
    11:[A], 12:[B], 13:[C], 14:[D], 15:[C],
    16:[B], 17:[B], 18:[A], 19:[C], 20:[A],
    21:[D], 22:[D], 23:[C], 24:[B], 25:[A],
    26:[A], 27:[A], 28:[C], 29:[B], 30:[D],
    31:[C], 32:[C], 33:[A], 34:[D],
    35:[A, B],
    36:[B], 37:[D], 38:[B], 39:[C], 40:[D],
    41:[D],
    42:[A, D],
    43:[B], 44:[A], 45:[B],
    46:[C], 47:[D], 48:[C], 49:[A], 50:[D]
}

if uploaded_zip is not None:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        zip_path = tmp_path / uploaded_zip.name
        with open(zip_path, "wb") as f:
            f.write(uploaded_zip.read())

        try:
            with zipfile.ZipFile(zip_path, "r") as z:
                z.extractall(tmp_path)
        except zipfile.BadZipFile:
            st.error("Uploaded file is not a valid ZIP.")
            st.stop()

        extracted_items = [p for p in tmp_path.iterdir() if p.name != uploaded_zip.name]
        working_dir = extracted_items[0] if len(extracted_items) == 1 and extracted_items[0].is_dir() else tmp_path

        zip_files = list(working_dir.rglob("*.zip"))
        if not zip_files:
            st.warning("No ZIP files found inside the uploaded file.")
            st.stop()

        compiled_data = {
            "names": [],
            "npm": [],
            "skor": []
        }
        for i in range(1, 51):
            compiled_data[f"Q{i}"] = []

        # -----------------------------------------
        # Process each student's ZIP
        # -----------------------------------------
        for zp in zip_files:
            try:
                with zipfile.ZipFile(zp, "r") as z:
                    excel_files = [f for f in z.namelist() if f.endswith((".xlsx", ".xls"))]

                    for excel_file in excel_files:
                        with z.open(excel_file) as ef:
                            df_ID = pd.read_excel(ef, sheet_name="ID", engine="openpyxl")
                            name = df_ID.iloc[3, 3]
                            npm = df_ID.iloc[5, 3]

                        with z.open(excel_file) as ef:
                            df_PG = pd.read_excel(ef, sheet_name="PG", engine="openpyxl")
                            jawaban = df_PG.iloc[:, [0, 5]]
                            jawaban.columns = ["No", "Jawaban"]
                            jawaban = jawaban[jawaban["No"].notna()]

                        compiled_data["names"].append(name)
                        compiled_data["npm"].append(npm)

                        skor = 0
                        student_answers = {f"Q{i}": None for i in range(1, 51)}

                        for _, row in jawaban.iterrows():
                            try:
                                no = int(row["No"])
                                ans = str(row["Jawaban"]).strip().upper()
                                if 1 <= no <= 50:
                                    student_answers[f"Q{no}"] = ans
                                    if ans in answer_key.get(no, []):
                                        skor += 1
                            except Exception:
                                continue

                        for i in range(1, 51):
                            compiled_data[f"Q{i}"].append(student_answers[f"Q{i}"])

                        compiled_data["skor"].append(skor)

            except zipfile.BadZipFile:
                st.warning(f"Skipped invalid ZIP: {zp.name}")

        compiled_df = pd.DataFrame(compiled_data)

        st.success("✅ Processing complete")
        st.dataframe(compiled_df, use_container_width=True)
