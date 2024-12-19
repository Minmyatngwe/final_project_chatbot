import tkinter as tk
from langchain_ollama import OllamaLLM
from langdetect import detect

model = OllamaLLM(model='llama3')

def stream_response(user_input):
    try:
        response_stream = model.stream(input=user_input)
        chat_display.insert(tk.END, "Chatbot: ")
        chat_display.see(tk.END)
        for token in response_stream:
            chat_display.insert(tk.END, token) 
            chat_display.update_idletasks()  
        chat_display.insert(tk.END, "\n\n")  
        chat_display.see(tk.END)
        chat_display.insert(tk.END,"You :")
    except Exception as e:
        chat_display.insert(tk.END, f"Chatbot: Error: {e}\n\n")
        chat_display.see(tk.END)

def send_message():
    common_word=['hi','hello','Thanks']
    user_input = user_input_entry.get("1.0", "end-1c").strip()

    user_input_entry.delete("1.0", "end") 

    if not user_input:
        chat_display.insert(tk.END, "You: (Empty message)\nChatbot: Please enter a message.\n\n")
        return

    if detect(user_input) != 'en' and not (any(word.lower() in common_word for word in common_word)):
        chat_display.insert(tk.END, f" {user_input}\nChatbot: Only English text is supported.\n\n")
        return

    chat_display.insert(tk.END, f"You: {user_input}\n")
    chat_display.see(tk.END)  

    root.after(100, lambda: stream_response(user_input))

root = tk.Tk()
root.title("Chatbot")
root.geometry("1500x1500")
root.resizable(False, False)

chat_display = tk.Text(root, font=("Arial", 12), wrap=tk.WORD)
chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

user_input_frame = tk.Frame(root)
user_input_frame.pack(fill=tk.X, padx=10, pady=5)

user_input_entry = tk.Text(user_input_frame, font=("Arial", 18), height=5, bd=5, relief=tk.GROOVE, wrap=tk.WORD)
user_input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button = tk.Button(user_input_frame, text="Send", command=send_message,height=5)
send_button.pack(side=tk.RIGHT, padx=6)

root.mainloop()
