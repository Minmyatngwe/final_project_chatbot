import tkinter as tk
from langchain_ollama import OllamaLLM
from langdetect import detect

model = OllamaLLM(model='llama3')

def update_chat_display(message, tag=None):
    chat_display.config(state=tk.NORMAL) 
    chat_display.insert(tk.END, message, tag) 
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

def stream_response(user_input):
    try:
        response_stream = model.stream(input=user_input)
        update_chat_display("Chatbot: ", "bold")
        for token in response_stream:
            update_chat_display(token)
        update_chat_display("\n\n")
    except Exception as e:
        update_chat_display(f"Chatbot: Error: {e}\n\n")

def send_message():
    user_input = user_input_entry.get("1.0", "end-1c").strip() 
    user_input_entry.delete("1.0", "end")

    if not user_input:
        update_chat_display("You: (Empty message)\n", "user")
        update_chat_display("Chatbot: Please enter a message.\n\n")
        return

    if detect(user_input) != 'en':
        update_chat_display(f"You: {user_input}\n", "user")
        update_chat_display("Chatbot: Only English text is supported.\n\n")
        return

    update_chat_display(f"You: {user_input}\n", "user")
    root.after(100, lambda: stream_response(user_input))

def exit_app(event=None):
    root.destroy()

root = tk.Tk()
root.title("Chatbot")
root.geometry("600x700")
root.resizable(False, False)

chat_display = tk.Text(root, font=("Arial", 12), wrap=tk.WORD, state=tk.DISABLED)
chat_display.tag_config("bold", font=("Arial", 12, "bold"))
chat_display.tag_config("user", foreground="blue")
chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

user_input_frame = tk.Frame(root)
user_input_frame.pack(fill=tk.X, padx=10, pady=5)

user_input_entry = tk.Text(user_input_frame, font=("Arial", 14), height=3, wrap=tk.WORD)
user_input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

send_button = tk.Button(button_frame, text="Send", font=("Arial", 12), command=send_message, width=10)
send_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, font=("Arial", 12), command=exit_app, width=10)
exit_button.pack(side=tk.RIGHT, padx=5)

def on_hover(event):
    exit_button.config(text="Exit", bg="red", fg="white")

def on_leave(event):
    exit_button.config(text="", bg="SystemButtonFace", fg="black")

exit_button.bind("<Enter>") 
exit_button.bind("<Leave>")
root.mainloop()





