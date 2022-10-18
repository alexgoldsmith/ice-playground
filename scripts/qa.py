from ice.recipe import recipe


DEFAULT_CONTEXT = "We're running a hackathon on 9/9/2022 to decompose complex reasoning tasks into subtasks that are easier to automate & evaluate with language models. Our team is currently breaking down reasoning about the quality of evidence in randomized controlled trials into smaller tasks e.g. placebo, intervention adherence rate, blinding procedure, etc."

DEFAULT_QUESTION = "What is happening on 9/9/2022?"


def make_qa_prompt(context: str, question: str) -> str:
    return f"""
Background text: "{context}"

Answer the following question about the background text above:

Question: "{question}" 
Answer: "
""".strip()

async def answer(
    context: str = DEFAULT_CONTEXT, question: str = DEFAULT_QUESTION
) -> str:
    prompt = make_qa_prompt(context, question)
    answer = await recipe.agent().complete(prompt=prompt, stop='"')
    return answer

def make_qa_prompt_improve(context: str, question: str, answer: str) -> str:
    return f"""
Background text: "{context}"

The question about the background text is: "{question}"
 
The answer to the question about the background text above was: "{answer}":

Let's improve the answer to the question above by thinking step by step about the answer.
""".strip()

async def improve_answer(
    context: str = DEFAULT_CONTEXT, question: str = DEFAULT_QUESTION , answer: str = ""
) -> str:
    prompt = make_qa_prompt_improve(context, question, answer)
    answer = await recipe.agent().complete(prompt=prompt, stop='"')
    return answer

async def main():
    first_answer = await answer()
    improved_answer = await improve_answer(answer=first_answer)
    return improved_answer


recipe.main(main)