from strands import Agent
from strands.models import BedrockModel

from strands_tools import file_read, file_write, speak

# Step 1: Define the model
model_id = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    max_tokens=64000,
    additional_request_fields={
        "thinking": {
            "type":"disabled",
        }
    },
)

# Step 2: Define the system prompt
system_prompt = """
You are a helpful personal assistant capable of performing local file actions and simple tasks for the user.

Your key capabilities:
1. Read, understand, and summarize files.
2. Create and write to files.
3. List directory contents and provide information on the files.
4. Summarize text content

You can use the following tools to perform these actions:
- file_read: Read a file and return the content.
- file_write: Write to a file.
- file_list: List the contents of a directory.
- 'speak': Speak a message to the user.
"""

# Step 3: Define the agent
agent = Agent(
    model=model_id,
    system_prompt=system_prompt,
    tools=[
        file_read,
        file_write,
        speak,
    ],
)

# Step 4: Run the agent
agent("What is the content of the file 'chapter10.txt' located in the 'docs' directory and summarize it in less than 100 words? \
    And save the file in Markdown format in the 'results' directory, \
    If the folder 'results' does not exist, create it. \
    If the file 'chapter10.md' already exists, overwrite it. \
    And finally also speak out the summary you have created. Make sure the voice is very natural and not robotic.")
