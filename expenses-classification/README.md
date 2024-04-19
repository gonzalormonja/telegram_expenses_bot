## Set env variables

You will need to get the following variables to be able to use the application:

SUPABASE_URL
SUPABASE_KEY
OPENAI_API_KEY

In addition, you can configure the list of categories to register using the CATEGORIES environment variable.

### Use without docker

If you want to use the application without docker you must:
1_ place yourself in the folder expenses-classification
2_ create a python virtual environment using `virtualenv venv`.
3_ enter the virtual environment using source `venv/bin/activate`.
4_ install the dependencies using `pip install --no-cache-dir -r requirements.txt` 
5_ run the project using `python src/main.py`.