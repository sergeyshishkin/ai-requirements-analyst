from pydantic import BaseModel


class RequirementAnalysis(BaseModel):
    problem: str
    user_story: str
    acceptance_criteria: list[str]
    assumptions: list[str]
    dependencies: list[str]
    open_questions: list[str]
    risks: list[str]
    unsupported_assumptions: list[str]