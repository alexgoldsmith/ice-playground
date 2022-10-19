import json

# load json from file src/job_qa/resume.json
def load_resume() -> dict:
    with open('src/job_qa/resume.json') as f:
        resume_json = json.load(f)
    return resume_json

# parse json into a format easy for humans to read
def parse_resume() -> str:
    resume_str = ""
    resume_obj = load_resume()
    resume_str += parse_profile(resume_obj)
    resume_str += parse_work(resume_obj)
    resume_str += parse_education(resume_obj)
    resume_str += parse_projects(resume_obj)
    resume_str += parse_skills(resume_obj)
    return resume_str

# parse profile
def parse_profile(resume_obj: dict) -> str:
    resume_str = """Personal information:

"""
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
def parse_work(resume_obj: dict) -> str:
    resume_str = """Work Experience:

"""
    for job in resume_obj['work']:
        resume_str += f"""{job['company']}
"""
        resume_str += f"""{job['position']}
"""
        resume_str += f"""{job['location']}
"""
        resume_str += f"""{job['startDate']} - {job['endDate']}
"""
        for highlight in job['highlights']:
            resume_str += f"""{highlight}
"""
        resume_str += f"""

"""
    return resume_str

# parse education
def parse_education(resume_obj: dict) -> str:
    resume_str = """Education:
    
"""
    for school in resume_obj['education']:
        resume_str += f"""{school['institution']}
"""
        resume_str += f"""{school['studyType']} - {school['area']}
"""
        resume_str += f"""{school['location']}
"""
        resume_str += f"""{school['startDate']} - {school['endDate']}
"""
#         resume_str += f"""{school['gpa']}
# """
        resume_str += f"""

"""
    return resume_str

# parse projects
def parse_projects(resume_obj: dict) -> str:
    resume_str = """Projects:
    
"""
    for project in resume_obj['projects']:
        resume_str += f"""{project['name']}
"""
        resume_str += f"""{project['description']}
"""
        for keyword in project['keywords']:
            resume_str += f"""{keyword}
"""
        resume_str += f"""

"""
    return resume_str

# parse skills
def parse_skills(resume_obj: dict) -> str:
    resume_str = """Skills:

"""
    for skill in resume_obj['skills']:
        resume_str += f"""{skill['name']}
"""
        for keyword in skill['keywords']:
            resume_str += f"""{keyword}
"""
        resume_str += f"""
"""
    return resume_str