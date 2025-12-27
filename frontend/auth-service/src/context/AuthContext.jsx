import React, { createContext, useState, useEffect } from "react";
import axios from "axios";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    if (storedToken) {
      setToken(storedToken);
      axios.defaults.headers.common["Authorization"] = `Bearer ${storedToken}`;
    }
    setLoading(false);
  }, []);

  const login = async (email, password) => {
    try {
      const params = new URLSearchParams({
        email,
        password,
        is_active: "true",
        is_superuser: "false",
        is_verified: "false",
      });

      const response = await axios.post(
        `http://localhost:8000/api/auth/login?${params.toString()}`,
        {},
        { headers: { Accept: "application/json" } },
      );

      const access_token = response.data.access_token || response.data.token;
      setToken(access_token);
      localStorage.setItem("token", access_token);
      axios.defaults.headers.common["Authorization"] = `Bearer ${access_token}`;
      return true;
    } catch (error) {
      console.error("Login failed:", error);
      return false;
    }
  };

  const register = async (email, password) => {
    try {
      const params = new URLSearchParams({
        email,
        password,
        is_active: "true",
        is_superuser: "false",
        is_verified: "false",
      });

      await axios.post(
        `http://localhost:8000/api/auth/register?${params.toString()}`,
        {},
        { headers: { Accept: "application/json" } },
      );
      return true;
    } catch (error) {
      console.error("Register failed:", error);
      return false;
    }
  };

  const logout = () => {
    setToken(null);
    localStorage.removeItem("token");
    delete axios.defaults.headers.common["Authorization"];
  };

  return (
    <AuthContext.Provider value={{ token, login, register, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
