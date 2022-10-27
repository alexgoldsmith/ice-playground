import json
from datetime import datetime
from ice.recipe import recipe
from parse_resume import parse_resume

RESUME = parse_resume()

COMPANY_DESC="""Revere, as a company, is about that robust and diverse network of trustworthy and smart individuals – that shift into the future of real estate – and we are the information and intelligence brand at the center of it.

We launched in July 2020 in the midst of the global health pandemic and recession, with the goal to revolutionize the $250 billion global brokerage and services industry and to become the daily homepage for commercial real estate professionals.

With 50+ years of capital markets, real estate, and engineering experience, we understand the pain avoided when equipped with the right technology, business and capital markets insights, access to key decision makers, and asset price discovery.
"""
BACKGROUND="""We're looking for a product-minded engineer to join our growing team. The Engineering team is responsible for planning and executing on bringing Revere's vision to life by building a one-stop-shop capital markets network supporting thousands of Commercial Real Estate capital markets users. 

Today, sourcing deals, underwriting them, and the capitalization process takes months. Data is silo'ed into Excel spreadsheets and Outlook contacts, which die or immediately go stale at the end of a transaction. Revere aims to solve these problem by:

1. Operating the first Capital Markets network with real time investment profiles / strategies, sponsor track records and up-to-date contact information.
2. Purpose built analytics / CRM tools to track and engage with the broader capital markets community. 
3. Leveraging predictive analytics and novel underwriting data sources to reduce time to capitalize multi-hundred million dollar deals and ultimately increasing transaction velocity.
"""
ROLE_DESC="""- Actively propose and/or develop UI components in React, server side APIs and data models in NodeJS / SQL.
- Architect solutions for longer-term roadmap (e.g. on-platform communication, warm-intro paths, large scale email distribution and analytics tracking) leveraging cloud infrastructure & resources (e.g. Redis, Kafka, etc.).
- Review, maintain, and improve existing features powering user workflows.
- Design and launch common infrastructure / processes that will improve team velocity, such as better CI/CD, DevOps & DevEx tooling.
- Thought leadership - periodic publication of interesting topics and assessments to share with the broader community.
"""
DESIRED_CANDIDATE_DESCRIPTION = """General Qualifications
- 1 – 3 years as a full-stack developer making web apps. We are looking for **generalists** who are enthusiastic about applying technology to solve problems.
- Familiarity with JavaScript frameworks such as Angular, Vue, or **React**.
- Familiarity with server side languages such as Python, Golang, or **Node.js.**
- Familiarity with relational database systems such as MySQL or **Postgres.**
- Familiarity with hosted public cloud infrastructure on AWS, Azure, or **GCP.**
- Bonus points for expertise in **TypeScript**.

Personal Qualifications
- **Independently Inquisitive**: Research and understand business needs, validating hypotheses with experiments and refining requirements based on results with minimal to no oversight.
- **High Velocity**: Sustained software development and decision making with endurance, nimble and willing to course correct where needed.
- **Craftsmanship**: Incredible attention to detail; placing the user and user journeys at the heart of software design and UI/UX.
- **Communicative**: Well articulated and capable of expressing complex requirements, dependencies or concerns concisely and with empathy.
"""


def compose_prompt() -> str:
    return f"""
Resume: "{RESUME}"
Company Description: "{COMPANY_DESC}"
Background: "{BACKGROUND}"
Role Description: "{ROLE_DESC}"
Desired Candidate Description: "{DESIRED_CANDIDATE_DESCRIPTION}"

Given the context above, I will write a cover letter in detail below, citing from my resume where appropriate:
""".strip()


async def create() -> str:
    letter_prompt = compose_prompt()
    letter = await recipe.agent().complete(prompt=letter_prompt, max_tokens=1000)
    suffix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"/workspaces/code/src/career/outputs/{suffix}.md", "w+") as f:
        f.write(letter)

recipe.main(create)
