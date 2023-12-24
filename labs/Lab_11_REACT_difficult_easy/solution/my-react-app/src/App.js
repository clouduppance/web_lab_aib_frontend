// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { NoteProvider } from './NoteContext';
import Calendar from './components/Calendar';
import DayDetails from './components/DayDetails';
import './style.css';

const App = () => {
  return (
    <Router>
      <NoteProvider>
        <div className="app">
          <Routes>
            <Route path="/" element={<Calendar />} />
            <Route path="/:year/:month/:day" element={<DayDetails />} />
          </Routes>
        </div>
      </NoteProvider>
    </Router>
  );
};

export default App;
