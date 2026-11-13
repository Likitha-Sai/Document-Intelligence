
# Document Intelligence

An AI-powered application that allows users to upload PDF documents and ask questions in natural language. The application extracts text from PDF files and uses the Groq API to generate context-aware answers.

## Features

- Upload PDF documents.
- Extract text from PDF files using PyPDF.
- Ask questions about the uploaded document.
- Generate AI-powered answers using the Groq API.
- Simple and interactive interface built with Streamlit.

## Tech Stack

- Python
- Streamlit
- PyPDF
- Groq API

## Project Structure

    Document-Intelligence/
    │
    ├── app.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd Document-Intelligence
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your Groq API key as an environment variable named `GROQ_API_KEY`.

5. Run the application:

   ```bash
   streamlit run app.py
   ```

## How It Works

1. User uploads a PDF document.
2. The application extracts text using PyPDF.
3. User enters a question related to the document.
4. The extracted content and question are sent to the Groq API.
5. The AI generates and displays an answer.

## Future Improvements

- Support for multiple PDF documents.
- Improved document processing for large PDFs.
- Conversation history.
- Docker-based deployment.
- Cloud deployment.

## Author

Developed as a Python and Generative AI project.

