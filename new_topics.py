import json

def generate_topic():
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The LA Dodgers won in 2020."},
    {"role": "user", "content": "Where was it played?"}
    ]

# Dump it somewhere
  with open('topics.json', 'w') as fh: 
      json.dump(messages, fh)
      
      
