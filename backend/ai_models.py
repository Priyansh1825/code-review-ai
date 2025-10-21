from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class AIModels:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.setup_models()
    
    def setup_models(self):
        try:
            # Code generation model
            self.code_generator = pipeline(
                "text-generation",
                model="microsoft/DialoGPT-medium",
                tokenizer="microsoft/DialoGPT-medium",
                device=self.device
            )
            
            # Code summarization model
            self.summarizer = pipeline(
                "summarization",
                model="facebook/bart-large-cnn",
                tokenizer="facebook/bart-large-cnn",
                device=self.device
            )
            
        except Exception as e:
            print(f"Model loading error: {e}")
            self.code_generator = None
            self.summarizer = None
    
    def generate_improvements(self, code, language):
        if not self.code_generator:
            return ["AI models not available. Using rule-based suggestions."]
        
        prompt = f"Improve this {language} code and suggest better practices:\n{code}\n\nSuggestions:"
        
        try:
            response = self.code_generator(
                prompt,
                max_length=150,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True
            )
            return [response[0]['generated_text'].replace(prompt, '').strip()]
        except Exception as e:
            return [f"AI suggestion error: {str(e)}"]

class AdvancedAIAnalysis:
    def __init__(self):
        try:
            self.sentiment_analyzer = pipeline(
                "sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english",
                device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            )
        except:
            self.sentiment_analyzer = None
    
    def analyze_code_sentiment(self, code):
        if not self.sentiment_analyzer:
            return {"error": "Sentiment analyzer not available"}
        
        # Extract comments for sentiment analysis
        comments = self.extract_comments(code)
        if not comments:
            return {"message": "No comments found for sentiment analysis"}
        
        try:
            results = self.sentiment_analyzer(comments)
            return {
                "comments_analyzed": len(comments),
                "overall_sentiment": self.aggregate_sentiment(results),
                "detailed_results": results
            }
        except Exception as e:
            return {"error": f"Sentiment analysis failed: {str(e)}"}
    
    def extract_comments(self, code):
        # Simple comment extraction for Python
        comments = []
        for line in code.split('\n'):
            stripped = line.strip()
            if stripped.startswith('#'):
                comments.append(stripped[1:].strip())
        return comments
    
    def aggregate_sentiment(self, results):
        if not results:
            return "NEUTRAL"
        
        positive_count = sum(1 for r in results if r['label'] == 'POSITIVE')
        negative_count = sum(1 for r in results if r['label'] == 'NEGATIVE')
        
        if positive_count > negative_count:
            return "POSITIVE"
        elif negative_count > positive_count:
            return "NEGATIVE"
        else:
            return "NEUTRAL"