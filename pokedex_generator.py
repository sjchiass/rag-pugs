from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
import os

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

# os.remove("./pokedex.md")

for name in [
    "Shoppug Spree",
    "Zombie Pug",
    "Pugkin",
    "Moonpug",
    "Pugsommar",
    "Santa Pug",
    "Snowed In",
    "Alien Pug",
    "Cowboy Pug",
]:
    prompt = f"""Write the pokedex entry for {name}. The pokedex entry will have five sections:\n\n1. Type (choose two of the following: Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Steel, Dragon, Dark, or Fairy)\n2. Description (short physical description)\n3. Special moves (bullet point list of three items)\n4. Habitat\n5. Diet\n\nFinish by adding any notes useful for pokemon trainers."""
    response = query_engine.query(prompt)
    print("\n")
    print(response)
    print("\n")
    with open("./pokedex.md", "a") as f:
        f.write(f"## {name}\n\n" + str(response) + "\n\n")
