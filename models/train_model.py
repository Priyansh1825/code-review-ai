import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel, Trainer, TrainingArguments
from datasets import Dataset
import pandas as pd

class CodeReviewModel(nn.Module):
    """Custom AI model for code review tasks"""
    
    def __init__(self, model_name="microsoft/codebert-base"):
        super(CodeReviewModel, self).__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        self.classifier = nn.Linear(self.encoder.config.hidden_size, 5)  # 5 types of issues
        
    def forward(self, input_ids, attention_mask):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        return self.classifier(outputs.pooler_output)

class ModelTrainer:
    """Train custom AI models for code analysis"""
    
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
    
    def prepare_dataset(self, code_samples, labels):
        """Prepare dataset for training"""
        encodings = self.tokenizer(
            code_samples, 
            truncation=True, 
            padding=True, 
            max_length=512
        )
        
        dataset = Dataset.from_dict({
            'input_ids': encodings['input_ids'],
            'attention_mask': encodings['attention_mask'],
            'labels': labels
        })
        
        return dataset
    
    def train_model(self, train_dataset, eval_dataset):
        """Train the custom model"""
        model = CodeReviewModel()
        
        training_args = TrainingArguments(
            output_dir='./models/trained_models/results',
            num_train_epochs=3,
            per_device_train_batch_size=8,
            per_device_eval_batch_size=16,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir='./models/logs',
            logging_steps=10,
            evaluation_strategy="epoch",
            save_strategy="epoch"
        )
        
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=self.tokenizer
        )
        
        trainer.train()
        return trainer

# Usage example
if __name__ == "__main__":
    trainer = ModelTrainer()
    # Load your training data
    # train_dataset = trainer.prepare_dataset(train_codes, train_labels)
    # trainer.train_model(train_dataset, eval_dataset)