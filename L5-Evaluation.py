from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import DocArrayInMemorySearch
import langchain

file = 'OutdoorClothingCatalog_1000.csv'

def do_retrievel_qa():
    loader = CSVLoader(file_path=file)
    #data = loader.load()

    index = VectorstoreIndexCreator(
        vectorstore_cls=DocArrayInMemorySearch
    ).from_loaders([loader])

    llm = ChatOpenAI(temperature = 0.0)
    qa = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=index.vectorstore.as_retriever(), 
        verbose=True,
        chain_type_kwargs = {
            "document_separator": "<<<<>>>>>"
        }
    )

    print(qa)

# examples = [
#     {
#         "query": "Do the Cozy Comfort Pullover Set\
#         have side pockets?",
#         "answer": "Yes"
#     },
#     {
#         "query": "What collection is the Ultra-Lofty \
#         850 Stretch Down Hooded Jacket from?",
#         "answer": "The DownTek collection"
#     }
# ]

def do_examples():
    from langchain.evaluation.qa import QAGenerateChain
    langchain.debug = True

    loader = CSVLoader(file_path=file)
    data = loader.load()

    print(len(data))
    print(data[0])
    print(data[1])
    print()

    example_gen_chain = QAGenerateChain.from_llm(ChatOpenAI())

    docs = [{"doc": t} for t in data[:2]]
    #docs = [{"doc": t} for t in data[:5]]
    print(docs)
    print()

    new_examples = example_gen_chain.apply_and_parse(docs)

    print(new_examples)
    langchain.debug = False


if __name__ == "__main__":
    do_examples()