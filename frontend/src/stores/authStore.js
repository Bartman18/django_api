import { defineStore } from 'pinia';
import router from "@/router/index.js";
import Home from "@/views/Home.vue";

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    isAuthenticated: !!localStorage.getItem("access_token"),
    accessToken: localStorage.getItem("access_token") || null,


  }),

  actions: {
    async login(email, password) {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/token/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password }),
        });

        const data = await response.json();

        if (response.ok) {
          localStorage.setItem("access_token", data.access);
          localStorage.setItem("refresh_token", data.refresh);
          this.accessToken = data.access;
          this.isAuthenticated = true;

          await this.getUserData();
          return true;
        } else {
          return data.message || "Błąd logowania";
        }
      } catch (error) {
        return "Błąd połączenia z serwerem";
      }
    },

    async register(userData) {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/register/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(userData),
        });

        const data = await response.json();

        if (response.ok) {
          localStorage.setItem("access_token", data.access);
          localStorage.setItem("refresh_token", data.refresh);
          this.accessToken = data.access;
          this.isAuthenticated = true;
          return true;
        } else {
          return data.message || "Błąd rejestracji";
        }
      } catch (error) {
        return "Błąd połączenia z serwerem";
      }
    },

    async getUserData() {
      try {
        const token = localStorage.getItem("access_token");

        if (!token) {
          this.user = null;
          this.isAuthenticated = false;

          return;
        }

        const response = await fetch("http://127.0.0.1:8000/api/user/", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        });

        const data = await response.json();

        if (response.ok) {
          this.user = data;
        } else {
          this.logout();
        }
      } catch (error) {
        console.error("Błąd pobierania danych użytkownika:", error);
        this.logout();
      }
    },

    logout() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      this.user = null;
      this.isAuthenticated = false;
      this.accessToken = null;
      router.push({ path: '/home' });

    },
  },
});
