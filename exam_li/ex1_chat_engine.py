from llama_index import VectorStoreIndex, SimpleDirectoryReader

import logging
import sys
import openai 

openai.log = "debug"

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#documents = SimpleDirectoryReader('data').load_data()
fd_data = "/root/llm_exam/llama_index/examples/paul_graham_essay/data"
documents = SimpleDirectoryReader(fd_data).load_data()
index = VectorStoreIndex.from_documents(documents)

# query_engine = index.as_query_engine()
# response = query_engine.query("What did the author do growing up?")
# print(response)
# print()

chat_engine = index.as_chat_engine()
response = chat_engine.query("What did the author do growing up?")
print(response)