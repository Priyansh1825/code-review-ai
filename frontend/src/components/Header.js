import React from 'react';
import { AppBar, Toolbar, Typography, Chip, Box } from '@mui/material';
import { Code as CodeIcon } from '@mui/icons-material';

const Header = () => {
  return (
    <AppBar position="static" elevation={2}>
      <Toolbar>
        <CodeIcon sx={{ mr: 2 }} />
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          AI Code Review Assistant
        </Typography>
        <Box sx={{ display: { xs: 'none', md: 'block' } }}>
          <Chip 
            label="M.Tech AI Project" 
            variant="outlined" 
            sx={{ color: 'white', borderColor: 'white' }}
          />
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Header;