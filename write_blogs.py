import json
import requests
import pickle

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = 'mistral' # TODO: update this for whatever model you wish to use

def generate(prompt, context):
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=False)
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        # the response streams one token at a time, print that as we receive it

        print(response_part, end='', flush=True)


        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):

            return body['context']
    


def main():
    file = open("topics.json", "r")
    for line in file:
        line = line.strip()
        original_line = line
        line = (f"You are an expert tech blog writer, pleast write a guide for {line} in markdown format.")
        print(line)
        context = [] # the context stores a conversation history, you can use this to make the model more context aware
        savefile = "content/pages/" + original_line.replace(" ", "") + ".md"
        user_input = line
        if not user_input:
          exit()
        print()
        with open("tmp/pickle-build/context.json", "a") as f:
            
            context = generate(user_input, context)
            print(context, file=f)
        #with open("tmp/pickle-build/context.json", "a") as f:
              #json.dump(context, f)
        
        with open(savefile, "w") as f:
          with open("tmp/pickle-build/context.json", "r") as p:
              loaded_list = json.load(p)
              f.write('# Title: ' + original_line + '\n')
              for item in loaded_list:
                f.write('{} '.format(item))
                #f.write(item)
                f.write('\n')
                print(item)
          f.write('\n')
       
        print()
        
    file.close()
    
   # context = [] # the context stores a conversation history, you can use this to make the model more context aware
   # while True:
   #     user_input = input("Enter a prompt: ")
   #     if not user_input:
   #         exit()
   #     print()
  #      context = generate(user_input, context)
   #     print()

if __name__ == "__main__":
    main()