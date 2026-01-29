// Local shim for @cegid/cds-react
// Maps required components to MUI equivalents so the app can run
// Primitives
export { default as Button } from '@mui/material/Button';
export { default as Alert } from '@mui/material/Alert';
export { default as Box } from '@mui/material/Box';
export { default as Typography } from '@mui/material/Typography';
export { default as CircularProgress } from '@mui/material/CircularProgress';

// Layout
export { default as Grid } from '@mui/material/Grid';
export { default as Paper } from '@mui/material/Paper';
export { default as Card } from '@mui/material/Card';
export { default as CardContent } from '@mui/material/CardContent';
export { default as Container } from '@mui/material/Container';

// App bar
export { default as AppBar } from '@mui/material/AppBar';
export { default as Toolbar } from '@mui/material/Toolbar';

// Dialogs
export { default as Dialog } from '@mui/material/Dialog';
export { default as DialogTitle } from '@mui/material/DialogTitle';
export { default as DialogContent } from '@mui/material/DialogContent';

// Forms
export { default as TextField } from '@mui/material/TextField';
export { default as FormControl } from '@mui/material/FormControl';
export { default as InputLabel } from '@mui/material/InputLabel';
export { default as Select } from '@mui/material/Select';
export { default as MenuItem } from '@mui/material/MenuItem';
export { default as Chip } from '@mui/material/Chip';
export { default as Stack } from '@mui/material/Stack';
export { default as IconButton } from '@mui/material/IconButton';
export { default as Fab } from '@mui/material/Fab';
export { default as Avatar } from '@mui/material/Avatar';
export { default as Divider } from '@mui/material/Divider';
export { default as Slide } from '@mui/material/Slide';
export { useTheme } from '@mui/material';
export { default as useMediaQuery } from '@mui/material/useMediaQuery';
export { default as Pagination } from '@mui/material/Pagination';

// Tables
export { default as Table } from '@mui/material/Table';
export { default as TableBody } from '@mui/material/TableBody';
export { default as TableCell } from '@mui/material/TableCell';
export { default as TableContainer } from '@mui/material/TableContainer';
export { default as TableHead } from '@mui/material/TableHead';
export { default as TableRow } from '@mui/material/TableRow';

// Allow default import fallback (noop)
export default {};