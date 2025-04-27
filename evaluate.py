import torch
from train import SimpleModel

# Evaluation function
def evaluate_model():
    # Load the trained model (for simplicity, using the same model definition)
    model = SimpleModel(input_size=10, output_size=2)
    model.eval()

    # Example test data
    test_data = torch.randn(20, 10)
    test_labels = torch.randint(0, 2, (20,))

    with torch.no_grad():
        outputs = model(test_data)
        predictions = torch.argmax(outputs, dim=1)
        accuracy = (predictions == test_labels).float().mean()

    print(f"Accuracy: {accuracy.item() * 100:.2f}%")

if __name__ == "__main__":
    evaluate_model()