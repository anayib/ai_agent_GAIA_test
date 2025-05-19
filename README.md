---
title: Template Final Assignment
emoji: 🕵🏻‍♂️
colorFrom: indigo
colorTo: indigo
sdk: gradio
sdk_version: 5.25.2
app_file: app.py
pinned: false
hf_oauth: true
# optional, default duration is 8 hours/480 minutes. Max duration is 30 days/43200 minutes.
hf_oauth_expiration_minutes: 480
---

Agent with the following characterstics:

Core Components:
- Tool Definitions:
    - Basic math operations (multiply, add, subtract, divide, modulus)
    - Information retrieval tools:
        - wiki_search: Searches Wikipedia
        - web_search: Uses Tavily for web search
        - arvix_search: Searches Arxiv for research papers
- LLM Integration:
    - Supports multiple LLM providers:
        - Google Gemini
        - Groq (default, using qwen-qwq-32b model)
    - HuggingFace endpoints
Vector Store:
    - Uses Supabase with HuggingFace embeddings (sentence-transformers/all-mpnet-base-v2)
    - Enables semantic search over stored documents
Graph Architecture:
    - Built using StateGraph with MessagesState
Main nodes:
    - retriever: Finds similar questions from vector store
    - assistant: Processes user queries using LLM
    - tools: Handles tool execution
Workflow:
    - User query enters the graph
    - retriever node finds similar questions
    - assistant node processes the query with context
    - If tools are needed, routes to tools node
    - Returns final response
Key Features:
    - Modular design for easy tool addition
    - Support for multiple LLM providers
    - Integration with external services (Wikipedia, Arxiv, web search)
    - Vector-based retrieval for similar questions
Environment variable based configuration

Additional files to set up data embeddings:

- gaia/metadata_gaia.jsonl : contains questions and answers from the Gaia dataset
- import_data.py : script to import data into the vector store
- test_database.py : script to test the vector store
- metadata.jsonl : contains questions and answers from the final assignment dataset

To import data into the vector store, run the import_data.py script.
To test the vector store, run the test_database.py script.

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference