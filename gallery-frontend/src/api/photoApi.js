import axios from 'axios';

const API_BASE_URL = "http://127.0.0.1:5000";

export const fetchPhotos = async () => {
    const response = await axios.get(`${API_BASE_URL}/photos`);
    return response.data;
};

export const uploadPhoto = async (photo) => {
    const response = await axios.post(`${API_BASE_URL}/photos`, photo);
    return response.data;
};
