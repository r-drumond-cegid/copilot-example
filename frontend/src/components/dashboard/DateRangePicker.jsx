import { Box, TextField } from '@mui/material';
import { DateRange as DateRangeIcon } from '@mui/icons-material';

const DateRangePicker = ({ fromDate, toDate, onChange }) => {
  const handleFromChange = (e) => {
    onChange(e.target.value, toDate);
  };

  const handleToChange = (e) => {
    onChange(fromDate, e.target.value);
  };

  return (
    <Box sx={{ display: 'flex', gap: 2, alignItems: 'center', flexWrap: 'wrap' }}>
      <DateRangeIcon sx={{ color: 'text.secondary', display: { xs: 'none', sm: 'block' } }} />
      <TextField
        label="Du"
        type="date"
        value={fromDate}
        onChange={handleFromChange}
        inputProps={{ max: toDate }}
        size="small"
        sx={{ minWidth: 150 }}
        InputLabelProps={{ shrink: true }}
      />
      <TextField
        label="Au"
        type="date"
        value={toDate}
        onChange={handleToChange}
        inputProps={{ min: fromDate }}
        size="small"
        sx={{ minWidth: 150 }}
        InputLabelProps={{ shrink: true }}
      />
    </Box>
  );
};

export default DateRangePicker;
