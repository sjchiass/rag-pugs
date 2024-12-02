This is a repo with some very basic use of a RAG version of llama 3.1. Read about RAG here: https://en.wikipedia.org/wiki/Retrieval-augmented_generation

The script `query.py` has a basic example taken from the llamaindex guide. It is not stateful. I would have to find a way to create a custom chat_engine for llama.

## Setup + Guides

To start, download and install ollama: https://ollama.com/ Make sure to have ollama running with `ollama serve` so that llamaindex can connect to its models.

This guide for using ollama within llamaindex: https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/

The pip install would be the following. (The Hugging Face embeddings are necessary for embedding the documents for llama-3.1.)

`pip install llama-index-core llama-index-readers-file llama-index-llms-ollama llama-index-embeddings-huggingface`

## Some ideas for prompts

With the documents loaded, here are some ideas of prompts to try.

`Generate a debate between PugBeard the pirate pug and Byte the hacker cat between the R vs. Python. Pugbeard prefers R while Byte prefers Python. PlugPug the time-traveling cyborg will moderate. Have all participants stay in character.`

`Create an adventure where PugBeard, Byte and PlugPug travel to a fantasy world of sword and sorcery. They have to learn how to adapt to this new world and fight an evil wizard to return home.`

`Write the pokedex entry for PugBeard. The pokedex entry will have five sections:\n\n1. Type (choose two of the following: Normal, Fire, Water, Electric, Grass, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Steel, Dragon, Dark, or Fairy)\n2. Description (short physical description)\n3. Special moves (bullet point list of three items)\n4. Habitat\n5. Diet\n\nFinish by adding any notes useful for pokemon trainers.`

`Write a D&D 3.5 character sheet for PlugPug. Include character class, alignment, ability scores, skills, and backstory.`

`Please write a description of Byte as if she were a monster in a 90s dungeon crawler game. Describe the following:\n\n1. Where in the dungeon she can be found\n2. Her attacks\n3. What loot she drops when defeated.\n\nFinish by giving any hints to players on how to defeat her.`

`Please create a pirate pug named "Shoppug Spree". Give them the following appearance: "a cute beige pug who wears expensive pink designer sunglasses." In a single paragraph character description, describe their appearance, backstory, personality, coding style and favorite treats. For clarity, make sure their name is the subject of every sentence. Afterwards, describe in one sentence how they joined the RPUG.`
