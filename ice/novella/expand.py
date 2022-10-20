from pathlib import Path
from secrets import randbelow
from ice.recipe import recipe

DEFAULT_CONTEXT = "I stare out the window. My building is on the edge of the city and beyond it is only wilderness. I can't see any other buildings from my window, which is probably why I chose this apartment. I like feeling like I'm the only person for miles, even though I know I'm not."

def get_context() -> str:
    return Path('chapter_1.md').read_text()

def make_prompt(context: str) -> str:
    return f"""
Passage from a chapter of a novel: "{context}"

Continue writing the chapter from the passage above:

Contination: "
""".strip()


async def expand() -> str:
    context = get_context()
    prompt = make_prompt(context)
    response = await recipe.agent().complete(prompt=prompt, stop='"')
    id = randbelow(99999)
    with open(f"out_{id}.md", "w+") as f:
        f.write(response)
    return response 


recipe.main(expand)
