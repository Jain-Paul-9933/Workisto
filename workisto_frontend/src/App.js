import React from "react";
import UserRegistration from "./components/user/UserRegistration";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import UserLogin from "./components/user/UserLogin";
import HomePage from "./components/user/HomePage";
import { AuthProvider } from "./context/AuthContext";

const App = () => {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/user_registration" element={<UserRegistration />} />
          <Route path="/user_login" element={<UserLogin />} />
          <Route path="/" element={<HomePage />} />
        </Routes>
      </AuthProvider>
    </Router>
  );
};

export default App;
