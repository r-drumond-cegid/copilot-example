import { AppBar, Toolbar, Typography, Box, Container } from '@mui/material';
import { AccountBalance as AccountBalanceIcon } from '@mui/icons-material';

const Header = () => {
  return (
    <AppBar position="static" elevation={0} sx={{ borderBottom: 1, borderColor: 'divider' }}>
      <Container maxWidth="xl">
        <Toolbar disableGutters sx={{ py: 1 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, flexGrow: 1 }}>
            <AccountBalanceIcon sx={{ fontSize: 32, color: 'primary.contrastText' }} />
            <Typography
              variant="h5"
              component="h1"
              sx={{
                fontWeight: 700,
                color: 'primary.contrastText',
                letterSpacing: '-0.5px',
              }}
            >
              Finance Dashboard
            </Typography>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Header;
