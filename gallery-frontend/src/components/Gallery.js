import React, { useState, useEffect } from 'react';
import { fetchPhotos } from '../api/photoApi';

const Gallery = () => {
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    fetchPhotos().then(data => setPhotos(data));
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold text-center mb-4 text-blue-600">
        Photo Gallery
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {photos.map(photo => (
          <div key={photo.id} className="p-4 border rounded shadow">
            <h3 className="font-bold text-lg">{photo.title}</h3>
            <img src={photo.url} alt={photo.title} className="w-full mt-2" />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Gallery;
