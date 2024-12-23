from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("pdfs/input.pdf")
print(result.text_content)
