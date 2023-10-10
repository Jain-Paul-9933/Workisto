import React from "react";
import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <div>
      <nav className="bg-blue-500 p-4">
        <div className="container mx-auto flex items-center justify-between">
          <Link to="/" className="text-white text-2xl font-kaushan">
            Workisto
          </Link>
          <ul className="flex space-x-4">
            <li>
              <Link to="/" className="text-white hover:text-gray-200">
                Home
              </Link>
            </li>
            <li>
              <Link to="/login" className="text-white hover:text-gray-200">
                Login
              </Link>
            </li>
          </ul>
        </div>
      </nav>

      <div className="container mx-auto mt-8">
        <h1 className="text-3xl font-semibold">Welcome to Workisto</h1>
        <p className="mt-4 text-gray-600">
          Your platform for connecting with skilled professionals.
        </p>
      </div>
    </div>
  );
};

export default HomePage;
