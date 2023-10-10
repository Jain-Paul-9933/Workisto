import { createContext, useEffect, useState } from "react";
import jwt_decode from "jwt-decode";
import axios from "axios";

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
  const apiUrl = "http://127.0.0.1:8000";

  const registerUser = async (formData) => {
    try {
      const response = await axios.post(
        `${apiUrl}/authentication/user_registration/`,
        formData
      );
      console.log("User Registion call was success", response.data);
    } catch (error) {
      console.error("User Registion call was failed", error);
    }
  };

  const loginUser = async (formData) => {
    try {
      const response = await axios.post(
        `${apiUrl}/authentication/auth_token/`,
        formData,
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        }
      );

      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);

      axios.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${response.data.access}`;
      console.log("Login Succssfull");
    } catch (error) {
      console.error("Login Failed");
    }
  };

  const contextData = {
    registerUser,
    loginUser,
  };

  return (
    <AuthContext.Provider value={contextData}>{children}</AuthContext.Provider>
  );
};
