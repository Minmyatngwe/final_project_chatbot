# Final Project Chatbot

## How to Use
This chatbot uses the **Llama3** large language model, available via the **Ollama** platform. Follow these steps to set it up:

1. **Install Ollama**  
   Open a terminal and type the following command:  
   ```bash
   snap install ollama
Verify Installation
Once installed, type the following command:

bash
Copy code
ollama
If you see output from the command, it means Ollama was installed successfully.

Download Llama3
Pull the Llama3 model by running:

bash
Copy code
ollama pull llama3
Run the Chatbot
After completing the above steps, you can run the Python file to start the chatbot.

Language Detection
The chatbot uses a language detection library to identify the input language. However, short inputs like "hello" or "hi" might be misclassified as non-English, as these words exist in multiple languages.

Recommendation
To avoid misclassification, we recommend typing full sentences instead of single words or short phrases.

Response Time
The response time of the chatbot depends on the hardware of your computer. Since the Llama3 model has 8 billion parameters, the speed of the chatbot will vary based on your system's GPU and CPU performance.

Limitations
English Only
The chatbot only supports English input. With 8 billion parameters, the model is smaller compared to others like ChatGPT-4 (which has over 1.76 trillion parameters). For accurate results, inputs in other languages or numbers only will prompt the program to ask you to retype in English.

User Interface (UI)
The UI design might not be visually appealing as we are not software engineering students, but it is functional and user-friendly.

