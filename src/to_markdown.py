import pymupdf4llm
import typer
from typing import List

import pathlib


app = typer.Typer(name="extract-md")


@app.command()
def extract_md(pdf_path: str, pages: List[int]):
    md_text = pymupdf4llm.to_markdown(pdf_path, pages=pages)

    print(md_text)
    pathlib.Path("output.md").write_bytes(md_text.encode())


if __name__ == "__main__":
    app()
