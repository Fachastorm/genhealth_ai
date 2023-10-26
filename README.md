Testing the API

To ensure the functionality of the proxy API, we've included a set of unit tests. Follow the steps below to run the tests:
Prerequisites:

    Ensure you have Python installed. You can check by running:

python --version

Install the required packages:

pip install -r requirements.txt

Load the environment variables from the .env file. If you're using a Unix-based system (like macOS or Linux), you can use:

source .env

If you're on Windows, use:

    set /p GENHEALTH_API_KEY=<.env

Running the tests:

    Navigate to the root directory of the project.

    Run the tests using the following command:


    pytest app/tests/

    This will execute all the tests inside the tests directory and display the results.

Understanding the tests:

    test_predict_endpoint: Tests the /v1/predict endpoint by sending a sample patient history and expects predictions from the GenHealth API in response.

    test_embeddings_endpoint: Tests the /v1/embeddings endpoint by sending a sample patient history and expects embeddings from the GenHealth API in response.