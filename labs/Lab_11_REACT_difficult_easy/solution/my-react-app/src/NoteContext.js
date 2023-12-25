// NoteContext.js
import React, { createContext, useContext, useState } from 'react';

const NoteContext = createContext();

export const NoteProvider = ({ children }) => {
  const [notes, setNotes] = useState({});

  const getNotesForDate = (date) => {
    const dateKey = date.toISOString().split('T')[0];
    return notes[dateKey] || "";
  };

  const updateNotesForDate = (date, newNote) => {
    const dateKey = date.toISOString().split('T')[0];
    const newNotes = {
      ...notes,
      [dateKey]: newNote,
    };
    setNotes(newNotes);
    localStorage.setItem('notes', JSON.stringify(newNotes));
  };

  return (
    <NoteContext.Provider value={{ getNotesForDate, updateNotesForDate }}>
      {children}
    </NoteContext.Provider>
  );
};

export const useNoteContext = () => {
  const context = useContext(NoteContext);
  if (!context) {
    throw new Error("useNoteContext must be used within a NoteProvider");
  }
  return context;
};
