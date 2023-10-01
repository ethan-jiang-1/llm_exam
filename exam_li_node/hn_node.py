from llama_index.node_parser import HierarchicalNodeParser
#from llama_index.text_splitter import TextSplitter
from llama_index.text_splitter import TokenTextSplitter
import os

# create a HierarchicalNodeParser object
#hn_parser = HierarchicalNodeParser.from_defaults(chunk_sizes=[196, 128])
hn_parser = HierarchicalNodeParser.from_defaults()

# set the chunk size to 128
#hn_parser.chunk_size = 128

# create a TextSplitter object
#text_splitter = TextSplitter()

#text_splitter = TokenTextSplitter(separator=" ", chunk_size=128, chunk_overlap=128)


# set the text to be parsed
#text = "This is an example sentence to demonstrate the usage of HierarchicalNodeParser."

# parse the text using the HierarchicalNodeParser object
#bstr = text.encode('utf-8')

file_pathname = "/root/llm_exam/llama_index/examples/paul_graham_essay/data/paul_graham_essay.txt"
if os.path.isfile(file_pathname):
    nodes = hn_parser.parse_file(file_pathname)

    # print the nodes
    for node in nodes:
        print(node.text)

    print(len(nodes))