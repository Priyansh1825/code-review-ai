import React from 'react';
import { Paper, Typography } from '@mui/material';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { darcula } from 'react-syntax-highlighter/dist/esm/styles/prism';

const CodeDisplay = ({ code, language }) => {
  return (
    <Paper sx={{ p: 2, mt: 2 }}>
      <Typography variant="h6" gutterBottom>
        Code Preview
      </Typography>
      <SyntaxHighlighter 
        language={language} 
        style={darcula}
        showLineNumbers
        customStyle={{ maxHeight: '400px', borderRadius: '4px' }}
      >
        {code}
      </SyntaxHighlighter>
    </Paper>
  );
};

export default CodeDisplay;