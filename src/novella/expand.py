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
    return f"""We are writing a science fiction novel.

{STYLE}
{TIPS}

Here the passage so far: "{context}"

Let's continue writing the passage below, starting by repeating the last paragraph of the passage above:
""".strip()

# example usage: python expand.py --file "chapter_1.md"
async def expand(file: str = "ch_1.md") -> str:
    context = (DIR / file).read_text()
    prompt = make_prompt(context)
    response = await recipe.agent().complete(prompt=prompt, max_tokens=2000)

    suffix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    new_file = DIR / "outputs" / f"{file}_{suffix}.md"

    with new_file.open("w+") as f:
        f.write(response)
    return response 


recipe.main(expand)
