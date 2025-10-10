import numpy as np
import yaml
import json
import os
import matplotlib.pyplot as plt
import argparse

def train_model(version):
    print(f"Training model for version: {version}")
    
    # Load parameters
    with open('params.yaml', 'r') as f:
        params = yaml.safe_load(f)
    epochs = params["train"]["epochs"]
    learning_rate = params["train"]["learning_rate"]

    X_train_b = np.load(f'data/x_train_{version}.npy')
    y_train = np.load(f'data/y_train_{version}.npy')
    
    np.random.seed(42)
    thetas = np.random.randn(X_train_b.shape[1], 1)
    N = X_train_b.shape[0]
    losses = []

    print(f"Training on {len(X_train_b)} samples...")

    for _ in range(epochs):
        y_hat = X_train_b.dot(thetas)
        loss = np.mean((y_hat - y_train) ** 2)
        gradient = (2 / N) * X_train_b.T.dot(y_hat - y_train)
        thetas -= learning_rate * gradient
        losses.append(loss)
    
    os.makedirs('models', exist_ok=True)
    np.save(f'models/model_{version}.npy', thetas)

    metrics = {
        'dataset_size': len(X_train_b),
        'dataset_version': version,
        'model': f'model_{version}',
    }

    with open(f'models/metrics_{version}.json', 'w') as f:
        json.dump(metrics, f, indent=2)

    plt.plot(losses)
    plt.xlabel("Epoch")
    plt.ylabel("MSE Loss")
    plt.title("Training Loss Curve")
    plt.savefig("models/loss_curve.png")

    print(f"Model and metrics saved for {version}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', required=True, choices=['v1', 'v2'])
    args = parser.parse_args()
    
    train_model(args.version)