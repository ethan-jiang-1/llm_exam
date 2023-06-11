#import os
import json

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

#from langchain.chains import RetrievalQA
#from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.indexes import VectorstoreIndexCreator
import langchain
#from IPython.display import display, Markdown

file = 'OutdoorClothingCatalog_1000_0.csv'

def load_df():
    import pandas as pd
    df = pd.read_csv(file)
    print(df)


def index_and_query():
    langchain.debug = True
    loader = CSVLoader(file_path=file)

    print("build vectorstore index...")
    index = VectorstoreIndexCreator(
        vectorstore_cls=DocArrayInMemorySearch
    ).from_loaders([loader])
    print("build vectorstore done.")

    query = "Please list all your shirts with sun protection in a table in markdown and summarize each one."
    #query = "Please list all your shirts with sun protection in json list, each shirt has name and description as keywords for the json dictionary, and summarize each one."

    response = index.query(query)
    print(response)

    try:
        rjson = json.loads(response.encode('utf-8'))
        print(rjson)
    except: # noqa
        pass
    langchain.debug = False


if __name__ == "__main__":
    load_df()
    index_and_query()