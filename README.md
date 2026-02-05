# MCQ Generation App Using Pdf

This project is an automated Multiple Choice Question (MCQ) generator that uses Large Language Models (LLMs) via LangChain and OpenRouter. It extracts text from PDF documents and generates questions based on specified difficulty levels.

## 🚀 Features

- **PDF Text Extraction**: Seamlessly extracts content from PDF files.
- **AI-Powered MCQ Generation**: Uses advanced LLMs (like Qwen via OpenRouter) to create relevant questions.
- **Customizable Difficulty**: Generate questions at various difficulty levels (Easy, Medium, Hard).
- **Streamlit Interface**: User-friendly web interface for interaction (if applicable) or notebook-based experimentation.
- **Local Package Support**: Includes `setup.py` for easy installation of the project as a local package.

## 🛠️ Tech Stack

- **Core**: Python
- **LLM Orchestration**: LangChain
- **LLM Provider**: OpenRouter (OpenAI compatible API)
- **UI (Optional)**: Streamlit
- **PDF Processing**: PyPDF2
- **Environment Management**: `python-dotenv`

## 📋 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd mcqgen
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/Scripts/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install as a local package**:
   ```bash
   pip install -e .
   ```

## ⚙️ Configuration

Create a `.env` file in the root directory and add your OpenRouter API key:

```env
OPENROUTERAI_API_KEY=your_openrouter_api_key_here
```

## 📖 Usage

### Experimentation via Jupyter Notebook
You can explore the core logic in the `experiment/mcq.ipynb` notebook. It demonstrates how to load the PDF, extract text, and invoke the LLM to generate MCQs.

### Running with Streamlit
*(If you have a streamlit app entry point, e.g., app.py)*
```bash
streamlit run app.py
```

## 📂 Project Structure

```text
mcqgen/
├── examplePdf/         # Sample PDF files for testing
├── experiment/         # Jupyter notebooks for testing and development
├── src/                # Source code
│   └── mcqgen/         # Core package logic
├── .env                # API keys and environment variables
├── requirements.txt    # Project dependencies
├── setup.py            # Package installation script
└── README.md           # Project documentation
```

## ⚖️ License

[MIT License](LICENSE) (or your preferred license)
