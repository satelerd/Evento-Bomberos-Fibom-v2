import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Test from './pages/test';
import Info from './pages/info.js';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Test />} exact />
        <Route path="/:postId" element={<Info />} exact />
        {/* <Route path="/:postId" component={Info} exact /> */}
      </Routes>
    </Router>
  );
}

export default App;
