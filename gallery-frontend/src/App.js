import React from "react";
import Gallery from "./components/Gallery"; // Adjust the path if necessary

function App() {
  return (
    <div className="bg-gray-100 min-h-screen">
      <header className="bg-blue-600 text-white py-4 text-center">
        <h1 className="text-4xl font-bold">Gallery Management System</h1>
      </header>
      <main className="p-8">
        <Gallery />
      </main>
    </div>
  );
}

export default App;
