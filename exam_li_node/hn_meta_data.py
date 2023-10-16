from llama_index.node_parser import SimpleNodeParser
from llama_index.node_parser.extractors import (
    MetadataExtractor,
    SummaryExtractor,
    QuestionsAnsweredExtractor,
    TitleExtractor,
    KeywordExtractor,
)
from llama_index.schema import Document

# Define the metadata extractor with a list of feature extractors
metadata_extractor = MetadataExtractor(
    extractors=[
        TitleExtractor(nodes=5),  # Extracts the title from the first 5 nodes
        QuestionsAnsweredExtractor(questions=3),  # Determines 3 questions that the excerpt can answer
        SummaryExtractor(summaries=["prev", "self"]),  # Provides summaries of the previous and current sections
        KeywordExtractor(keywords=10),  # Extracts the top 10 keywords
        #EntityExtractor(prediction_threshold=0.5),  # Extracts entities with a prediction threshold of 0.5
    ],
)

# Feed the metadata extractor to the node parser
node_parser = SimpleNodeParser.from_defaults(
    metadata_extractor=metadata_extractor,
)

# Sample document
text_document = """
Uber Technologies, Inc. 2019 Annual Report: Revolutionizing Mobility and Logistics Across 69 Countries and 111 Million MAPCs with $65 Billion in Gross Bookings.
The 2019 Annual Report provides an overview of the key topics and entities that have been important to the organization over the past year.
This section discusses a global tech platform that serves multiple multi-trillion dollar markets with products leveraging core technology and infrastructure.
"""

# Extract metadata from the document

#parser = SimpleNodeParser.from_defaults()
#nodes = parser.get_nodes_from_documents([document])


if __name__ == "__main__":
    document = Document(text=text_document)

    nodes = node_parser.get_nodes_from_documents([document])
    for node in nodes:
        print(node.metadata)
    print(nodes)
