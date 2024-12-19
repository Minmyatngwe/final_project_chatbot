import tkinter as tk
from langchain_ollama import OllamaLLM
from langdetect import detect

model = OllamaLLM(model='llama3')

def send_message():
    user_input = user_input_entry.get().strip()
    user_input_entry.delete(0, tk.END)

    if not user_input:
        chat_display.insert(tk.END, "You: (Empty message)\nChatbot: Please enter a message.\n\n")
        return

    if detect(user_input) != 'en':
        chat_display.insert(tk.END, f"You: {user_input}\nChatbot: Only English text is supported.\n\n")
        return

    chat_display.insert(tk.END, f"You: {user_input}\n")

    try:
        response_stream = model.stream(input=user_input)
        chatbot_response = "".join(response_stream)
        chat_display.insert(tk.END, f"Chatbot: {chatbot_response}\n\n")
    except Exception as e:
        chat_display.insert(tk.END, f"Chatbot: Error: {e}\n\n")

root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")

chat_display = tk.Text(root, font=("Arial", 12), wrap=tk.WORD)
chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

user_input_frame = tk.Frame(root)
user_input_frame.pack(fill=tk.X, padx=10, pady=5)

user_input_entry = tk.Entry(user_input_frame, font=("Arial", 14))
user_input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button = tk.Button(user_input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()

