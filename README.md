# RAG API with FastAPI and Ollama

This project implements a local Retrieval-Augmented Generation (RAG) API using FastAPI and Ollama.
It allows users to add documents to a knowledge base and query them using an LLM.
Document embeddings are generated and stored in a local vector database.
At query time, relevant document chunks are retrieved based on semantic similarity.
The retrieved context is injected into the prompt for grounded responses.
The system runs fully locally without external API dependencies.
TinyLlama is used as the language model via Ollama.
FastAPI exposes endpoints for adding and querying knowledge.
The `db/` directory stores vector embeddings persistently.
The project is intended for learning and experimentation with RAG systems.
It supports plain text documents such as technical notes and documentation.
This setup demonstrates core RAG concepts: chunking, embedding, retrieval, and generation.
