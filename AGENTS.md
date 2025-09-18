# Repository Guidelines

## Project Structure & Module Organization
Core Python utilities for PDF-to-Markdown workflows live in `src/` (`to_markdown.py`, `loop_prompt.py`, `get_markdown.py`). Prompt templates and reusable scripts are grouped under `prompts/`, organized by level and topic—follow the existing naming (e.g., `prompt_level3_summarize.txt`). Keep reference PDFs in `pdfs/` and generated experiments in `downloads/` or `output.md` so reviewers can reproduce results quickly.

## Build, Test, and Development Commands
- `uv sync` — install and lock Python dependencies defined in `pyproject.toml` and `uv.lock`.
- `uv run python src/to_markdown.py --help` — inspect CLI options for exporting Markdown from PDFs.
- `uv run python src/loop_prompt.py pdfs/input.pdf` — iterate through pages and print Markdown for validation.
- `uv run pytest` — execute automated tests once they exist; add `tests/` modules alongside new utilities.
- `llm < prompts/prompt_level1_count.txt` or `ollama run llama3.2 < prompts/...` — smoke-test prompt templates using the same commands documented in `README.md`.

## Coding Style & Naming Conventions
Write Python in PEP 8 style with four-space indents, type hints, and descriptive snake_case names. Mirror existing Typer CLIs when adding commands, and keep side effects in `if __name__ == "__main__"` blocks. Store prompt files as lowercase underscore names that convey purpose and level, and document any new workflow in `README.md` or directory-level `README` files.

## Testing Guidelines
Adopt `pytest` for new features; co-locate fixtures under `tests/` mirroring the `src/` package structure. Name test files `test_<module>.py` and cover both success paths and prompt edge cases (e.g., empty variables). When adding prompts, capture a short transcript in `downloads/` or commit message so reviewers can verify expected behavior manually.

## Commit & Pull Request Guidelines
Follow Conventional Commit prefixes seen in history (`feat:`, `chore:`, `docs:`) and keep messages in the imperative mood. Reference related issues, summarize prompt changes, and note any model/runtime requirements. Pull requests should include a brief testing note (commands executed, sample outputs) and screenshots or Markdown snippets when the change affects generated content.

## Prompt Contribution Tips
Prefer incremental additions: clone an existing prompt template, annotate dynamic variables at the top, and include inline comments for agents when necessary. Validate new prompts against both `llm` and `ollama` runners, and add guidance in the prompt header on the recommended model or context size. If a prompt depends on external assets, commit them under `pdfs/` or link to accessible sources in the PR description.
