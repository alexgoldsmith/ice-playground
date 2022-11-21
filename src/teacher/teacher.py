from pathlib import Path
from datetime import datetime
from ice.recipe import recipe
from examples.formik_react_next_form import OUTLINE

TOPIC = """How do I make a write an Node.js api call to send an email?"""

def get_outline_prompt(topic: str) -> str:
    return f"""
Let's take a question and write a detailed outline for an extensive technical blog post explaining the solution step-by-step.

Here is an example of a question and corresponding outline:

{OUTLINE}

Let's use this example to write an outline based on the topic below.
We should outline at least 4 body paragraphs, though we can write more if we want.

Question: {topic}

Outline:

""".strip()


def get_blog_post_prompt(topic: str, outline: str) -> str:
    return f"""We are given a topic and outline for a blog post.

Topic: {topic}
    
Outline: {outline}

Each body paragraph should be at least 4 sentences long.
We need a compelling introduction and conclusion, along with a well-organized body.
We should also make sure to use a variety of transitions to connect our ideas.
Make sure to use a variety of sentence structures and sophisticated vocabulary.

Below is the published version of our blog post. 

Blog post:
""".strip()

async def generate_post(topic: str = TOPIC) -> str:

    outline_prompt = get_outline_prompt(topic)
    outline = await recipe.agent().complete(prompt=outline_prompt, max_tokens=800, stop='"')

    blog_prompt = get_blog_post_prompt(topic, outline)
    blog_post = await recipe.agent().complete(prompt=blog_prompt, max_tokens=3400)

    suffix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"./outputs/{suffix}.md", "w+") as f:
        f.write(f"{topic}\n\n{outline}\n\n{blog_post}")

    return blog_post

recipe.main(generate_post)
