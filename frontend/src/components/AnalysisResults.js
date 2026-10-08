import React from 'react';
import {
  Paper,
  Typography,
  Box,
  Card,
  CardContent,
  Chip,
  LinearProgress,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Alert
} from '@mui/material';
import {
  Warning as WarningIcon,
  Error as ErrorIcon,
  Info as InfoIcon,
  CheckCircle as CheckCircleIcon
} from '@mui/icons-material';
import { styled } from '@mui/material/styles';

const ScorePaper = styled(Paper)(({ theme, score }) => ({
  padding: theme.spacing(2),
  background: score >= 80 
    ? 'linear-gradient(45deg, #4caf50, #81c784)'
    : score >= 60
    ? 'linear-gradient(45deg, #ff9800, #ffb74d)'
    : 'linear-gradient(45deg, #f44336, #e57373)',
  color: 'white',
  textAlign: 'center'
}));

const AnalysisResults = ({ analysis }) => {
  const getSeverityIcon = (severity) => {
    switch (severity) {
      case 'HIGH': return <ErrorIcon color="error" />;
      case 'MEDIUM': return <WarningIcon color="warning" />;
      case 'LOW': return <InfoIcon color="info" />;
      default: return <InfoIcon />;
    }
  };

  const getSeverityColor = (severity) => {
    switch (severity) {
      case 'HIGH': return 'error';
      case 'MEDIUM': return 'warning';
      case 'LOW': return 'info';
      default: return 'default';
    }
  };

  return (
    <Box sx={{ mt: 3 }}>
      <ScorePaper elevation={3} score={analysis.score}>
        <Typography variant="h4" gutterBottom>
          Code Quality Score: {analysis.score}/100
        </Typography>
        <LinearProgress 
          variant="determinate" 
          value={analysis.score} 
          sx={{ height: 10, borderRadius: 5 }}
          color={analysis.score >= 80 ? 'success' : analysis.score >= 60 ? 'warning' : 'error'}
        />
      </ScorePaper>

      <Grid container spacing={3} sx={{ mt: 1 }}>
        {/* Issues */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Code Issues ({analysis.issues.length})
              </Typography>
              <List>
                {analysis.issues.map((issue, index) => (
                  <ListItem key={index}>
                    <ListItemIcon>
                      {getSeverityIcon(issue.severity)}
                    </ListItemIcon>
                    <ListItemText
                      primary={issue.message}
                      secondary={`Type: ${issue.type}`}
                    />
                    <Chip 
                      label={issue.severity} 
                      color={getSeverityColor(issue.severity)}
                      size="small"
                    />
                  </ListItem>
                ))}
                {analysis.issues.length === 0 && (
                  <ListItem>
                    <ListItemIcon>
                      <CheckCircleIcon color="success" />
                    </ListItemIcon>
                    <ListItemText primary="No code issues found!" />
                  </ListItem>
                )}
              </List>
            </CardContent>
          </Card>
        </Grid>

        {/* Security Issues */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Security Issues ({analysis.security.length})
              </Typography>
              <List>
                {analysis.security.map((issue, index) => (
                  <ListItem key={index}>
                    <ListItemIcon>
                      <ErrorIcon color="error" />
                    </ListItemIcon>
                    <ListItemText
                      primary={issue.message}
                      secondary={`Type: ${issue.type}`}
                    />
                  </ListItem>
                ))}
                {analysis.security.length === 0 && (
                  <Alert severity="success">No security issues found!</Alert>
                )}
              </List>
            </CardContent>
          </Card>
        </Grid>

        {/* Suggestions */}
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Improvement Suggestions
              </Typography>
              <List>
                {analysis.suggestions.map((suggestion, index) => (
                  <ListItem key={index}>
                    <ListItemIcon>
                      <InfoIcon color="info" />
                    </ListItemIcon>
                    <ListItemText primary={suggestion} />
                  </ListItem>
                ))}
                {analysis.suggestions.length === 0 && (
                  <ListItem>
                    <ListItemIcon>
                      <CheckCircleIcon color="success" />
                    </ListItemIcon>
                    <ListItemText primary="Great job! No major suggestions." />
                  </ListItem>
                )}
              </List>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default AnalysisResults;