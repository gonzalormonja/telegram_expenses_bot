## Set env variables

You will need to get the following variables to be able to use the application:

POSTGRES_URL
OPENAI_API_KEY

In addition, you can configure the list of categories to register using the CATEGORIES environment variable.

### Use without docker

If you want to use the application without docker you must:
1_ place yourself in the folder expenses-classification
2_ create a python virtual environment using `virtualenv venv`.
3_ enter the virtual environment using source `venv/bin/activate`.
4_ install the dependencies using `pip install --no-cache-dir -r requirements.txt` 
5_ run the project using `python src/main.py`.

#### Dependencies
* langchain: To obtain a prediction of the user's text
* fastapi: To use this service via http
* uvicorn: To run the http server
* python-dotenv: To configure the environment variables
* autopep8: To format the code
* PyJWT: To decode the user token
* psycopg2-binary: to database connection