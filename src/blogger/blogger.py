from pathlib import Path
from datetime import datetime
from ice.recipe import recipe

TOPIC = """Precision medicine and population health"""

def get_thesis_prompt(topic: str) -> str:
    return f"""We are given a topic and asked to write a thesis statement.

Topic: {topic}

Thesis:
"""

def get_outline_prompt(topic: str, thesis: str) -> str:
    return f"""Let's first pick a topic and write an outline for an essay.

Here is an example of an outline format:

Topic: AI and education

Thesis: Although AI has the potential to improve education, there are several risks associated with its implementation that must be addressed.

Outline: 

1. Introduction
    1. Attention-grabbing opening
    2. Thesis statement:  Although AI has the potential to improve education, there are several risks associated with its implementation that must be addressed.
    3. Background information on AI in education
    4. Overview of main points

2. Body Paragraph 1
    1. Point: AI may exacerbate the achievement gap.
    2. Support 1: AI could be used to personalize learning for each student, but this could lead to some students getting ahead while others fall behind.
    3. Support 2: AI could also be used to select and track which students receive the best resources, leading to a further widening of the achievement gap.
    4. Rebuttal: AI could help to close the achievement gap by giving all students access to the same information and resources.
    5. Conclusion: Whether or not AI actually ends up closing the achievement gap is yet to be seen, but it has the potential to exacerbate the problem.

3. Body Paragraph 2
    1. Point: AI may lead to a decrease in critical thinking skills.
    2. Support 1: If students are relying on AI to do all of their learning for them, they may not develop the critical thinking skills they need.
    3. Support 2: AI could also be used to grade students' work, which could incentivize them to find ways to game the system instead of developing their own critical thinking skills.
    4. Rebuttal: AI could help students to develop critical thinking skills by providing them with instant feedback on their work.
    5. Conclusion: Whether or not AI leads to a decrease in critical thinking skills depends on how it is implemented, but there is potential for it to have a negative impact.

4. Body Paragraph 3
    1. Point: AI may lead to a loss of jobs for teachers.
    2. Support 1: If AI is used to personalize learning for each student, there may be less of a need for teachers.
    3. Support 2: AI could also be used to grade students' work, which would lead to a decrease in the need for teachers.
    4. Rebuttal: AI could help teachers by giving them more time to focus on other tasks or by providing them with instant feedback on students' work.
    5. Conclusion: While AI may have some potential benefits for teachers, it also poses a threat to their jobs.

5. Body Paragraph 4
    1. Point: The implications of AI in education extend beyond the loss of jobs for teachers.
    2. Support 1: AI has the potential to change the power dynamics in education, with students having more control over their learning and teachers being more like facilitators.
    3. Support 2: AI could also lead to a more standardized form of education, which may not be beneficial for all students.
    4. Rebuttal: AI could actually help to customize education for each student and make it more individualized.
    5. Conclusion: While there are some potential positives to AI in education, the negatives outweigh them because of the ways it could potentially harm society and devalue human creativity.

6. Conclusion
    1. Restate thesis statement
    2. Summarize main points
    3. Call to action or final thoughts

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
