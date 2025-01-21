# Multimodal RAG with ColPali, ColQwen2, and Amazon Nova

This repository contains the Jupyter Notebook and accompanying resources for implementing a Multimodal Retrieval-Augmented Generation (RAG) system. The notebook demonstrates the integration of document retrieval capabilities using ColPali, vision language processing using ColQwen2, and leveraging Amazon Nova for enhanced computational performance. This example showcases how different AI and ML components can be combined to create a robust multimodal system capable of understanding and generating responses based on text and visual inputs.

## Prerequisites

Ensure you have Conda installed on your machine to manage your environments and packages.

## Setup

Follow these steps to set up your environment to run the notebook:

1. **Create and activate a new Conda environment**:
   ```bash
   conda create --name mlenv python=3.12
   conda activate mlenv
   ```

2. **Install ipykernel and set up your environment with Jupyter**:
   ```bash
   conda install ipykernel
   python -m ipykernel install --user --name=mlenv --display-name="mlenv"
   ```

After setting up, launch your Jupyter Notebook in the `mlenv` environment to access the [01-multimodal-retrival-with-colpali-retreve-gen.ipynb](01-multimodal-retrival-with-colpali-retreve-gen.ipynb) notebook and start experimenting with Multimodal RAG using the provided models and tools.
