from llama_index import SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser

def get_documents():
    raw_data = "/root/llm_exam/llama_index/examples/paul_graham_essay/data"

    documents = SimpleDirectoryReader(raw_data).load_data()
    return documents


def make_nodes_from_documents(documents):
    parser = SimpleNodeParser.from_defaults()

    nodes = parser.get_nodes_from_documents(documents)
    return nodes


def make_index_from_nodes(nodes):
    from llama_index import VectorStoreIndex

    index = VectorStoreIndex(nodes)
    return index


if __name__ == "__main__":
    documents = get_documents()
    nodes = make_nodes_from_documents(documents)
    for ndx, node in enumerate(nodes):
        print()
        print(ndx, len(node.text))
        print(node)
        print()

    index = make_index_from_nodes(nodes)
    print(index)