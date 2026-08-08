# AI Requirements Analyst

A small AI-assisted tool for analyzing software requirements.

## What it does

The tool takes a software requirement written in Markdown and uses an LLM to identify:

- Problem
- User Story
- Acceptance Criteria
- Assumptions
- Dependencies
- Open Questions
- Risks
- Unsupported Assumptions

The result is validated with Pydantic and exported as both JSON and Markdown.

## Workflow

Requirement
→ Prompt
→ Gemini API
→ Structured JSON
→ Pydantic validation
→ JSON + Markdown report

## Example

Input:

`requirements/example.md`

Output:

`output/example_analysis.json`

`output/example_analysis.md`

## Tech Stack

- Python
- Google Gemini API
- Pydantic
- python-dotenv

## Run

```bash
python src/analyze.py requirements/example.md


The project is designed as a small demonstration of AI-assisted requirements analysis rather than as a production-ready requirements management system.