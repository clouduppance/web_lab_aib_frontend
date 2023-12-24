import React, { useState, useEffect } from 'react';
import MonthView from './MonthView';
import { useNoteContext } from '../NoteContext';

const Calendar = () => {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [notes, setNotes] = useState({});
  const { updateNotesForDate } = useNoteContext();

  useEffect(() => {
    const storedNotes = JSON.parse(localStorage.getItem('notes'));
    if (storedNotes) {
      setNotes(storedNotes);
    }
  }, []); 

  const handleDateChange = (newDate) => {
    setSelectedDate(newDate);
  };

  const handleDeleteNote = () => {
    const { [selectedDate.toISOString().split('T')[0]]: deletedNote, ...restNotes } = notes;

    const updatedNotes = {
      ...restNotes,
    };

    setNotes(updatedNotes);
    localStorage.setItem('notes', JSON.stringify(updatedNotes));

    updateNotesForDate(selectedDate, null);
  };

  const handlePrevMonth = () => {
    const prevMonth = new Date(selectedDate);
    prevMonth.setMonth(prevMonth.getMonth() - 1);
    setSelectedDate(prevMonth);
  };

  const handleNextMonth = () => {
    const nextMonth = new Date(selectedDate);
    nextMonth.setMonth(nextMonth.getMonth() + 1);
    setSelectedDate(nextMonth);
  };

  const addNote = () => {
    // Сохраняем выбранную дату перед вызовом prompt
    const currentSelectedDate = selectedDate;

    const title = prompt('Введите заголовок:');
    const mainText = prompt('Введите основной текст:');
    const time = prompt('Введите время:');
    const importance = prompt('Введите важность:');

    const newNote = {
      title,
      mainText,
      time,
      importance,
    };

    const updatedNotes = {
      ...notes,
      [currentSelectedDate.toISOString().split('T')[0]]: newNote,
    };

    setNotes(updatedNotes);
    localStorage.setItem('notes', JSON.stringify(updatedNotes));
    updateNotesForDate(currentSelectedDate, newNote);
  };

  return (
    <div className="Calendar">
      <div className="month-navigation">
        <button onClick={handlePrevMonth}>&lt; Предыдущий месяц</button>
        <input
          type="date"
          value={new Date(selectedDate.getTime() + 86400000).toISOString().split('T')[0]}
          onChange={(e) => handleDateChange(new Date(e.target.value))}
        />
        <button onClick={handleNextMonth}>Следующий месяц &gt;</button>
      </div>
      <MonthView
        selectedDate={selectedDate}
        onDateChange={handleDateChange}
        notes={notes}
      />
      <div className="add-note">
        <button onClick={() => addNote(prompt('Добавить заметку:'))}>Добавить заметку</button>
        <button onClick={handleDeleteNote}>Удалить заметку</button>
      </div>
    </div>
  );
};

export default Calendar;
