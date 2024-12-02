from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

print("Loading data ...")

documents = SimpleDirectoryReader("data").load_data()

print("Initializing models ...")

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama3.1", request_timeout=900.0)

print("Calculating vector ...")

index = VectorStoreIndex.from_documents(
    documents,
)

print("Preparing query engine ...")
query_engine = index.as_query_engine()
print("Ready!")

while True:
    response = query_engine.query(input(">>> "))
    print("\n\n")
    print(response)
    print("\n\n")

# print("Preparing chat engine ...")
# chat_engine = index.as_chat_engine()
# response = chat_engine.chat("Tell me a joke.")
# print("Ready!")

# while True:
#     streaming_response = chat_engine.stream_chat(input(">>> "))
#     for token in streaming_response.response_gen:
#         print(token, end="")
#     print("\n\n")
