import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import UserRegistration from "./components/user/UserRegistration";
import UserLogin from "./components/user/UserLogin";
import UserHomePage from "./components/user/UserHomePage";
import WorkerRegistration from "./components/worker/WorkerRegistration";
import WorkerLogin from "./components/worker/WorkerLogin";
import WorkerHomePage from "./components/worker/WorkerHomePage";
import AdminLogin from "./components/admin/AdminLogin";
import AdminHomePage from "./components/admin/AdminHomePage";
import { AuthProvider } from "./context/AuthContext";

const App = () => {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/user_registration" element={<UserRegistration />} />
          <Route path="/user_login" element={<UserLogin />} />
          <Route exact path="/" element={<UserHomePage/>} />
          <Route path="/worker_registration" element={<WorkerRegistration />} />
          <Route path="/worker_login" element={<WorkerLogin />} />
          <Route path="/worker" element={<WorkerHomePage/>} />
          <Route path="/admin_login" element={<AdminLogin/>}/>
          <Route path="/admin" element={<AdminHomePage/>}/>
        </Routes>
      </AuthProvider>
    </Router>
  );
};

export default App;
