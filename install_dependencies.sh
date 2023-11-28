#!/bin/bash

# Ensure the script stops if any command fails
set -e

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Get PyTorch version using Python and set it as a variable
TORCH=$(python -c "import torch; print(torch.__version__)" | sed 's/\+.*//')
export TORCH

# Echo the PyTorch version (Optional, for verification)
echo "PyTorch version: $TORCH"

# Install PyTorch Geometric dependencies
pip install -q torch-scatter -f https://data.pyg.org/whl/torch-${TORCH}.html
pip install -q torch-sparse -f https://data.pyg.org/whl/torch-${TORCH}.html
pip install -q git+https://github.com/pyg-team/pytorch_geometric.git

# Install Flask and related dependencies for gnnlens
pip install -U flask-cors
pip install Flask==2.0.3
pip install gnnlens