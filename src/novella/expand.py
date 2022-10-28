from pathlib import Path
from datetime import datetime
from ice.recipe import recipe


TIPS = """Here are some writing tips:
- Focus on the interactions of characters.
- Show, don't tell.
- The plot should be driven by dialogue and action.
- Minimize exposition.
Let's make sure to use these writing tips when we compose our passage below.

"""

STYLE = """Since we are writing a science fiction novel, let's draw inspiration from the following authors:
- Kurt Vonnegut
- Joseph Heller
- Isaac Asimov
- Robert Heinlein
- Arthur C. Clarke
- Blake Crouch

"""

DIR = Path(__file__).parent.resolve()

def make_prompt(context: str) -> str:
    return f"""
Here is a passage from a chapter of a novel: "{context}"

{TIPS}
{STYLE}

Let's continue writing, starting by repeating the last sentence of the passage above.
""".strip()

# example usage: python expand.py --file "chapter_1.md"
async def expand(file: str = "default.md") -> str:
    context = (DIR / file).read_text()
    prompt = make_prompt(context)
    response = await recipe.agent().complete(prompt=prompt, max_tokens=3000)

    suffix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    new_file = DIR / "outputs" / f"{file}_{suffix}.md"

    with new_file.open("w+") as f:
        f.write(response)
    return response 


recipe.main(expand)
