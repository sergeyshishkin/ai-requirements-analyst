import os

from dotenv import load_dotenv
from openai import OpenAI

from schema import RequirementAnalysis


load_dotenv()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)


def analyze_requirement(prompt: str) -> RequirementAnalysis:
    response = client.chat.completions.create(
        model="google/gemma-4-26b-a4b-it:free",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "requirement_analysis",
                "strict": True,
                "schema": RequirementAnalysis.model_json_schema(),
            },
},
    )

    content = response.choices[0].message.content

    return RequirementAnalysis.model_validate_json(content)