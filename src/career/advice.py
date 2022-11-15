import json

from ice.recipe import recipe
from parse_resume import parse_resume

RESUME = parse_resume()

QUESTION = """What can I do to get hired?"""


def compose_prompt(question: str) -> str:
    return f"""
Resume: "{RESUME}"

Question: "{question}"

Advice:
""".strip()


async def answer(question: str = QUESTION
) -> str:
    prompt = compose_prompt(question)
    return await recipe.agent().complete(prompt=prompt, max_tokens=1000, stop='"')

recipe.main(answer)
