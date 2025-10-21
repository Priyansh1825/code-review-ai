from flask import Flask, request, jsonify
from flask_cors import CORS
from code_analyzer import CodeAnalyzer
from ai_models import AIModels, AdvancedAIAnalysis
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize analyzers
analyzer = CodeAnalyzer()
ai_models = AIModels()
advanced_ai = AdvancedAIAnalysis()

@app.route('/api/analyze', methods=['POST'])
def analyze_code():
    try:
        data = request.json
        code = data.get('code', '')
        language = data.get('language', 'python')
        
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        # Perform comprehensive analysis
        basic_analysis = analyzer.analyze_code(code, language)
        ai_suggestions = ai_models.generate_improvements(code, language)
        sentiment_analysis = advanced_ai.analyze_code_sentiment(code)
        
        # Combine all analyses
        comprehensive_analysis = {
            **basic_analysis,
            'ai_suggestions': ai_suggestions,
            'sentiment_analysis': sentiment_analysis,
            'timestamp': '2024-01-01T00:00:00Z'  # Add actual timestamp
        }
        
        return jsonify(comprehensive_analysis)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/languages', methods=['GET'])
def get_supported_languages():
    return jsonify({
        'languages': analyzer.supported_languages,
        'message': 'Supported programming languages'
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy', 
        'message': 'Code Review AI Assistant is running',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)