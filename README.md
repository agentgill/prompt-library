# My Prompt Library

## Getting started

1. Install llm
2. Install ollama

## Basics

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

## Resources

- LLM <https://llm.datasette.io/en/stable/#>
- LLM Plugins & Models <https://llm.datasette.io/en/stable/plugins/directory.html#plugin-directory>
- Ollama <https://github.com/ollama>
- Ollama Docs <https://github.com/ollama/ollama/tree/main/docs>
- Ollama Models <https://ollama.com/search>
