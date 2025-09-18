# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Setup and Dependencies
- `uv sync` - Install and lock Python dependencies from pyproject.toml

### PDF to Markdown Conversion
- `uv run python src/to_markdown.py <pdf_path>` - Convert PDF to Markdown and save to output.md
- `uv run python src/loop_prompt.py <pdf_path>` - Process PDF page-by-page and display Markdown

### Running Prompts
- `llm < prompts/prompt_level1_ping.txt` - Run prompts using llm tool
- `ollama run llama3.2 < prompts/prompt_level2_comedian.txt` - Run prompts using ollama
- Output to file: `llm < prompts/prompt_level3_summarize.txt > output.md`

### Testing
- `uv run pytest` - Run tests when available (add tests under tests/ directory)

## Architecture

This is a prompt engineering library focused on PDF-to-Markdown workflows and reusable prompt templates. The repository demonstrates different prompt levels from basic text input to dynamic variables.

### Core Components
- **src/** - Python utilities for PDF processing using pymupdf4llm
  - `to_markdown.py` - CLI tool to convert PDFs to Markdown
  - `loop_prompt.py` - Page-by-page PDF processor
  - `get_markdown.py` - Additional Markdown extraction utility

- **prompts/** - Reusable prompt templates organized by complexity level
  - Level 1: Basic text input (prompt_level1_*.txt)
  - Level 2: Structured instructions (prompt_level2_*.txt)
  - Level 3: Examples-based prompts (prompt_level3_*.txt)
  - Level 4: Dynamic variables (prompt_level4_*.txt)
  - **phi_ignore/** - PHI-related prompts for medical/sensitive data
  - **encounters/** - Medical encounter analysis prompts

### Prompt Naming Convention
Follow pattern: `prompt_level<N>_<purpose>.txt` where N indicates complexity level

### Development Standards
- Python: PEP 8 style, type hints, snake_case naming
- Typer CLI pattern for command-line tools
- Keep side effects in `if __name__ == "__main__"` blocks
- Commit messages: Use conventional prefixes (feat:, chore:, docs:)