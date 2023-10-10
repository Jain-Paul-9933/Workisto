import React from "react";
import UserRegistration from "./components/UserRegistration";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import UserLogin from "./components/UserLogin";
import HomePage from "./components/HomePage";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/user_registration" element={<UserRegistration />} />
        <Route path="/user_login" element={<UserLogin/>}/>
        <Route path="/" element={<HomePage/>}/>
      </Routes>
    </Router>
  );
};

export default App;
