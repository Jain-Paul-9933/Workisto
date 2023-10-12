import { createContext, useEffect, useState } from "react";
import jwt_decode from "jwt-decode";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { setUser, clearUSer } from "../slices/userSlice";

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
  const navigate = useNavigate();

  const dispatch = useDispatch();

  const apiUrl = "http://127.0.0.1:8000";

  const registerUser = async (formData) => {
    try {
      const response = await axios.post(
        `${apiUrl}/authentication/user_registration/`,
        formData
      );
      console.log("User Registion success", response.data);
      if (response.data.is_staff === false)
        navigate("/user_login");
      else
        navigate("/worker_login")
    } catch (error) {
      console.error("User Registion failed", error);
      navigate("/user_registration");
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
      console.log("Here is the response");
      dispatch(setUser(jwt_decode(response.data.access).user));
      axios.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${response.data.access}`;
      console.log("Login Succssfull");
      if (response.data.is_staff === false && response.data.is_superuser === false )
        navigate("/");
      else if (response.data.is_staff === true && response.data.is_superuser === false )
        navigate("/worker")
      else
        navigate("/admin")
    } catch (error) {
      console.error("Login Failed");
      dispatch(clearUSer());
      navigate("/user_login");
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
