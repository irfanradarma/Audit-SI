from pypdf import PdfReader
import re
reader = PdfReader(r'C:\Users\USER\OneDrive - Kemenkeu\PKN STAN\Audit SI\Externals\COBIT_2019_Framework_Governance.pdf')
text = '\n'.join(page.extract_text() or '' for page in reader.pages)
for pattern in ['EDM01', 'EDM02', 'EDM03', 'EDM04', 'EDM05', 'APO01', 'APO02', 'BAI01', 'DSS01', 'MEA01']:
    print('===', pattern, '===')
    for m in re.finditer(pattern, text):
        s = max(0, m.start()-400)
        e = min(len(text), m.end()+2200)
        chunk = text[s:e]
        print(chunk)
        print('---')
        break
