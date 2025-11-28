from google.adk.agents import LlmAgent
from google.adk.models import Gemini

from src.tools.read_cv import load_cv
from src import config

retry_config=config.RETRY_CONFIG

summarize_model = Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    )

analyze_agent = LlmAgent(
    name="cv_analyst",
    model=summarize_model,
    description="A simple agent that can summarize a CV.",
    instruction="""You are a professional recruiter. You should analyze a provided CV after extracting its content.
    
    1. You get a request to find relevant jobs for specific CV. CV is provided as a full path to the pdf file in users query.
    2. Extract the path and use 'load_cv' method to find the file and extract its content.
    3. Review the extracted content for these points:
        - identify potential job roles and career paths that match the candidate’s skills, experience and expertise
        - suggest both traditional roles within their background and alternative opportunities where their expertise is applicable
        - indicate the seniority level (entry, mid, senior)
        - list the most relevant keywords and skills from the CV that can help align with job descriptions
    4. Summarize the output in bullet points, where each point MUST contain role name, relevant skills from the CV, seniority level.
    5. Return ONLY final bullet points list stored in variable 'roles'.
        """,
    output_key="roles",
    tools=[load_cv]
)
