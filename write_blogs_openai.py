import openai
import time
import json

client = openai.OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

# Function to send a message to OpenAI and return the response
def send_message(message):
    response = client.chat.completions.create(
        model="mistral",
        messages=json.dumps({"role": "user", "content": m}),
        stream=False,
    )
     print(response)
    return response.choices[0].text.strip()

# Read chat messages from the text file
def read_chat_messages(file_path):
    with open(file_path, "r") as file:
        return json.load(file)
        #return file.readlines()

# File path for the text file containing chat messages
file_path = "topics.json"

# Read chat messages from the file
chat_messages = read_chat_messages(file_path)
print(chat_messages)


# Iterate through the chat messages, send each message to OpenAI, and save the responses to a Markdown file
with open("chat_responses.md", "w") as f:
    f.write("# Chat Responses\n\n")
    for message in chat_messages:
        response = send_message(message)
        f.write("## Input:\n")
        f.write("- " + message.strip() + "\n\n")
        f.write("## Response:\n")
        f.write("- " + response + "\n\n")
        # Add a sleep to avoid rate limiting
        time.sleep(2)

print("Chat responses saved to chat_responses.md")