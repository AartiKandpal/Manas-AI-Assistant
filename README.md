# 🧠 Manas AI Assistant

A modern AI-powered desktop voice assistant built with Python. Manas supports natural conversations, voice input/output, memory, tool execution, and local LLMs through Ollama.

---

## ✨ Features

- 🎙️ Voice Input (Speech-to-Text)
- 🔊 Natural Text-to-Speech
- 🤖 Local AI using Ollama
- 🧠 Persistent Memory
- 💬 Chat Interface
- ⚡ Wake Word Support
- 🛠️ Built-in Tools
- 📂 File Operations
- 🌐 Browser Automation
- 🎨 Modern Desktop GUI

---

## 📂 Project Structure

```
Manas-AI-Assistant/
│
├── src/
│   ├── agent/
│   ├── ai/
│   ├── assistant/
│   ├── audio/
│   ├── config/
│   ├── conversation/
│   ├── core/
│   ├── gui/
│   ├── memory/
│   ├── models/
│   ├── tools/
│   └── utils/
│
├── requirements.txt
├── .gitignore
└── README.md
```


---


# 🤖 Agent Architecture

The Manas AI Assistant follows a modular, agent-oriented architecture where each component has a dedicated responsibility. Instead of directly generating responses, the assistant first understands the user's intent, plans an execution strategy, invokes tools when necessary, retrieves memory, and finally generates a natural response.

```text
                        ┌─────────────────────┐
                        │      User Input     │
                        │ (Voice / Text GUI)  │
                        └──────────┬──────────┘
                                   │
                                   ▼
                     ┌────────────────────────┐
                     │ Conversation Manager   │
                     └──────────┬─────────────┘
                                │
                                ▼
                     ┌────────────────────────┐
                     │        Planner         │
                     │ Intent Understanding   │
                     └──────────┬─────────────┘
                                │
                                ▼
                     ┌────────────────────────┐
                     │    Command Router      │
                     └───────┬─────────┬──────┘
                             │         │
                  Tool Needed?│         │Direct LLM Response
                             │         │
                  Yes         │         ▼
                             ▼   ┌──────────────┐
                  ┌─────────────────────────────┐
                  │       Tool Manager          │
                  └───────┬─────────┬───────────┘
                          │         │
          ┌───────────────┘         └────────────────┐
          ▼                                          ▼
 ┌────────────────┐                        ┌─────────────────┐
 │ Browser Tools  │                        │ Memory Manager  │
 └────────────────┘                        └─────────────────┘
          │                                          │
          └──────────────────┬───────────────────────┘
                             ▼
                  ┌────────────────────────┐
                  │      LLM Engine        │
                  │ (Ollama / Local Model) │
                  └──────────┬─────────────┘
                             │
                             ▼
                  ┌────────────────────────┐
                  │      Final Response    │
                  └──────────┬─────────────┘
                             │
                             ▼
                  ┌────────────────────────┐
                  │ Text-to-Speech Engine  │
                  └──────────┬─────────────┘
                             │
                             ▼
                         🔊 Speaker
```


---

### Components

- **Conversation Manager** – Maintains conversation state and manages the interaction lifecycle.
- **Planner** – Analyzes user requests and determines the execution strategy.
- **Command Router** – Decides whether the request requires direct LLM reasoning or external tool execution.
- **Tool Manager** – Executes registered tools such as browser, file, memory, or system utilities.
- **Memory Manager** – Stores and retrieves conversational context for more coherent responses.
- **LLM Engine** – Generates context-aware responses using a local Ollama model.
- **Text-to-Speech Engine** – Converts the final response into natural speech for voice interaction.

This modular architecture allows Manas AI Assistant to remain scalable, maintainable, and easily extensible by adding new tools or capabilities without modifying the core agent workflow.


---


## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/AartiKandpal/Manas-AI-Assistant.git
```

Move into the project

```bash
cd Manas-AI-Assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python src/main.py
```

or

```bash
python src/gui_main.py
```

---

## 🛠 Technologies Used

- Python 3
- Ollama
- PyQt
- Speech Recognition
- Text-to-Speech
- SQLite
- PyAudio

---

## 🎯 Roadmap

- [x] Voice Assistant
- [x] Desktop GUI
- [x] Memory System
- [x] Tool Calling
- [x] Local LLM Integration

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 👩‍💻 Author

**Aarti Kandpal**

GitHub: https://github.com/AartiKandpal

---

⭐ If you like this project, consider giving it a star!
