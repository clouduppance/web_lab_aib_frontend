import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useNoteContext } from '../NoteContext';

const DayDetails = () => {
  const { year, month, day } = useParams();
  const date = new Date(`${year}-${month}-${day}T00:00:00`);
  const { getNotesForDate, updateNotesForDate } = useNoteContext();
  const [noteData, setNoteData] = useState({});

  useEffect(() => {
    const noteForDate = getNotesForDate(date);
    setNoteData(noteForDate || {});

    const storedNotes = JSON.parse(localStorage.getItem('notes')) || {};
    const storedNoteForDate = storedNotes[date.toISOString().split('T')[0]];

    if (storedNoteForDate) {
      setNoteData(storedNoteForDate);
      updateNotesForDate(date, storedNoteForDate);
    }
  }, [date, getNotesForDate, updateNotesForDate]);

  const isValidDate = !isNaN(date.getTime());

  if (!isValidDate) {
    return <div>Invalid Date</div>;
  }
  
  const formattedDate = `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`;

  const noteText = Object.values(noteData).join('\n');

  const handleNoteChange = (e) => {
    const lines = e.target.value.split('\n');
    const updatedNoteData = lines.reduce((acc, line, index) => {
      acc[`value${index + 1}`] = line.trim();
      return acc;
    }, {});
    updateNotesForDate(date, updatedNoteData);
    setNoteData(updatedNoteData);
  };

  return (
    <div>
      <h2>Заметка на {formattedDate}</h2>
      <textarea
        placeholder="Тут должна быть заметка... "
        value={noteText}
        onChange={handleNoteChange}
      />
    </div>
  );
};

export default DayDetails;
