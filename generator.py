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

os.remove("./data/other_pugs.txt")

for name, description in [
    ["Shoppug Spree", "it is a cute beige pug who wears expensive pink designer sunglasses"],
    ["Zombie Pug", "it is a green zombie pirate pug with a tricorne hat and a long stitch down its cheek"],
    ["Pugkin", "it is a cute pirate pug whose head has been transformed into a pumpkin"],
    ["Moonpug", "it is a cute pirate pug whose head has been transformed into a mooncake"],
    ["Pugsommar", "she is a cute pirate pug who wears a crown of colorful flowers instead of a tricorne hat"],
    ["Santa Pug", "it is a cute pirate pug who dresses as Santa Claus"],
    ["Snowed In", "it is a pirate pug that is entirely buried under snow"],
    ["Alien Pug", "it is a cute pirate pug that is half green alien with big black eyes"],
    ["Cowboy Pug", "it is a pirate pug wearing a cowboy hat"],
    ["PSL Pug", "it is a pirate pug that is always sipping a pumpkin spice latte"],
]:
    prompt = f"""Please create a pirate pug named "{name}". Give them the following appearance: "{description}". In a single paragraph character description, describe their appearance, backstory, personality, coding style and favorite treats. For clarity, make sure their name is the subject of every sentence. Afterwards, describe in one sentence how they joined the RPUG."""
    while True:
        response = query_engine.query(prompt)
        if "\n" in str(response):
            print("Response had a newline ... Generating again ...")
        else:
            break
    print("\n")
    print(response)
    print("\n")
    with open("./data/other_pugs.txt", "a") as f:
        f.write(str(response)+"\n\n")