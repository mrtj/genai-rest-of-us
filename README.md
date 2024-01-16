# Generative AI for the rest of us

Accompanying jupyter notebooks for the lecture "Generative AI for the rest of us"

## Getting started

1. Spin up your favorite python virtual environment manager ([venv](https://docs.python.org/3/library/venv.html), [Poetry](https://python-poetry.org/docs/), [miniconda](https://docs.conda.io/projects/miniconda/en/latest/), [pipenv](https://pipenv.pypa.io/en/latest/), [virtualenv](https://virtualenv.pypa.io/en/stable/), [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html), [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to name a few, in case of doubts which to choose, read [this article](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko))
2. Create a virtual environment for this project.
3. a. Download [Jupyter lab](https://jupyter.org/install), or<br/>
   b. use [VSCode](https://code.visualstudio.com/download) with built-in support for Jupyter notebooks.
4. Install dependencies:

```shell
pip install -r requirements.txt
```

## Contents

- [rag.ipynb](./rag.ipynb): A practical example of how to build a question answering system using Retrieval Augmented Generation.
- [clip.ipynb](./clip.ipynb): Introduction to multi-modal semantic search (text-to-image and image-to-image) with CLIP models.
- [stable-diff.ipynb](./stable-diff.ipynb): A getting started tutorial of WebUI for Stable Diffusion, showing how to use image inpainting assisted by an object segmentation algorithm.
