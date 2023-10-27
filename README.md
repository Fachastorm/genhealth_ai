# GenHealth Proxy API

GenHealth Proxy API is a Python-based FastAPI application that serves as a proxy to forward requests to the GenHealth inference API.

## Installation

Ensure you have Python installed on your system. Then, clone the repository and navigate to the project directory.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary dependencies.

```bash
pip install -r requirements.txt 
```

## Usage

Set the environment variables. If you're using a Unix-based system (like macOS or Linux):

```
source .env

# For Windows:
set /p GENHEALTH_API_KEY=<.env

# Start the FastAPI server:
uvicorn app.main:app --reload

# Access the API documentation at:
http://127.0.0.1:8000/docs
```

Use the endpoints /v1/predict and /v1/embeddings as per the provided documentation.

## Testing

To run the tests, navigate to the root directory of the project and execute:

```
pytest app/tests/
```

Please make sure to update tests as appropriate.