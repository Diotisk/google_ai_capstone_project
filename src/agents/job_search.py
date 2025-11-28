from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import google_search

from src import config

retry_config=config.RETRY_CONFIG

job_search_model = Gemini(
    model="gemini-2.5-flash",
    retry_options=retry_config
)

job_search_agent = Agent(
    name="job_search",
    model=job_search_model,
    description="An agent that searches for five relevant job openings based on the bullet points list in variable 'roles'.",
    instruction="""You are a professional recruiter. Using the provided list, craft 2–5 focused search queries combining roles and domain keywords.
    1. Input variable 'roles' MUST contain a list of roles, relevant skills and seniority levels for each role.
    2. If 'roles' is not empty, extract concrete location or remote working option from the user query.
    3. You MUST call 'google_search' tool to conduct a search for relevant open positions in the extracted location or remote.
    4. Select 5 most relevant positions found.
    5. Summarize the output as a bullet points list where for each position MUST be named:
    - title
    - company
    - location
    - published date
    - summarized job description
    - url
    6. Return only final list stored in variable 'jobs'.
        """,
    output_key="jobs",
    tools=[google_search]
)
