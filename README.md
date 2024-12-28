# My Prompt Library

Reusable & customizable set of prompts and resources for prompt engineering.

> "The Prompt is the new fundamental unit of knowledge work" by IndyDevDan

## Level 1 Prompt - Basic Text Input

Basic free-text input "tell me a joke".

## Level 2 Prompt - Structured Intructions

Reusable Prompt that you can use to solve well defined problems where you specify additional information upfront using static variables.

## Level 3 Prompt - Give Examples

Use & provide examples

## Level 4 Prompt - Dynamic Variables

## Getting started

- Install uv `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Install llm `brew install llm`
- Install ollama `https://ollama.com/download`
- List ollama models `ollama models`
- List llm models `llm models`
- See default model `llm models default`

## Level 1 - Basic Input

Pinging

- `llm < prompts/prompt_level1_ping.txt`

Counting

- `llm < prompts/prompt_level1_count.txt`

Ping using ollama & llama3.2

- `ollama run llama3.2 < prompts/prompt_level1_count.txt`

## Level 2 -  Structured Prompt

Structured prompt

- `ollama run llama3.2 < prompts/prompt_level2_comedian.txt`

## Level 3 - With Examples

Guide the LLM (input and output file)

- `llm -o bedrock_model_id us.anthropic.claude-3-5-sonnet-20241022-v2:0 < prompts/prompt_level3_summarize.txt > output.md`

## Level 4 - Make scalable

Use dymnamic variables and create scalable prompts on the fly

- Specific purpose
- Specific instructions
- Specific examples
- Dynamic Variables

It's all just prompts.

## Models

How to install models

- Install AWS Bedrock Anthropic `llm install llm-bedrock-anthropic`
- Install Anthropic Models for direct API access `llm install llm-claude-3`
- Install Groq Models `llm install llm-groq`

## Resources

- LLM <https://llm.datasette.io/en/stable/#>
- LLM Plugins & Models <https://llm.datasette.io/en/stable/plugins/directory.html#plugin-directory>
- Ollama <https://github.com/ollama>
- Ollama Docs <https://github.com/ollama/ollama/tree/main/docs>
- Ollama Models <https://ollama.com/search>
- Pymupdf <https://pymupdf.readthedocs.io/en/latest/index.html>
- Pymupdf4llm <https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/index.html>
- Typer <https://typer.tiangolo.com/>
- UV <https://docs.astral.sh/uv/getting-started/installation/>
