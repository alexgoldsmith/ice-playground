from ice.recipe import recipe
import json

RESUME_JSON = {
  "headings": {
    "work": "Work Experience",
    "education": "Education",
    "skills": "Skills",
    "awards": "",
    "projects": "Projects"
  },
  "basics": {
    "name": "Alex Goldsmith",
    "email": "gold.alex.smith@gmail.com",
    "phone": "8644983481",
    "website": "alexgoldsmith.me",
    "location": {
      "address": "Madison, Wisconsin"
    }
  },
  "education": [
    {
      "institution": "University of Wisconsin - Madison",
      "location": "Madison, Wisconsin",
      "endDate": "Present",
      "startDate": "Dec 2020",
      "studyType": "Professional Capstone Certificate in Computer Sciences (in progress)"
    },
    {
      "institution": "Clemson",
      "location": "Clemson, South Carolina",
      "studyType": "MA",
      "area": "Economics",
      "gpa": "3.49",
      "startDate": "Aug 2018",
      "endDate": "Aug 2019"
    },
    {
      "institution": "Clemson University",
      "location": "Clemson, South Carolina",
      "studyType": "BA",
      "area": "Economics",
      "gpa": "3.51",
      "startDate": "Aug 2015",
      "endDate": "May 2018"
    }
  ],
  "work": [
    {
      "location": "Madison, Wisconsin",
      "position": "Full Stack Developer",
      "website": "",
      "startDate": "Aug 2022",
      "highlights": [
        "Developed pages and UI components using Next.js, React, and Tailwind.",
        "Designed all digital graphics appearing on the website"
      ],
      "company": "GreenShell, LLC",
      "endDate": "Present"
    },
    {
      "highlights": [
        "Ensured continued success of 6 hospital system organizations live on Epic’s registration and real-time eligibility applications through dozens of major software upgrades.",
        "Consistently maintained a success rate (greater than 90%) for First Response Time targets within the top half of the application support team.",
        "Investigated technical bugs encountered by customers via methods such as code walkthroughs, application testing, and code debugging. Achieved customer-accepted resolution of 100% of submitted issues.",
        "Owned high-impact customer issues from discovery to resolution, including issues within other Epic applications.",
        "Documented customer requirements, technical bugs and broken workflows, application functionality, and user feedback.",
        "Provided technical expertise to a customer implementation project, while mentoring the customer’s long-term support engineer."
      ],
      "company": "Epic Systems Corporation",
      "position": "Technical Solutions Engineer",
      "location": "Madison, Wisconsin",
      "startDate": "Dec 2019",
      "endDate": "Jun 2021"
    },
    {
      "highlights": [
        ""
      ]
    }
  ],
  "skills": [
    {
      "name": "Programming Languages",
      "level": "",
      "keywords": [
        "Python, TypeScript, JavaScript, C++, Java, MUMPS"
      ]
    },
    {
      "keywords": [
        "React, React-Native, Svelte, Astro, Remix"
      ],
      "name": "Front-end Frameworks"
    },
    {
      "keywords": [
        "SQL, SQLite, MySQL, SQL Server, MongoDB, Firebase, Relational & Document Models"
      ],
      "name": "Database Technologies"
    },
    {
      "keywords": [
        "Google Cloud Platform (GCP), Microsoft Azure"
      ],
      "name": "Cloud Platforms"
    },
    {
      "keywords": [
        "NodeJS, Jest, Git, Docker, CMake, JSON, HTML, CSS, REST APIs, X12, LaTeX"
      ],
      "name": "Other Technologies"
    },
    {
      "keywords": [
        "Competent and flexible team-leadership via carefully considered emotional intelligence"
      ],
      "name": "Leadership"
    },
    {
      "keywords": [
        " Capable time management through careful single-source of truth calendar use. Reliable task management with intelligent prioritization"
      ],
      "name": "Organization"
    },
    {
      "keywords": [
        "Skilled written (email, support tickets, technical documentation) and interpersonal communication"
      ],
      "name": "Communication"
    },
    {
      "keywords": [
        "Adept innovative and entreprenurial skills combined with problem-solving acumen"
      ],
      "name": "Creativity"
    }
  ],
  "projects": [
    {
      "name": "Developer blog",
      "url": "https://alexander.me",
      "keywords": [
        "Astro.js"
      ],
      "description": "Personal site hosting my resume, featured projects, and a blog"
    },
    {
      "keywords": [
        "Astro.js, Python, BeautifulSoup"
      ],
      "name": "E-learning site migration",
      "description": "Currently working on a project to migrate legacy e-learning site to a modern design. I am using the Astro framework (JAMstack architecture) to design and build the new site."
    },
    {
      "keywords": [
        "React-Native, Expo, Jest, Google Firebase"
      ],
      "description": "Participated in a team of 3 developers to create a web and mobile application with create/read/update/delete functionality for a course project. Stack included React front-end and NodeJs backend connecting to a document based database.",
      "name": "Badger Mental Health",
      "url": "https://github.com/alexgoldsmith/badgermentalhealth"
    },
    {
      "keywords": [
        ""
      ],
      "name": "Stack Overflow Survey Visualization",
      "description": "Created a web application for a course project using PyScript, JavaScript, and SQLite. The Web application allowed users to query a database, and subsequently displayed a visualization."
    }
  ],
  "awards": [
    {
      "title": "",
      "date": "",
      "awarder": "",
      "summary": ""
    }
  ],
  "sections": [
    "templates",
    "profile",
    "work",
    "education",
    "projects",
    "skills",
    "awards"
  ]
}


# parse json into a format easy for humans to read
def parse_resume() -> str:
    resume_str = ""
    resume_obj = RESUME_JSON
    resume_str += parse_profile(resume_obj)
    # resume_str += parse_work(resume_obj)
    # resume_str += parse_education(resume_obj)
    # resume_str += parse_projects(resume_obj)
    # resume_str += parse_skills(resume_obj)
    return resume_str

# parse profile
def parse_profile(resume_obj: dict) -> str:
    resume_str = ""
    resume_str += f"""{resume_obj['basics']['name']}
"""
    resume_str += f"""{resume_obj['basics']['location']['address']}
"""
    resume_str += f"""{resume_obj['basics']['email']}
"""
    resume_str += f"""{resume_obj['basics']['phone']}
"""
    resume_str += f"""{resume_obj['basics']['website']}
"""
    return resume_str


# parse work

# parse education

# parse projects

# parse skills



RESUME = parse_resume()
COMPANY_DESC="""stuff"""
ROLE_DESC="""stuff"""
DESIRED_CANDIDATE_DESCRIPTION = """stuff"""

QUESTION = """stuff"""


def compose_prompt(question: str) -> str:
    return f"""
Resume: "{RESUME}"
Company Description: "{COMPANY_DESC}"
Role Description: "{ROLE_DESC}"
Desired Candidate Description: "{DESIRED_CANDIDATE_DESCRIPTION}"

Question: "{question}"

Using the context provided above, we construct the best possible answer below:
""".strip()


async def answer(question: str = QUESTION
) -> str:
    prompt = compose_prompt(question)
    answer = await recipe.agent().complete(prompt=prompt, stop='"')
    return answer

print(parse_resume())


# recipe.main(answer)
