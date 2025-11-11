#Utility functions to get information on job out of the description

def extract_company(desc: str) -> str:
    job: str = desc
    return job

def extract_location(desc: str) -> str:
    location: str = desc
    return location

def extract_date_posted(desc: str) -> str:
    date: str = desc
    return date

def extract_requirements(desc: str) -> list[str]:
    reqs: list[str] = []
    return reqs

def extract_salary(desc: str) -> int:
    salary: int = 0
    return salary