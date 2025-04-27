# PyTorch Model Training and Evaluation

This project demonstrates how to train and evaluate a simple model using PyTorch.

## Files

- `train.py`: Contains the training logic for the model.
- `evaluate.py`: Contains the evaluation logic for the model.

## Setup

1. Ensure you have PyTorch installed in your environment.
2. Run `train.py` to train the model.
3. Run `evaluate.py` to evaluate the model's performance.

## Environment Setup

To set up the environment, choose one of the following options:

### GPU Installation
For systems with GPU support, use the `environment_gpu.yml` file:

```bash
conda env create -f environment_gpu.yml
```

### CPU Installation
For systems without GPU support, use the `environment_cpu.yml` file:

```bash
conda env create -f environment_cpu.yml
```

This will create a conda environment with all the required dependencies for the respective setup.