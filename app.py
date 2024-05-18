import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileReadTool, MDXSearchTool
from utils import get_openai_api_key, get_serper_api_key
import openai

# Load environment variables
load_dotenv()

openai_api_key = get_openai_api_key()
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4'  # Use GPT-4o model
os.environ["SERPER_API_KEY"] = get_serper_api_key()

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_resume = FileReadTool(file_path='./fake_resume.md')
semantic_search_resume = MDXSearchTool(mdx='./fake_resume.md')

# Import agents and tasks
from agents import researcher, profiler, resume_strategist, interview_preparer
from tasks import research_task, profile_task, resume_strategy_task, interview_preparation_task

# Create the crew
job_application_crew = Crew(
    agents=[researcher, profiler, resume_strategist, interview_preparer],
    tasks=[research_task, profile_task, resume_strategy_task, interview_preparation_task],
    verbose=True
)

# Set the inputs for the execution of the crew
job_application_inputs = {
    'job_posting_url': 'https://www.webber.lt/karjera/',
    'github_url': 'https://github.com/joaomdmoura',
    'personal_writeup': """Noah is an accomplished Software
    Engineering Leader with 18 years of experience, specializing in
    managing remote and in-office teams, and expert in multiple
    programming languages and frameworks. He holds an MBA and a strong
    background in AI and data science. Noah has successfully led
    major tech initiatives and startups, proving his ability to drive
    innovation and growth in the tech industry. Ideal for leadership
    roles that require a strategic and innovative approach."""
}

# Execute the crew tasks
result = job_application_crew.kickoff(inputs=job_application_inputs)

# # Print the output of each task for debugging
# print("Research Task Output:")
# print(result[0]['output'])

# print("Profile Task Output:")
# print(result[1]['output'])

# print("Resume Strategy Task Output:")
# print(result[2]['output'])

# print("Interview Preparation Task Output:")
# print(result[3]['output'])

# Write the complete output to the file
# with open('tailored_resume.md', 'w') as file:
#     file.write(result[2]['output'])

# with open('interview_materials.md', 'w') as file:
#     file.write(result[3]['output'])

# Display the generated tailored_resume.md file
from IPython.display import Markdown, display
display(Markdown("./tailored_resume.md"))

# Display the generated interview_materials.md file
display(Markdown("./interview_materials.md"))
