import requests, json, pprint



def write_blog():
  url = "http://localhost:11434/api/generate"

  headers = {
      "Content-Type": "application/json"
  }



  file = json.loads("topics.json", "r")
  for line in file:
    line = line.strip()
    original_line = line
    line = (f"You are an expert tech blog writer, pleast write a guide for {line} in markdown format.")
    data = {
        "model": "mistral",
        "prompt": line,
        "context": []
    }
    print(line)
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = response.text
        pprint.pprint(data)
        #print(content)
    else:
        print("An error occurred.")





write_blog()