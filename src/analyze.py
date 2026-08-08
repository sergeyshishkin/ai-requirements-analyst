import argparse
import json
from pathlib import Path

from llm import analyze_requirement


parser = argparse.ArgumentParser(
    description="Analyze a software requirement using an LLM."
)

parser.add_argument(
    "requirement",
    help="Path to the Markdown file containing the requirement.",
)

args = parser.parse_args()

requirement_path = Path(args.requirement)



requirement = requirement_path.read_text(encoding="utf-8")
prompt_path = Path("prompts/requirements_analysis.txt")
prompt_template = prompt_path.read_text(encoding="utf-8")
prompt = f"{prompt_template}\n{requirement}"
analysis = analyze_requirement(prompt)

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

output_path = output_dir / f"{requirement_path.stem}_analysis.json"

output_path.write_text(
    json.dumps(analysis.model_dump(), ensure_ascii=False, indent=2),
    encoding="utf-8",
)

markdown = f"""# Requirements Analysis
## Problem
{analysis.problem}
## User Story
{analysis.user_story}
## Acceptance Criteria
{chr(10).join(f"- {item}" for item in analysis.acceptance_criteria)}
## Assumptions
{chr(10).join(f"- {item}" for item in analysis.assumptions)}
## Dependencies
{chr(10).join(f"- {item}" for item in analysis.dependencies)}
## Open Questions
{chr(10).join(f"- {item}" for item in analysis.open_questions)}
## Risks
{chr(10).join(f"- {item}" for item in analysis.risks)}
## Unsupported Assumptions
{chr(10).join(f"- {item}" for item in analysis.unsupported_assumptions)}
"""
markdown_path = output_dir / f"{requirement_path.stem}_analysis.md"
markdown_path.write_text(markdown, encoding="utf-8")
print(f"Analysis saved to {output_path}")
print(f"Report saved to {markdown_path}")