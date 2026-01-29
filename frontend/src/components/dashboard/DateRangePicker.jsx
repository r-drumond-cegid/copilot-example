import { Box, Chip, Button } from '@cegid/cds-react';
import { TextField } from '@cegid/forms';
import { DateRange as DateRangeIcon } from '@mui/icons-material';
import { format, subDays, parseISO } from 'date-fns';

const DateRangePicker = ({ fromDate, toDate, onChange }) => {
  const handleFromChange = (e) => {
    onChange(e.target.value, toDate);
  };

  const handleToChange = (e) => {
    onChange(fromDate, e.target.value);
  };

  const setPreset = (days) => {
    const to = parseISO(toDate || format(new Date(), 'yyyy-MM-dd'));
    const from = subDays(to, days - 1);
    onChange(format(from, 'yyyy-MM-dd'), format(to, 'yyyy-MM-dd'));
  };

  const isInvalid = fromDate && toDate && parseISO(fromDate) > parseISO(toDate);

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
        helperText={isInvalid ? 'La date de début doit être antérieure à la date de fin.' : ''}
        error={isInvalid}
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
        helperText={isInvalid ? 'La date de fin doit être postérieure à la date de début.' : ''}
        error={isInvalid}
      />
      <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap' }}>
        <Chip label="7 jours" size="small" onClick={() => setPreset(7)} clickable />
        <Chip label="30 jours" size="small" onClick={() => setPreset(30)} clickable />
        <Chip label="90 jours" size="small" onClick={() => setPreset(90)} clickable />
        <Button size="small" variant="outlined" onClick={() => setPreset(30)} aria-label="Derniers 30 jours">Rapide: 30j</Button>
      </Box>
    </Box>
  );
};

export default DateRangePicker;
