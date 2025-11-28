# Capstone project Google IA Agents

This project contains an AI agent workflow which aims to analyze provided CV and search
for most relevant open positions.

## File Structure

- `agent.py` --- File containing root agent that orchestrates all other agents.
- `main.py` --- File containing code to run the root agent.
- `analyze_agent.py` --- File containing agent which extracts the CV from the provided path
and makes a summary of relevant job positions. It is using a custom tool 'read_cv' to extract
its content.
- `job_search.py` --- File containing agent to search for relevant positions based on
the output of analyze_agent.
- `check_results.py` --- File containing agent to evaluate the result of job_search agent.

## Getting Started

1. Clone the repository to your local machine. 
2. Ensure you have Python 3.10+ and all required dependencies are installed. Dependencies
are listed in requirements.txt.
3. Create a .env file in root directory of your project and add following environment
variables:
--- GOOGLE_API_KEY="..." //set up here https://aistudio.google.com/app/api-keys
--- GOOGLE_GENAI_USE_VERTEXAI=FALSE 
--- CV_FILE_PATH="..." // full path to the CV file in pdf format
--- PREFERRED_LOCATION="..." // location for job search
4. Run the script using Google ADK Web UI with the following command 'adk web --port 8000'
and selecting hr_agent in the web interface. In this case provide the path to the CV file
and desired location in the chat with the LLM.
5. Alternatively you can run the main.py file. In this case the query will be conducted
based on the data in .env file.
