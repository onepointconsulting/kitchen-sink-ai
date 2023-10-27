# Websocket Server Experiment
Simple websocket server experiment in Python.

## Setup

We suggest to use [Conda](https://docs.conda.io/en/latest/) to manage the virtual environment and then install poetry.

```
conda activate base
conda remove -n websocket_server --all
conda create -n websocket_server python=3.11
conda activate websocket_server
pip install poetry
```

## Running the simple server

```
python.exe .\websocket_server\service\simple_query.py
```