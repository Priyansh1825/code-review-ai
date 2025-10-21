import os
import json
from collections import defaultdict

class DataCollector:
    """Collect and organize code datasets for training"""
    
    def __init__(self):
        self.datasets = defaultdict(list)
    
    def collect_from_github(self, query, language, limit=100):
        """Collect code samples from GitHub (conceptual)"""
        # This would use GitHub API to collect real code samples
        # For M.Tech project, you can use pre-existing datasets
        pass
    
    def load_codes_from_directory(self, directory_path):
        """Load code samples from local directory"""
        code_samples = []
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code_samples.append({
                            'file_path': file_path,
                            'code': f.read(),
                            'language': 'python'
                        })
        
        return code_samples
    
    def annotate_samples(self, code_samples, annotations):
        """Annotate code samples with issues"""
        annotated_data = []
        
        for sample, annotation in zip(code_samples, annotations):
            annotated_data.append({
                **sample,
                'issues': annotation.get('issues', []),
                'score': annotation.get('score', 0),
                'complexity': annotation.get('complexity', 0)
            })
        
        return annotated_data
    
    def save_dataset(self, dataset, filename):
        """Save dataset to JSON file"""
        with open(f'datasets/{filename}', 'w') as f:
            json.dump(dataset, f, indent=2)

# Example usage
if __name__ == "__main__":
    collector = DataCollector()
    
    # Collect sample codes
    python_codes = [
        {"code": GOOD_CODE_1, "language": "python"},
        {"code": BAD_CODE_1, "language": "python"}
    ]
    
    annotations = [
        {"issues": [], "score": 95},
        {"issues": ["POOR_NAMING", "MISSING_DOCSTRING"], "score": 65}
    ]
    
    annotated_data = collector.annotate_samples(python_codes, annotations)
    collector.save_dataset(annotated_data, 'training_dataset.json')