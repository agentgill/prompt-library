import pymupdf4llm
import pymupdf
import typer

app = typer.Typer(name="loop-prompt")


@app.command()
def loop_prompt(pdf_path: str):
    doc = pymupdf.open(pdf_path, filetype="pdf")
    pages = doc.page_count
    print(f"total_pages: {pages}")

    for page in range(pages):
        md_text = pymupdf4llm.to_markdown(pdf_path, pages=[page])
        print(f"markdown for page {page}:\n\n {md_text}")


if __name__ == "__main__":
    app()
