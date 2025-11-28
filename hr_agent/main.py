import os
import asyncio
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner

from hr_agent.agent import root_agent


async def main():
    load_dotenv()
    cv_file_path = os.getenv('CV_FILE_PATH')
    preferred_location = os.getenv('PREFERRED_LOCATION')
    runner = InMemoryRunner(agent=root_agent, app_name="agents")
    response = await runner.run_debug(
        f"Find jobs for {cv_file_path} in {preferred_location}."
    )
    print(response)

if __name__ == "__main__":
  asyncio.run(main())
