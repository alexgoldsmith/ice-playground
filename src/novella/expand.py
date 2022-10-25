from pathlib import Path
from datetime import datetime
from ice.recipe import recipe


TIPS = """Here are some writing tips:
Maintain the theme and style of the passage, but continue the plot in a way that is interesting and compelling.
Focus on the interactions of characters, and keep most of the passage limited to dialogue.
"""

def make_prompt(context: str) -> str:
    return f"""
Here is a passage from a chapter of a novel: "{context}"

{TIPS}

Let's now continue writing the passage at length starting from the end of the passage above. 
""".strip()

# example usage: python expand.py --file "chapter_1.md"
async def expand(file: str = "/code/src/novella/test2.md") -> str:
    context = Path(file).read_text()
    prompt = make_prompt(context)
    # set breakpoint
    response = await recipe.agent().complete(prompt=prompt, max_tokens=2000)
    suffix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"{file}_{suffix}.md", "w+") as f:
        f.write(response)
    return response 


recipe.main(expand)
