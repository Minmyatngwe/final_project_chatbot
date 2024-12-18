from langchain_ollama import OllamaLLM
from langdetect import detect

model = OllamaLLM(model='llama3')

print("Chatbot initialized. Type 'bye' to exit.")

def check_language(user_input):
    greetings=['hello','hi']
    if detect(user_input)=='en' or any(i in user_input.lower() for i in greetings):
        return True
    else: return False

while True:
    user_input = input("You: ").strip()
    if check_language(user_input):
        if user_input.lower() == "bye":
            
            print("Chatbot: Goodbye!")

            break

        try:
            response_stream = model.stream(input=user_input)
            print("Chatbot:", end=" ", flush=True)

            
            for token in response_stream:
            
                print(token, end="", flush=True)  

            print() 
        except Exception as e:
            
            print(f"An error occurred: {e}")
    else:
        print("Only english")
        continue
