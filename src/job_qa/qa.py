import json

from ice.recipe import recipe
from src.job_qa.parse_resume import parse_resume




RESUME = parse_resume()
COMPANY_DESC="""stuff"""
ROLE_DESC="""stuff"""
DESIRED_CANDIDATE_DESCRIPTION = """stuff"""

QUESTION = """stuff"""


def compose_prompt(question: str) -> str:
    return f"""
Resume: "{RESUME}"
Company Description: "{COMPANY_DESC}"
Role Description: "{ROLE_DESC}"
Desired Candidate Description: "{DESIRED_CANDIDATE_DESCRIPTION}"

Question: "{question}"

Using the context provided above, we construct the best possible answer below:
""".strip()


async def answer(question: str = QUESTION
) -> str:
    prompt = compose_prompt(question)
    answer = await recipe.agent().complete(prompt=prompt, stop='"')
    return answer


# recipe.main(answer)
