import React, { useState } from 'react';
import {
  Container,
  Paper,
  TextField,
  Button,
  Typography,
  Box,
  Card,
  CardContent,
  Chip,
  Alert,
  CircularProgress,
  Grid
} from '@mui/material';
import { styled } from '@mui/material/styles';
import axios from 'axios';
import CodeDisplay from './components/CodeDisplay';
import AnalysisResults from './components/AnalysisResults';
import './App.css';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  margin: theme.spacing(2, 0),
}));

function App() {
  const [code, setCode] = useState('');
  const [language, setLanguage] = useState('python');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const analyzeCode = async () => {
    if (!code.trim()) {
      setError('Please enter some code to analyze');
      return;
    }

    setLoading(true);
    setError('');
    
    try {
      const response = await axios.post('http://localhost:5000/api/analyze', {
        code,
        language
      });
      setAnalysis(response.data);
    } catch (err) {
      setError('Failed to analyze code. Please try again.');
      console.error('Analysis error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          🤖 AI Code Review Assistant
        </Typography>
        
        <StyledPaper elevation={3}>
          <Typography variant="h5" gutterBottom>
            Enter Your Code
          </Typography>
          
          <TextField
            select
            label="Language"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            sx={{ mb: 2, minWidth: 120 }}
            SelectProps={{
              native: true,
            }}
          >
            <option value="python">Python</option>
            <option value="javascript">JavaScript</option>
            <option value="java">Java</option>
          </TextField>

          <TextField
            multiline
            rows={15}
            fullWidth
            variant="outlined"
            placeholder="Paste your code here..."
            value={code}
            onChange={(e) => setCode(e.target.value)}
            sx={{ mb: 2 }}
          />

          <Button
            variant="contained"
            color="primary"
            onClick={analyzeCode}
            disabled={loading}
            startIcon={loading ? <CircularProgress size={20} /> : null}
          >
            {loading ? 'Analyzing...' : 'Analyze Code'}
          </Button>

          {error && (
            <Alert severity="error" sx={{ mt: 2 }}>
              {error}
            </Alert>
          )}
        </StyledPaper>

        {analysis && (
          <AnalysisResults analysis={analysis} />
        )}

        {code && !analysis && !loading && (
          <CodeDisplay code={code} language={language} />
        )}
      </Box>
    </Container>
  );
}

export default App;