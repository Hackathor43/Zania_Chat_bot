# Zania_Chat_bot
# FastAPI Question Answering API

This is a FastAPI application that utilizes OpenAI's language model to answer questions from documents. The application supports both Word (.docx) and PDF file formats.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Hackathor43/Zania_Chat_bot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Zania_Chat_bot
    ```

3. Install the required dependencies:

    ```bash
    pip install "required modules"
    ```

### Usage

1. Set up your OpenAI API key by creating a `.env` file with the following content:

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

    Replace `your_openai_api_key_here` with your actual OpenAI API key.

2. Run the FastAPI application:

    ```bash
     python -m uvicorn main:app --reload
    ```

    The application will be accessible at `http://127.0.0.1:8000`.

3. Open your web browser and navigate to the Swagger documentation to test the API:

    ```
    http://127.0.0.1:8000/docs
    ```

    You can also use tools like [curl](https://curl.se/) or [Postman](https://www.postman.com/) to interact with the API.

## Features

- Supports Word (.docx) and PDF file formats.
- Generates answers to questions from the provided documents.
- Uses OpenAI's language model for natural language processing.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI](https://beta.openai.com/)
- [python-docx](https://python-docx.readthedocs.io/)
- [PyPDF2](https://pythonhosted.org/PyPDF2/)

