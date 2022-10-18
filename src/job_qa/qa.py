from ice.recipe import recipe

EXPERIENCE = """EXPERIENCE

Company name: GreenShell, LLC
Job Title: Full Stack Developer
Dates of employment: Aug 2022 - Present
Place of employment: Madison, Wisconsin

Company name: Epic Systems Corporation
Job title: Technical Solutions Engineer
Dates of employment: Dec 2019 - Jun 2021
Place of employment: Madison, Wisconsin

Responsibilities and Accomplishments:
- Developed pages and UI components using Next.js, React, and Tailwind.
- Designed all digital graphics appearing on the website

Responsibilities and Accomplishments
- Ensured continued success of 6 hospital system organizations live on Epic’s registration and real-time eligibility applications through dozens of major software upgrades.
- Consistently maintained a success rate (greater than 90%) for First Response Time targets within the top half of the application support team.
- Investigated techincal bugs encountered by customers via methods such as code walkthroughs, application testing, and code debugging. Achieved customer-accepted resolution of 100% of submitted issues.
- Owned high-impact customer issues from discovery to resolution, including issues within other Epic applications.
- Documented customer requirements, technical bugs and broken workflows, application functionality, and user feedback.
- Provided technical expertise to a customer implementation project, while mentoring the customer’s long-term support engineer.
"""

EDUCATION= """EDUCATION
School: University of Wisconsin - Madison
Dates of attendance: Dec 2020 - present
Place of attendance: Madison, Wisconsin
Certificate: Professional Capstone Certificate in Computer Sciences (in progress)

School: Clemson University
Dates of attendance: Aug 2018 - Aug 2019
Place of attendance: Clemson, South Carolina
Degree: Master of Arts, Economics

School: Clemson University
Dates of attendance: Aug 2018 - Aug 2019
Place of attendance: Clemson, South Carolina
Degree: Master of Arts, Economics
"""

COMPANY_DESC="""stuff"""
ROLE_DESC="""stuff"""
DESIRED_CANDIDATE_DESCRIPTION = """stuff"""


def compose_prompt(context: str, question: str) -> str:
    return f"""
Background text: "{context}"

Question: "{question}"
Answer: "
""".strip()


async def answer(
    context: str = DEFAULT_CONTEXT, question: str = DEFAULT_QUESTION
) -> str:
    prompt = make_qa_prompt(context, question)
    answer = await recipe.agent().complete(prompt=prompt, stop='"')
    return answer


recipe.main(answer)
