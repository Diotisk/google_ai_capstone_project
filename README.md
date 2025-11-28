# Job Search Agent

This project automates search for relevant job openings based on a given CV.

## File Structure

- `agent.py` -- Logic of the root agent that orchestrates the whole system.
- `main.py` -- Code to run the root agent.
- `analyze_agent.py` -- An agent that comes up with relevant job titles working off
- of a provided CV. It uses a custom 'read_cv' tool to extract its contents.
- `job_search.py` -- An agent to search for relevant positions based on
the output of the analyze_agent.
- `check_results.py` -- An agent to evaluate the output of the job_search agent.

## Getting Started

1. Clone the repository to your local machine. 
2. Ensure you have Python 3.10+ and all dependencies installed. Dependencies
are listed in requirements.txt and can be installed with ```pip install -r requirements.txt```.
3. Create a .env file in the root directory of your project and add following environment
variables:
* GOOGLE_API_KEY="..." //set up here https://aistudio.google.com/app/api-keys
* GOOGLE_GENAI_USE_VERTEXAI=FALSE 
* CV_FILE_PATH="..." // full path to the CV file in pdf format
* PREFERRED_LOCATION="..." // location for job search
5. Run the script using Google ADK Web UI with ```adk web --port 8000```
and selecting hr_agent in the web interface. In this case provide the path to the CV file
and desired location in the chat with the LLM.
6. Alternatively, you can run the main.py file. In this case the query will be conducted
based on the data in .env file.

This project was created as part of 11/2025 Google Agents Intensive.
