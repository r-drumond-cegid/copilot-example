import React, { useState, useRef, useEffect } from 'react';
import {
  Box,
  Paper,
  Typography,
  TextField,
  IconButton,
  Fab,
  Chip,
  CircularProgress,
  Avatar,
  Slide,
  Button,
  useMediaQuery,
  useTheme,
} from '@cegid/cds-react';
import { Dialog, DialogTitle, DialogContent } from '@cegid/cds-react';
import {
  Send as SendIcon,
  Close as CloseIcon,
  Chat as ChatIcon,
  SmartToy as BotIcon,
  Person as PersonIcon,
} from '@mui/icons-material';
import { sendChatMessage } from '../../api/chat';

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});

const Chatbot = ({ isOpen, onToggle }) => {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
  const isTablet = useMediaQuery(theme.breakpoints.between('sm', 'md'));
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [sessionId, setSessionId] = useState(null);
  const [loading, setLoading] = useState(false);
  const [suggestions, setSuggestions] = useState([]);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (isOpen && messages.length === 0) {
      // Add welcome message
      setMessages([
        {
          id: 'welcome',
          role: 'assistant',
          content: 'Bonjour ! Je suis votre assistant financier IA. Comment puis-je vous aider aujourd\'hui ?',
          timestamp: new Date().toISOString(),
        },
      ]);
      setSuggestions([
        'Quel est mon solde total ?',
        'Montre-moi mes dernières transactions',
        'Génère un rapport mensuel',
      ]);
    }
  }, [isOpen]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSendMessage = async () => {
    if (!inputMessage.trim()) return;

    const userMessage = {
      id: `user_${Date.now()}`,
      role: 'user',
      content: inputMessage,
      timestamp: new Date().toISOString(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputMessage('');
    setLoading(true);

    try {
      const response = await sendChatMessage({
        message: inputMessage,
        session_id: sessionId,
      });

      if (!sessionId) {
        setSessionId(response.session_id);
      }

      setMessages(prev => [...prev, response.message]);
      setSuggestions(response.suggestions || []);
    } catch (error) {
      const errorMessage = {
        id: `error_${Date.now()}`,
        role: 'assistant',
        content: `Erreur: ${error.message}`,
        timestamp: new Date().toISOString(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  const handleSuggestionClick = (suggestion) => {
    setInputMessage(suggestion);
  };
  const handleNewChat = () => {
    setMessages([]);
    setSessionId(null);
    setSuggestions([
      'Quel est mon solde total ?',
      'Montre-moi mes dernières transactions',
      'Génère un rapport mensuel',
    ]);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <>
      {/* Toggle Button */}
      <Fab
        color="primary"
        onClick={onToggle}
        sx={{
          position: 'fixed',
          bottom: 24,
          right: 24,
          zIndex: 1000,
        }}
      >
        {isOpen ? <CloseIcon /> : <ChatIcon />}
      </Fab>

      {/* Chatbot Modal Dialog (CDS Dialog) */}
      <Dialog
        open={isOpen}
        onClose={onToggle}
        maxWidth={false}
        fullWidth={false}
        fullScreen={isMobile}
        TransitionComponent={Transition}
        scroll="paper"
        keepMounted
        sx={{
          '& .MuiDialog-container': {
            alignItems: isMobile ? 'stretch' : 'flex-end',
            justifyContent: isMobile ? 'center' : 'flex-end',
            p: isMobile ? 0 : 2,
          },
        }}
        PaperProps={{
          sx: {
            width: isMobile ? '100%' : 460,
            height: isMobile ? '100vh' : '82vh',
            maxHeight: isMobile ? '100vh' : '90vh',
            borderRadius: isMobile ? 0 : 3,
            display: 'flex',
            flexDirection: 'column',
            overflow: 'hidden',
            boxShadow: 6,
            border: 1,
            borderColor: 'primary.main',
          },
        }}
      >
          {/* Header */}
          <DialogTitle
            sx={{
              backgroundColor: 'primary.main',
              color: 'primary.contrastText',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              p: 2,
              position: 'sticky',
              top: 0,
              zIndex: 2,
            }}
          >
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <BotIcon />
              <Typography variant="h6" sx={{ fontWeight: 600 }}>
                Assistant IA
              </Typography>
            </Box>
            <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
              <Button onClick={handleNewChat} size="small" variant="outlined" disabled={loading} aria-label="Nouveau chat">
                Nouveau chat
              </Button>
              <IconButton
                size="small"
                onClick={onToggle}
                sx={{ color: 'primary.contrastText' }}
                aria-label="Fermer"
              >
                <CloseIcon />
              </IconButton>
            </Box>
          </DialogTitle>

          {/* Messages Area */}
          <DialogContent
            dividers
            sx={{
              flex: 1,
              p: 2,
              backgroundColor: 'background.default',
              display: 'flex',
              flexDirection: 'column',
              gap: 2,
              overflowX: 'hidden',
            }}
          >
            {/* A11y: announce incoming assistant messages */}
            <Box component="div" sx={{ position: 'absolute', width: 1, height: 1, overflow: 'hidden', clip: 'rect(0 0 0 0)' }} aria-live="polite" role="status" />
            {messages.map((message) => (
              <Box
                key={message.id}
                sx={{
                  display: 'flex',
                  alignItems: 'flex-start',
                  gap: 1,
                  flexDirection: message.role === 'user' ? 'row-reverse' : 'row',
                }}
              >
                <Avatar
                  sx={{
                    width: 32,
                    height: 32,
                    bgcolor: message.role === 'user' ? 'primary.main' : 'secondary.main',
                  }}
                >
                  {message.role === 'user' ? <PersonIcon fontSize="small" /> : <BotIcon fontSize="small" />}
                </Avatar>
                <Box
                  sx={{
                    maxWidth: '70%',
                  }}
                >
                  <Paper
                    elevation={1}
                    sx={{
                      p: 1.5,
                      backgroundColor: message.role === 'user' ? 'primary.light' : 'background.paper',
                      color: message.role === 'user' ? 'primary.contrastText' : 'text.primary',
                      borderRadius: 2,
                    }}
                  >
                    <Typography variant="body2" sx={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
                      {message.content}
                    </Typography>
                  </Paper>
                  <Typography
                    variant="caption"
                    color="text.secondary"
                    sx={{ ml: 1, mt: 0.5, display: 'block' }}
                  >
                    {new Date(message.timestamp).toLocaleTimeString('fr-FR', {
                      hour: '2-digit',
                      minute: '2-digit',
                    })}
                  </Typography>
                </Box>
              </Box>
            ))}
            
            {loading && (
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <Avatar
                  sx={{
                    width: 32,
                    height: 32,
                    bgcolor: 'secondary.main',
                  }}
                >
                  <BotIcon fontSize="small" />
                </Avatar>
                <Paper elevation={1} sx={{ p: 1.5, borderRadius: 2 }}>
                  <Box sx={{ display: 'flex', gap: 0.5, alignItems: 'center' }}>
                    <CircularProgress size={16} />
                    <Typography variant="body2" color="text.secondary">
                      En cours de réflexion...
                    </Typography>
                  </Box>
                </Paper>
              </Box>
            )}
            <div ref={messagesEndRef} />
          </DialogContent>

          {/* Suggestions */}
          {suggestions.length > 0 && (
            <Box
              sx={{
                p: 1.5,
                display: 'flex',
                gap: 1,
                flexWrap: 'wrap',
                borderTop: 1,
                borderColor: 'divider',
                backgroundColor: 'background.paper',
              }}
            >
              {suggestions.map((suggestion, index) => (
                <Chip
                  key={index}
                  label={suggestion}
                  onClick={() => handleSuggestionClick(suggestion)}
                  disabled={loading}
                  size="small"
                  sx={{ cursor: 'pointer' }}
                />
              ))}
            </Box>
          )}

          {/* Input Area */}
          <Box
            sx={{
              p: 2,
              borderTop: 1,
              borderColor: 'divider',
              backgroundColor: 'background.paper',
              position: 'sticky',
              bottom: 0,
            }}
          >
            <Box sx={{ display: 'flex', gap: 1, alignItems: 'flex-end' }}>
              <TextField
                fullWidth
                multiline
                maxRows={3}
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Posez votre question..."
                disabled={loading}
                variant="outlined"
                size="small"
                inputProps={{ 'aria-describedby': 'chat-input-help' }}
                sx={{
                  '& .MuiOutlinedInput-root': {
                    borderRadius: 2,
                  },
                }}
              />
              <IconButton
                color="primary"
                onClick={handleSendMessage}
                disabled={!inputMessage.trim() || loading}
                sx={{
                  backgroundColor: 'primary.main',
                  color: 'primary.contrastText',
                  '&:hover': {
                    backgroundColor: 'primary.dark',
                  },
                  '&.Mui-disabled': {
                    backgroundColor: 'action.disabledBackground',
                  },
                }}
              >
                <SendIcon />
              </IconButton>
            </Box>
            <Typography id="chat-input-help" variant="caption" color="text.secondary" sx={{ mt: 0.5, display: 'block' }}>
              Entrée: envoyer. Maj+Entrée: retour à la ligne.
            </Typography>
          </Box>
        </Dialog>
    </>
  );
};

export default Chatbot;
