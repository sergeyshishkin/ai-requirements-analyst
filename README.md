# AI Requirements Analyst
A small AI-assisted tool for analyzing software requirements.

## What it does
The tool takes a software requirement written in Markdown and uses a configured LLM provider to analyze it.

The analysis covers:
* Problem
* User Story
* Acceptance Criteria
* Assumptions
* Dependencies
* Open Questions
* Risks
* Unsupported Assumptions

The LLM response is validated against a Pydantic schema and then exported as both JSON and Markdown.

## Architecture
The application separates the analysis workflow from the LLM provider.
The provider is selected using the `LLM_PROVIDER` environment variable.


## Example
Input:
`requirements/example.md`

Output:
`output/example_analysis.json`
`output/example_analysis.md`


## Tech Stack
* Python
* Google Gemini API
* OpenRouter API
* Pydantic
* python-dotenv

## Installation
Install the project dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file with your API keys and select the LLM provider:
LLM_PROVIDER=gemini
Supported providers: gemini, openrouter

## Run
```bash
python src/analyze.py requirements/example.md
```

## Note
This project is a small demonstration of an AI-assisted requirements analysis workflow. It is not intended to be a production-ready requirements management system.
