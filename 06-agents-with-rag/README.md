# Multimodal RAG with Visual Retrieval using Amazon Nova, Amazon Bedrock, and CrewAI

This repository provides an in-depth implementation of **AI agents** using **CrewAI and AWS Bedrock**, demonstrating a variety of agent architectures, from basic implementations to advanced **multi-agent systems with memory capabilities**. The focus is on **multimodal retrieval-augmented generation (RAG) with video retrieval using Colpali**, enabling intelligent information retrieval across text and visual data.

## Prerequisites

Ensure you have Conda installed on your machine to manage your environments and packages.

## Setup

1. **Create and activate a new Conda environment**:
   ```bash
   conda create --name rag_env python=3.12
   conda activate rag_env
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Jupyter support**:
   ```bash
   conda install ipykernel
   python -m ipykernel install --user --name=rag_env --display-name "Python (rag_env)"
   ```

## Notebooks Overview

### 1. [Introduction to Agents](00-intro-agents.ipynb)
This notebook covers:
- LLM Selection and Configuration

- Basic Agent Implementation

- Tool-Enhanced Agents

- Multi-Agent Systems

- Memory-Enhanced Agents


### 2. [Multimodal Retrieval with Colpali](01-multimodal-retrieval-with-colpali-retrieve-gen.ipynb)
This notebook covers:
- Multimodal Retrieval Techniques

- Colpali Model for Visual-Text Search

- Vector Indexing and Retrieval

- Augmenting Agent Capabilities with Multimodal Data

### 3. [Agentic RAG with CrewAI,ColPali, Bedrock, and Amazon Nova](02-multimodal-retrival-with-colpali-retreve-gen-agents-crewAI.ipynb)
This notebook explores:
- Complex multi-agent orchestration

- Specialized agent roles with multimodal retrieval

- Integration of CrewAI for advanced agent collaboration


## Getting Started
1. Run the following command to start Jupyter Notebook:
    ```bash
    jupyter notebook
    ```

2. Follow the instructions in the notebook to run the code.

