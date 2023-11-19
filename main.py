from fastapi import FastAPI, File, UploadFile
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from docx import Document
import json
import os
import PyPDF2
import uuid
from datetime import datetime

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI
app = FastAPI()


# Retrieve the OpenAI API key
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize LANGCHAIN
langchain_llm = OpenAI(openai_api_key=OPEN_API_KEY)

# Define the answer template
answer_template_string = """
    Provide a detailed answer for the following question:
    {text}
    Include information such as page number, question number, and any additional context.
"""

# Define the answer prompt template
answer_prompt = PromptTemplate(
    template=answer_template_string,
    input_variables=['text'],
)

# Initialize the LangChain model chain
answer_chain = LLMChain(
    llm=langchain_llm,
    prompt=answer_prompt,
)

def read_questions_from_word(file_path):
    doc = Document(file_path)
    questions = [paragraph.text.strip() for paragraph in doc.paragraphs if paragraph.text.strip()]
    return questions

def read_questions_from_pdf(file_path):
    questions = []
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            questions.extend(page.extract_text().strip().split('\n'))
    return [question.strip() for question in questions if question.strip()]

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define endpoint to handle questions and documents
@app.post("/answer")
async def answer_questions(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = f"{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Determine file type and read questions
    if file.filename.endswith('.docx'):
        questions = read_questions_from_word(file_path)
    elif file.filename.endswith('.pdf'):
        questions = read_questions_from_pdf(file_path)
    else:
        return {"error": "Unsupported file format"}

    # Initialize LangChain context
    context = answer_chain

    # Iterate through questions and generate answers
    answers = []
    for index, question in enumerate(questions):
        answer = context(question, "")
        answer = {
            "content": question,
            "id":str(uuid.uuid4()), 
            "createdAt": datetime.now().time(),
            "modifiedAt": datetime.now().time(),
            "answer": answer["text"].replace("\n", ""),
            "questionNumber": index+1,
            "product": "Zania Assignment",
            "accessLevel": "private",
            "source": "questionnaire",
            "subtype": {"raw": ["Custom"], "pretty": ["Custom"]},
        }
        answers.append(answer)
        

    return answers

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
