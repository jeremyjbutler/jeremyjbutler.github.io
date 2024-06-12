from langchain_community.llms import Ollama
ollama = Ollama(
    base_url='http://localhost:11434',
    model="mistral"
)
print(ollama.invoke("why is the sky blue"))

file = open("topics.txt", "r")
for line in file:
    line = line.strip()
    original_line = line
    line = (f"You are an expert tech blog writer, pleast write a guide for {line} in markdown format.")
    print(line)
    callit=ollama.invoke(line)
    filesave="content/pages/" + original_line.replace(" ", "") + ".md"
    with open(filesave, "w") as f:
      f.write("# Chat Responses\n\n")
      for message in callit:
        f.write("## Input:\n")
        f.write("- " + callit + "\n\n")
        # Add a sleep to avoid rate limiting
        
