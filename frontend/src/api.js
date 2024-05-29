import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1/ticket/';

export const getTickets = async () => {
    try {
        const response = await axios.get(`${API_URL}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching tickets:', error);
        throw error;
    }
};