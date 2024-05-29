import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import TicketList from './components/TicketList';

const App = () => {
    return (
        <Router>
            <div>
                <Routes>
                    <Route path="/" element={<TicketList />} />
                    {/* Добавьте другие маршруты по необходимости */}
                </Routes>
            </div>
        </Router>
    );
};

export default App;
