# My Prompt Library

Reusable & customizable set of prompts and resources for prompt engineering.

"The prompt is the new fundamental unit of knowledge work"

## Level 1 Prompt - Text

Basic free-text input "tell me a joke".

## Level 2 Prompt - Structure your prompt

Reusable Prompt that you can use to solve well defined problems where you specify additional information upfront using static variables.

## Getting started

1. Install llm
2. Install ollama

## Basic Text

List Models

`llm models`

Add Bedrock Models

- `llm install llm-bedrock-anthropic`

Add Anthropic Models - Claude 3

- `llm install llm-claude-3`

Ping

- `llm < prompts/prompt_lvl1_ping.txt`

Count

- `llm < prompts/prompt_lvl1_count.txt`

Ping Bedrock

- `llm -m bedrock-claude-v3.5-sonnet < prompts/prompt_lvl1_ping.txt`

Count Bedrock Model Override

- `llm -m bedrock-claude-sonnet -o bedrock_model_id us.anthropic.claude-3-5-sonnet-20241022-v2:0 < prompts/prompt_lvl1_count.txt`

Ping using ollama & llama3.2

- `ollama run llama3.2 < prompts/prompt_lvl1_count.txt`

or using qwen2.5

- `ollama run qwen2.5-coder < prompts/prompt_lvl1_count.txt`

List ollama models

- `ollama list`

## Basic Structured Prompt

Structured prompt

- `ollama run llama3.2 < prompts/prompt_lvl2.xml`

## Resources

- LLM <https://llm.datasette.io/en/stable/#>
- LLM Plugins & Models <https://llm.datasette.io/en/stable/plugins/directory.html#plugin-directory>
- Ollama <https://github.com/ollama>
- Ollama Docs <https://github.com/ollama/ollama/tree/main/docs>
- Ollama Models <https://ollama.com/search>
- Pymupdf <https://pymupdf.readthedocs.io/en/latest/index.html>
- Pymupdf4llm <https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/index.html>
- Typer <https://typer.tiangolo.com/>
