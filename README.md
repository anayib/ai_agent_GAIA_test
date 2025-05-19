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

## Agent with the following characterstics:

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

## Additional files:

Files that are not required for the agent to work but have been provided as reference to customized the set of answers and test locally the agent.

### Data files
- gaia/metadata_gaia.jsonl : contains questions and answers from the Gaia dataset
- import_data.py : script to import data into the vector store
- test_database.py : script to test the vector store
- metadata.jsonl : contains questions and answers from the final assignment dataset

### Local agent implementation (alternative to Gradio)

- test_agent.py : script to test the agent locally

### How to push to huggingface space

To import data into the vector store, run the import_data.py script.
To test the vector store, run the test_database.py script.

## Contributing to HF Spaca       

1. Add the space origin URL as a remote: `git remote set-url origin https://<your-username>:<your-token>@huggingface.co/spaces/anayib/hf-final-agent`
3. `git add < . | [..file names]>`
2. `git commit -m "<case>Your commit message"`
3. `git push origin <branch name>`


## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push your changes to your fork
5. Create a pull request


### Commit Messages

We use Conventional Commits to format our commit messages.

| Prefix       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `feat`       | A new feature (triggers a **minor** version bump in SemVer).                |
| `fix`        | A bug fix (triggers a **patch** version bump in SemVer).                    |
| `docs`       | Documentation changes (README, comments, etc.).                             |
| `style`      | Code style changes (formatting, linting, no functional changes).            |
| `refactor`   | Code restructuring (no new features or bug fixes).                          |
| `perf`       | Performance improvements.                                                   |
| `test`       | Adding or modifying tests.                                                  |
| `chore`      | Maintenance tasks (build config, dependencies, CI/CD).                      |
| `revert`     | Reverting a previous commit.                                                |
| `ci`         | Changes to CI/CD pipelines.                                                 |
| `build`      | Changes affecting the build system or dependencies.                         |

---

### Format of a Conventional Commit

```
<type>(<scope>): <description>
[optional body]
[optional footer]
```

```bash
**`<type>`**: The kind of change (`feat`, `fix`, `docs`, etc.).
**`<scope>`** (optional): The part of the codebase affected (e.g., `auth`, `api`, `ui`).
**`<description>`**: A concise summary of changes (imperative tense: "add" instead of "added").
**Body** (optional): Detailed explanation if needed.
**Footer** (optional): References like `BREAKING CHANGE:` or issue links (`Closes #123`).
```

---

### Examples

#### 1. Simple Feature Addition
```bash
git commit -m "feat(auth): add OAuth2 login support"
```

#### 2. Bug Fix with Issue Reference
```bash
git commit -m "fix(api): handle null response in user endpoint

Closes #456"
```
#### 3. Breaking Change (Major Version Bump)
```bash

git commit -m "feat(db): migrate to PostgreSQL
