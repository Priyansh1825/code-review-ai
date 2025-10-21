import json
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

class ModelEvaluator:
    """Evaluate AI model performance"""
    
    def evaluate_model(self, predictions, ground_truth):
        """Comprehensive model evaluation"""
        
        metrics = {
            'accuracy': accuracy_score(ground_truth, predictions),
            'precision': precision_score(ground_truth, predictions, average='weighted'),
            'recall': recall_score(ground_truth, predictions, average='weighted'),
            'f1_score': f1_score(ground_truth, predictions, average='weighted')
        }
        
        return metrics
    
    def confusion_matrix_analysis(self, y_true, y_pred, labels):
        """Detailed confusion matrix analysis"""
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(y_true, y_pred, labels=labels)
        return cm
    
    def save_evaluation_results(self, metrics, filepath):
        """Save evaluation results to JSON"""
        with open(filepath, 'w') as f:
            json.dump(metrics, f, indent=2)

# Example evaluation
evaluator = ModelEvaluator()
# metrics = evaluator.evaluate_model(predictions, ground_truth)