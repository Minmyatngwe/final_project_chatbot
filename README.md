# final_project_chatbot

## How to use?
Since TO USE OPEAN AI API ,there is limitation we use ollama large languare model,which is **llama3**

To use this chatbot we first need to download the llama3 llm
To download we first need to have ollma 
On the terminal type 

```bash

**snap install ollama**
```

After downloading **Type 
```bash
'ollama'
```
command on terminal you can see some output that means you successfully downloaded**
Next,we need to pull the largelanguage model that we are gonna use which is 'llama3'
To get that llama3 type this command 
```bash
**ollama pull llama3**
```

**After that you can run the python file**
## language detect

Since sometime languadetect libray thinks some common word like hello,hi bye not english because other languaes also has that kind of words.
### Recommendation
Our Recommendation is that instead of inputing or typing only one or two words ,type full sentences to avoid that

## Prompting Time
Since the model we are using has 8 billion parametors,the prompt time from the chat bot will be different based on the GPU AND CUP that your computer has.
## Warning
The chatbot only accepcts English since it has only 8 billion parameters which is kind of small large language model compared to chatgpt4 or other which has over 1.76 trillion parameters
so to get the accurate prompting we limite that.If you type other language or number only the programm will ask you to type again.
## weakness
While making UI is the hardest part for us ,sinnce we are not software engineering student.so it might not look that good but it is user friendly .

