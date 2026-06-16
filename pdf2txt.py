import pdfplumber 
import re
doc = 'claude_const_2026.pdf'
doc_txt = 'claude_const_2026.txt'

with open(doc_txt, 'w') as txt:
    with pdfplumber.open(doc) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()

            if text:
                txt.write(f"\n======= PAGE {i} =======\n")
                text = re.sub(r"Claude's Constitution—January 2026\s+\d+", "", text)
                txt.write(text)
                txt.write("\n")
