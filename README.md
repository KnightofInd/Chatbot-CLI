# 🤖 Local Command-Line Chatbot using Hugging Face

A lightweight, terminal-based chatbot powered by Hugging Face Transformers. This chatbot simulates realistic multi-turn conversations using short-term memory and runs entirely **offline** after the model is downloaded once. Built with modular, clean Python code — perfect for demos and developer-level interaction.

---

## 🚀 Features

- 💬 Conversational AI using `microsoft/DialoGPT-small`
- 🧠 Maintains memory of the last 5 exchanges (sliding window)
- 🖥️ CLI interface for fast and local user interaction
- 🧩 Clean modular code structure (`model_loader.py`, `chat_memory.py`, `interface.py`)
- ⚙️ Fully local execution (no need for GPU or cloud)

---

DEMO VIDEO LINK ------> https://drive.google.com/file/d/1iEHIgIHnb_DMGrytEJTwfWwFEjNjYQ3l/view?usp=sharing


## 🧱 Project Structure

```bash
Chatbot-CLI/
│
├── model_loader.py      # Loads the model and tokenizer from Hugging Face
├── chat_memory.py       # Manages short-term memory for conversations
├── interface.py         # Command-line loop that runs the chatbot
├── README.md            # You're reading it!
├── .gitignore           # Excludes large model and cache files
└── venv/                # Local virtual environment (not tracked by git)


🛠️ Setup Instructions
🔹 1. Clone the repository

git clone https://github.com/yourusername/Chatbot-CLI.git
cd Chatbot-CLI
🔹 2. Create and activate virtual environment
bash

python -m venv venv

# Activate:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
🔹 3. Install dependencies
pip install transformers torch


▶️ Run the Chatbot

python interface.py


📦 Requirements
Python 3.7 or higher

transformers (by Hugging Face)

torch (PyTorch backend)

👨‍💻 Tech Stack
🧠 Model: microsoft/DialoGPT-small

🐍 Language: Python 3

📦 Libraries: transformers, torch, collections

🙌 Acknowledgements
Model: DialoGPT by Microsoft

Task: Machine Learning Internship Assignment – Local CLI Chatbot

📬 Contact
🔗 linkedin.com/in/rohanstech
📧 knightofind@gmail.com
   github.com/KnightofInd