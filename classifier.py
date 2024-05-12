# classifier.py
import torch.nn as nn
from transformers import DistilBertTokenizer

embed_dim = 768  # Dimension của xuất bản từ DistilBERT

class ClassificationModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(embed_dim, 3)

    def forward(self, x):
        return self.fc(x)

def initialize_model():
    return ClassificationModel()

def train_model(model, criterion, optimizer, train_loader):
    # Lấy dữ liệu训练 phù hợp với format
    # Hãy đảm bảo input là danh sách có 2 phần: đầu tiên là các input, thứ hai là các label tương ứng
    # Ví dụ: inputs = [input_ids, ...] và targets = [theme_compliance, beauty, creativity]
    for epoch in range(10):
        for input_ids, target in train_loader:
            # Convert to tensors
            input_ids = torch.tensor(input_ids)
            target = torch.tensor(target)

            # Forward pass
            outputs = model(input_ids)

            # Compute loss
            loss = criterion(outputs, target)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

def predict_scores(model, inputs):
    # Convert to tensors
    inputs = torch.tensor(inputs)

    # Forward pass
    outputs = model(inputs)

    # Convert logits to probabilities
    return torch.softmax(outputs, dim=1).tolist()