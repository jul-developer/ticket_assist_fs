import React, { useEffect, useState } from 'react';
import { getTickets } from '../api';

const TicketList = () => {
    const [tickets, setTickets] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchTickets = async () => {
            try {
                const data = await getTickets();
                setTickets(data);
                setLoading(false);
            } catch (error) {
                setError(error);
                setLoading(false);
            }
        };

        fetchTickets();
    }, []);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error loading tickets: {error.message}</p>;

    return (
        <div>
            <h1>Tickets</h1>
            <ul>
                {tickets.map(ticket => (
                    <li key={ticket.id}>
                        <h2>{ticket.title}</h2>
                        <p>{ticket.problem}</p>
                        <p>Created by: {ticket.creator}</p>
                        <p>Created at: {new Date(ticket.time_create).toLocaleString()}</p>
                        <p>Last updated: {new Date(ticket.time_update).toLocaleString()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TicketList;