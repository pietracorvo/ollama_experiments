# Run lllm models in ollama docker container locally with custom frontend



Ollama API docs https://github.com/ollama/ollama/blob/main/docs/api.md  


### Setup and run ollama docker container

Build and run docker container from https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image

```bash
docker run -d -v ollama_storage:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

and use docker start ollama afterwards

then go into the container and pull a model like llama:3.2

```bash
docker exec ollama bash -c "ollama pull llama3.2"
```

to make a request

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt":" Why is the colour of sea blue ?"
}'
```


### Other useful commands

Get the ollama logs from container

```bash
docker logs ollama
```

To run latest chroma container on port 8000
```bash
docker run -d -p 8000:8000 -v chroma-data:/chromadb/data chromadb/chroma
```


### TODOs

- hover cards with 2 side shadow to make illusion of flashcard https://stackoverflow.com/questions/50757671/add-shadow-effect-on-hover-to-div-boxes
- use local https://www.youtube.com/watch?v=FQTCLOUnIzI https://github.com/technovangelist/videoprojects/tree/2dd82eb1d8012e196f2e80b867744ebd42a10281/2024-09-10-buildrag/python to give rag capabilities using chrome docker container
- NOTE https://ollama.com/incept5/llama3.1-claude people say sonnet is best for coding reasoning
- implement context mechanism
- add llm options manipulation possiiblity (temperature, perplexity)
- FAR-FUTURE-TODO add multimodal capabilities
- langchain tutorial https://github.com/ollama/ollama/blob/main/docs/tutorials/langchainpy.md
