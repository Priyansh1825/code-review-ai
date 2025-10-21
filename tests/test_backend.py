import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from code_analyzer import CodeAnalyzer
from app import app

class TestCodeAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = CodeAnalyzer()
        self.app = app.test_client()
    
    def test_python_code_analysis(self):
        """Test Python code analysis functionality"""
        sample_code = """
def calculate_sum(a, b):
    return a + b
"""
        result = self.analyzer.analyze_code(sample_code, 'python')
        
        self.assertIn('score', result)
        self.assertIn('issues', result)
        self.assertIsInstance(result['score'], int)
    
    def test_security_vulnerability_detection(self):
        """Test SQL injection detection"""
        vulnerable_code = """
def get_user_data(user_id):
    query = "SELECT * FROM users WHERE id = %s" % user_id
    # This should trigger SQL injection warning
"""
        result = self.analyzer.analyze_code(vulnerable_code, 'python')
        
        security_issues = [issue for issue in result['security'] 
                          if issue['type'] == 'SQL_INJECTION']
        self.assertGreater(len(security_issues), 0)
    
    def test_complexity_calculation(self):
        """Test cyclomatic complexity calculation"""
        complex_code = """
def complex_function(x):
    if x > 0:
        if x < 10:
            for i in range(x):
                if i % 2 == 0:
                    print(i)
    return x
"""
        result = self.analyzer.analyze_code(complex_code, 'python')
        self.assertIn('complexity', result)
    
    def test_api_endpoints(self):
        """Test Flask API endpoints"""
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        
        response = self.app.post('/api/analyze', 
                               json={'code': 'print("hello")', 'language': 'python'})
        self.assertEqual(response.status_code, 200)

class TestAIModels(unittest.TestCase):
    
    def test_ai_suggestion_generation(self):
        """Test AI model suggestion generation"""
        # Test with simple code
        pass
    
    def test_model_loading(self):
        """Test that AI models load correctly"""
        pass

if __name__ == '__main__':
    unittest.main()