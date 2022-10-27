import json

from ice.recipe import recipe
from src.career.parse_resume import parse_resume

RESUME = parse_resume()
COMPANY_DESC="""Ought is a product-driven machine learning lab building Elicit, an AI research assistant. Elicit uses language models to automate and support research processes like literature and evidence review. Elicit applies frontier technology to serious use cases, enabling our research team to understand in great detail where language models fail and how to mitigate such failures."""
ROLE_DESC="""As an intern at Ought, you will be given ownership over a project. Some examples of possible projects:

Improve the performance of question-answering models on open-ended reasoning
Use language models to partially automate the creation of datasets for a contrastive, metric, or generative task
Fine-tune language models on parts of the systematic review process while coming up with novel ways to evaluate and improve their performance
Besides your main project, you may:

Generally improve and evaluate language model tasks
Do full-stack web development
Provide ideas and feedback to shape the future of Elicit
"""
DESIRED_CANDIDATE_DESCRIPTION = """Strong candidates will have software development experience and some familiarity with natural language processing. The role is flexible on the spectrum between NLP and production machine learning engineering. Some specific skills that are helpful:

Backend web development and experience working with distributed systems
Experience with software design and working writing readable, extensible code
Experience applying natural language processing e.g. projects utilizing transformers
Understanding of and interest in large generative pre-trained models like GPT-3 is a plus
We encourage you to apply if you're not sure if you'd be a good fit and are excited about Ought's mission.
"""

QUESTION = """Why are you interested in working at Ought?"""


def compose_prompt(question: str) -> str:
    return f"""
Resume: "{RESUME}"
Company Description: "{COMPANY_DESC}"
Role Description: "{ROLE_DESC}"
Desired Candidate Description: "{DESIRED_CANDIDATE_DESCRIPTION}"

Question: "{question}"

Given the context above, I answer the question in detail below, citing from my resume where appropriate:
""".strip()


async def answer(question: str = QUESTION
) -> str:
    prompt = compose_prompt(question)
    return await recipe.agent().complete(prompt=prompt, stop='"')

recipe.main(answer)
