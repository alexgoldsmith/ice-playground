from pathlib import Path
from datetime import datetime
from ice.recipe import recipe
from examples.persuasive_essay import OUTLINE

TOPIC = """Precision medicine and population health"""

def get_thesis_prompt(topic: str) -> str:
    return f"""We are given a topic and asked to write a thesis statement.

Topic: {topic}

Thesis:
"""

def get_outline_prompt(topic: str, thesis: str) -> str:
    return f"""Let's first pick a topic and write an outline for an essay.

Here is an example of an outline format:

{OUTLINE}

Let's use this example to write an outline based on the topic below.
We should outline at least 4 body paragraphs, though we can write more if we want.

Topic: {topic}

Thesis: {thesis}

Outline:

""".strip()


def get_blog_post_prompt(topic: str, outline: str) -> str:
    return f"""We are given a topic and outline for an essay.

Topic: {topic}
    
Outline: {outline}

Each body paragraph should be at least 4 sentences long.
We need a compelling introduction and conclusion, along with a well-organized body.
We should also make sure to use a variety of transitions to connect our ideas.
Make sure to use a variety of sentence structures and sophisticated vocabulary.

Below is the published version of our essay. 
Essay:
""".strip()


async def generate_post(topic: str = TOPIC) -> str:
    thesis_prompt = get_thesis_prompt(topic)
    thesis = await recipe.agent().complete(prompt=thesis_prompt, max_tokens=300, stop='"')

    outline_prompt = get_outline_prompt(topic, thesis)
    outline = await recipe.agent().complete(prompt=outline_prompt, max_tokens=800, stop='"')

    blog_prompt = get_blog_post_prompt(topic, outline)
    blog_post = await recipe.agent().complete(prompt=blog_prompt, max_tokens=2400)

    suffix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"./outputs/{suffix}.md", "w+") as f:
        f.write(f"{topic}\n\n{outline}\n\n{blog_post}")

    return blog_post

recipe.main(generate_post)
