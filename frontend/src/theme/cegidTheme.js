import { createTheme } from '@mui/material/styles';

/**
 * Cegid Design System Theme Configuration
 * Following Cegid design guidelines and color palette
 */
export const cegidTheme = createTheme({
  palette: {
    primary: {
      main: '#0066CC', // Cegid Blue
      light: '#4D94E0',
      dark: '#004A99',
      contrastText: '#FFFFFF',
    },
    secondary: {
      main: '#00B8A9', // Cegid Teal
      light: '#4DD4C7',
      dark: '#008C7F',
      contrastText: '#FFFFFF',
    },
    error: {
      main: '#E60023', // Critical/Error
      light: '#FF4D5C',
      dark: '#B30019',
    },
    warning: {
      main: '#FF9800',
      light: '#FFB74D',
      dark: '#F57C00',
    },
    info: {
      main: '#2196F3',
      light: '#64B5F6',
      dark: '#1976D2',
    },
    success: {
      main: '#4CAF50',
      light: '#81C784',
      dark: '#388E3C',
    },
    background: {
      default: '#F5F7FA',
      paper: '#FFFFFF',
    },
    text: {
      primary: '#222222',
      secondary: '#666666',
      disabled: '#999999',
    },
    divider: '#E0E0E0',
  },
  typography: {
    fontFamily: [
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif',
    ].join(','),
    h1: {
      fontSize: '2.5rem',
      fontWeight: 600,
      lineHeight: 1.2,
      color: '#222222',
    },
    h2: {
      fontSize: '2rem',
      fontWeight: 600,
      lineHeight: 1.3,
      color: '#222222',
    },
    h3: {
      fontSize: '1.75rem',
      fontWeight: 600,
      lineHeight: 1.4,
      color: '#222222',
    },
    h4: {
      fontSize: '1.5rem',
      fontWeight: 500,
      lineHeight: 1.4,
      color: '#222222',
    },
    h5: {
      fontSize: '1.25rem',
      fontWeight: 500,
      lineHeight: 1.5,
      color: '#222222',
    },
    h6: {
      fontSize: '1rem',
      fontWeight: 500,
      lineHeight: 1.5,
      color: '#222222',
    },
    body1: {
      fontSize: '1rem',
      lineHeight: 1.5,
      color: '#222222',
    },
    body2: {
      fontSize: '0.875rem',
      lineHeight: 1.5,
      color: '#666666',
    },
    button: {
      textTransform: 'none',
      fontWeight: 500,
    },
  },
  shape: {
    borderRadius: 8,
  },
  shadows: [
    'none',
    '0px 2px 4px rgba(0, 0, 0, 0.1)',
    '0px 4px 8px rgba(0, 0, 0, 0.12)',
    '0px 8px 16px rgba(0, 0, 0, 0.14)',
    '0px 12px 24px rgba(0, 0, 0, 0.16)',
    '0px 16px 32px rgba(0, 0, 0, 0.18)',
    ...Array(19).fill('none'),
  ],
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 8,
          padding: '10px 24px',
          fontSize: '1rem',
          fontWeight: 500,
          textTransform: 'none',
          boxShadow: 'none',
          '&:hover': {
            boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.1)',
          },
        },
        containedPrimary: {
          backgroundColor: '#0066CC',
          '&:hover': {
            backgroundColor: '#004A99',
          },
        },
        outlined: {
          borderWidth: 2,
          '&:hover': {
            borderWidth: 2,
          },
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          boxShadow: '0px 2px 8px rgba(0, 0, 0, 0.08)',
          border: '1px solid #E0E0E0',
        },
      },
    },
    MuiChip: {
      styleOverrides: {
        root: {
          borderRadius: 16,
          fontWeight: 500,
        },
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          '& .MuiOutlinedInput-root': {
            borderRadius: 8,
          },
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 12,
        },
        elevation1: {
          boxShadow: '0px 2px 8px rgba(0, 0, 0, 0.08)',
        },
      },
    },
    MuiTableCell: {
      styleOverrides: {
        head: {
          fontWeight: 600,
          backgroundColor: '#F5F7FA',
          color: '#222222',
        },
      },
    },
    MuiAlert: {
      styleOverrides: {
        root: {
          borderRadius: 8,
        },
        standardError: {
          backgroundColor: '#FFE6E9',
          color: '#B30019',
        },
        standardWarning: {
          backgroundColor: '#FFF4E5',
          color: '#F57C00',
        },
        standardInfo: {
          backgroundColor: '#E3F2FD',
          color: '#1976D2',
        },
        standardSuccess: {
          backgroundColor: '#E8F5E9',
          color: '#388E3C',
        },
      },
    },
  },
});

export default cegidTheme;
