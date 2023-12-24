import React from 'react';
import { Link } from 'react-router-dom';

const Day = ({ date, onDateChange, notes }) => {
  if (!date) {
    return <div className="day">{' '}</div>;
  }

  const isToday = () => {
    const today = new Date();
    return (
      date.getDate() === today.getDate() &&
      date.getMonth() === today.getMonth() &&
      date.getFullYear() === today.getFullYear()
    );
  };

  const handleClick = () => {
    if (onDateChange && typeof onDateChange === 'function') {
      onDateChange(date);
    } 
  };

  return (
    <div className={`${isToday() ? 'today' : 'day'}`} onClick={handleClick}>
      <Link to={`/${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`} className="day-day">
        {date.getDate()}
      </Link>
      {notes[date.toISOString().split('T')[0]] && (
        <div className="note">
          <span className="note-title"><strong>{notes[date.toISOString().split('T')[0]].title}</strong></span><br />
          <div className="note-text">{notes[date.toISOString().split('T')[0]].mainText}</div>
          <span className="note-time">{notes[date.toISOString().split('T')[0]].time}</span><br />
          <span className="note-importance">{notes[date.toISOString().split('T')[0]].importance}</span><br />
        </div>
      )}
    </div>
  );
};

export default Day;
