import pymupdf4llm

md_text = pymupdf4llm.to_markdown("./pdfs/input.pdf", pages=[1, 2])

print(md_text)
