import React from 'react';
import Day from './Day';

const MonthView = ({ selectedDate, onDateChange, notes }) => {
  const startOfMonth = new Date(selectedDate.getFullYear(), selectedDate.getMonth(), 1);
  const endOfMonth = new Date(selectedDate.getFullYear(), selectedDate.getMonth() + 1, 0);

  const firstDayOfWeek = startOfMonth.getDay() - 1;

  const startOfDisplayMonth = new Date(startOfMonth);
  startOfDisplayMonth.setDate(startOfDisplayMonth.getDate() - firstDayOfWeek);

  const endOfDisplayMonth = new Date(endOfMonth);
  const daysInLastWeek = 6 - endOfMonth.getDay();
  endOfDisplayMonth.setDate(endOfDisplayMonth.getDate() + daysInLastWeek);

  const daysInMonth = Math.ceil((endOfDisplayMonth - startOfDisplayMonth) / (24 * 60 * 60 * 1000)) + 2;

  const daysArray = Array.from({ length: daysInMonth }, (_, index) => {
    const day = new Date(startOfDisplayMonth);
    day.setDate(day.getDate() + index);

    const isOutsideMonth = day.getMonth() !== selectedDate.getMonth();
    const classNames = `day-container ${isOutsideMonth ? 'outside-month' : ''}`;

    return (
      <div key={index} className={classNames}>
        <Day date={day} onDateChange={onDateChange} notes={notes} />
      </div>
    );
  });

  return (
    <div>
      <div className="week-days">
        <div>пн</div>
        <div>вт</div>
        <div>ср</div>
        <div>чт</div>
        <div>пт</div>
        <div>сб</div>
        <div>вс</div>
      </div>

      <div className="month-view">{daysArray}</div>
    </div>
  );
};

export default MonthView;