import './DateRangePicker.css';

const DateRangePicker = ({ fromDate, toDate, onChange }) => {
  const handleFromChange = (e) => {
    onChange(e.target.value, toDate);
  };

  const handleToChange = (e) => {
    onChange(fromDate, e.target.value);
  };

  return (
    <div className="date-range-picker">
      <div className="date-input-group">
        <label>Du</label>
        <input 
          type="date" 
          value={fromDate} 
          onChange={handleFromChange}
          max={toDate}
        />
      </div>
      <div className="date-input-group">
        <label>Au</label>
        <input 
          type="date" 
          value={toDate} 
          onChange={handleToChange}
          min={fromDate}
        />
      </div>
    </div>
  );
};

export default DateRangePicker;
