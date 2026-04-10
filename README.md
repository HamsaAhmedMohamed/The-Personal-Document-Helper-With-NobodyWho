# 📚 Personal Document Helper (with NobodyWho)

This project is a simple demo that turns a PDF textbook into a format
readable by an encoder-based system, enabling you to query its contents
using natural language.

## 🚀 Features

-   📄 Load and process a PDF textbook\
-   🔍 Ask questions about the content\
-   🤖 Get context-aware answers based on the document\
-   🧠 Uses a local LLM via NobodyWho

## 🧩 How It Works

1.  The PDF is parsed and converted into a machine-readable format.\
2.  The processed text is embedded using an encoder.\
3.  When you ask a question, the system retrieves relevant parts of the
    document.\
4.  A local language model generates an answer based on the retrieved
    context.

⚠️ **Important:**\
When asking questions, phrase them clearly, for example:\
"What does the textbook say about \[your topic\]?"

This ensures the model grounds its answer in the document.

## 🛠️ Setup

### 1. Install dependencies

pip install pymupdf nobodywho

### 2. Download a compatible model

You need a GGUF-format model compatible with NobodyWho, such as:

Qwen_Qwen3-0.6B-Q4_K_M.gguf

You can also use other compatible models if preferred.

### 3. Configure model path

Make sure your code points to the correct local path of your downloaded
LLM.

Example:

model_path = "path/to/your/model.gguf"

## ▶️ Usage

1.  Place your PDF textbook in the project directory\
2.  Run the script\
3.  Ask questions about the document

Example:

chat.ask("What does the textbook say about neural networks?")



## 📄 License

Public use.
