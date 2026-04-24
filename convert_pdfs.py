import os
import glob
import pymupdf4llm

pdf_files = glob.glob('mathematics/*.pdf')
for pdf_file in pdf_files:
    md_file = pdf_file.replace('.pdf', '.md')
    print(f"Converting {pdf_file} to {md_file}...")
    try:
        md_text = pymupdf4llm.to_markdown(pdf_file)
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_text)
        print(f"Successfully converted {pdf_file}")
    except Exception as e:
        print(f"Failed to convert {pdf_file}: {e}")
