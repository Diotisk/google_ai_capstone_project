from google.adk.runners import Runner
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.tools import agent_tool

from src.agents.analyze_agent import analyze_agent
from src.agents.check_results import check_results_agent
from src.agents.job_search import job_search_agent
from src.tools.store_session_data import save_userinfo, retrieve_userinfo

root_agent = Agent(
    name="RootAgent",
    model="gemini-2.5-flash",
    description="Root Agent",
    instruction="""You are an orchestrator.
                1. Extract path to CV and location from user query with save_userinfo tool.
                2. Invoke cv_analyst tool with user query as input. Get response from cv_analyst stored in variable 'roles'.
                3. Retrieve 'user:location' with retrieve_userinfo tool.
                4. Invoke job_search tool with variable 'roles' and variable 'user:location'.
                5. Get response from job_search tool stored in variable 'jobs'.
                6. Retrieve 'user:path' and 'user:location' with retrieve_userinfo tool.
                7. Invoke check_results tool with following input:
                - variable 'jobs' from job_search tool,
                - variable 'user:path',
                - variable 'user:location'.
                8. Return the response of check_results tool.""",
    tools=[agent_tool.AgentTool(agent=analyze_agent), agent_tool.AgentTool(agent=job_search_agent),
           agent_tool.AgentTool(agent=check_results_agent), save_userinfo, retrieve_userinfo]
)

session_service = InMemorySessionService()
runner = Runner(agent=root_agent, session_service=session_service, app_name="default")