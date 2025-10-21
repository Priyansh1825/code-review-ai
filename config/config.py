import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('DEBUG', True)
    
    # AI Model Configuration
    HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Model Settings
    MAX_CODE_LENGTH = 10000
    SUPPORTED_LANGUAGES = ['python', 'javascript', 'java', 'cpp']
    
    # Analysis Thresholds
    COMPLEXITY_THRESHOLD = 10
    MAX_FUNCTION_LENGTH = 50
    MAX_FILE_LENGTH = 1000