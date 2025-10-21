import ast
import re
import radon.complexity as radon_cc
import radon.metrics as radon_metrics
import tempfile
import os

class CodeAnalyzer:
    def __init__(self):
        self.supported_languages = ['python', 'javascript', 'java']
    
    def analyze_code(self, code, language='python'):
        analysis = {
            'complexity': self.calculate_complexity(code, language),
            'issues': self.detect_issues(code, language),
            'security': self.security_scan(code, language),
            'metrics': self.calculate_metrics(code, language),
            'suggestions': self.generate_suggestions(code, language),
            'score': 0
        }
        
        # Calculate overall score (0-100)
        analysis['score'] = self.calculate_overall_score(analysis)
        
        return analysis
    
    def calculate_complexity(self, code, language):
        if language == 'python':
            try:
                # Use radon for cyclomatic complexity
                complexity = radon_cc.cc_visit(code)
                return [{'name': func.name, 'complexity': func.complexity} for func in complexity]
            except:
                return []
        return []
    
    def detect_issues(self, code, language):
        issues = []
        
        # Common code smells detection
        if language == 'python':
            # Long function detection
            lines = code.split('\n')
            if len(lines) > 50:
                issues.append({
                    'type': 'LONG_FUNCTION',
                    'message': 'Function is too long. Consider breaking it down.',
                    'severity': 'MEDIUM'
                })
            
            # TODO comments detection
            todo_pattern = r'#\s*TODO'
            if re.search(todo_pattern, code, re.IGNORECASE):
                issues.append({
                    'type': 'TODO_COMMENT',
                    'message': 'TODO comments found. Address them before production.',
                    'severity': 'LOW'
                })
        
        return issues
    
    def security_scan(self, code, language):
        security_issues = []
        
        if language == 'python':
            # SQL injection detection
            if 'execute(' in code and '%s' in code:
                security_issues.append({
                    'type': 'SQL_INJECTION',
                    'message': 'Potential SQL injection vulnerability. Use parameterized queries.',
                    'severity': 'HIGH'
                })
            
            # Hardcoded secrets detection
            secret_patterns = [
                r'password\s*=\s*["\'][^"\']+["\']',
                r'api_key\s*=\s*["\'][^"\']+["\']',
                r'secret\s*=\s*["\'][^"\']+["\']'
            ]
            
            for pattern in secret_patterns:
                if re.search(pattern, code, re.IGNORECASE):
                    security_issues.append({
                        'type': 'HARDCODED_SECRET',
                        'message': 'Potential hardcoded secret detected.',
                        'severity': 'HIGH'
                    })
        
        return security_issues
    
    def calculate_metrics(self, code, language):
        if language == 'python':
            try:
                metrics = radon_metrics.mi_visit(code, True)
                return {
                    'maintainability_index': metrics,
                    'lines_of_code': len(code.split('\n')),
                    'logical_lines': len([line for line in code.split('\n') if line.strip() and not line.strip().startswith('#')])
                }
            except:
                return {}
        return {}
    
    def generate_suggestions(self, code, language):
        suggestions = []
        
        if language == 'python':
            # Add function docstring suggestion
            if 'def ' in code and '"""' not in code and "'''" not in code:
                suggestions.append('Add docstrings to your functions for better documentation.')
            
            # Variable naming suggestion
            if re.findall(r'[a-z]_[a-z]', code):
                suggestions.append('Consider using more descriptive variable names.')
        
        return suggestions
    
    def calculate_overall_score(self, analysis):
        base_score = 100
        
        # Deduct for complexity
        for func in analysis['complexity']:
            if func['complexity'] > 10:
                base_score -= 5
        
        # Deduct for issues
        for issue in analysis['issues']:
            if issue['severity'] == 'HIGH':
                base_score -= 10
            elif issue['severity'] == 'MEDIUM':
                base_score -= 5
            else:
                base_score -= 2
        
        # Deduct for security issues
        for sec_issue in analysis['security']:
            if sec_issue['severity'] == 'HIGH':
                base_score -= 15
        
        return max(0, base_score)