import os

from dotenv import load_dotenv
from google import genai

from schema import RequirementAnalysis


load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def analyze_requirement(prompt: str) -> RequirementAnalysis:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": RequirementAnalysis,
        },
    )

    return RequirementAnalysis.model_validate_json(response.text)