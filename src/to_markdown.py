import pathlib
from typing import List

import pymupdf4llm
import typer

app = typer.Typer(name="extract-md")


def extract_md(pdf_path: str, pages: List[int] = None):
    md_text = pymupdf4llm.to_markdown(pdf_path, pages=pages)

    print(md_text)
    pathlib.Path("output.md").write_bytes(md_text.encode())


if __name__ == "__main__":
    typer.run(extract_md)
