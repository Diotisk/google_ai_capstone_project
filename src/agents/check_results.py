from google.adk.agents import Agent
from google.adk.models import Gemini

from src.tools.read_cv import load_cv
from src import config

retry_config=config.RETRY_CONFIG

check_results_model = Gemini(
    model="gemini-2.5-flash",
    retry_options=retry_config
)

check_results_agent = Agent(
    name="check_results",
    model=check_results_model,
    description="An agent that checks if positions found by job_search agent are relevant to the CV and location provided in the user query.",
    instruction="""You are a senior professional recruiter. Using the provided variable 'jobs', check if they are relevant to the provided CV and user query.
    1. Check, if input variable 'jobs' contains jobs with description and location.
    2. If 'jobs' is not empty, extract concrete location or remote working option from the user's query.
    3. From the user's request extract the full path to the CV, use 'load_cv' method to find the file and extract its content.
    4. Check if positions from 'jobs' are relevant for the provided CV and location from the user's query.
    5. Update bullet points list stored in variable 'jobs' by adding to each point a new parameter: relevance score from 0 to 10 where 0 means not relevant and 10 is a perfect match.
    6. Return updated bullet points list.
    """,
    tools=[load_cv]
)
