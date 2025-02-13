<script>
import axios from "axios";

export default {
  name: "AppVue",
  data() {
    return {
      email: "",
      first_name: "",
      last_name:"",
      phone_number: "",
      password: "",
      passwordVerify: "",
      errorMessage: "",
      successMessage: "",
    };
  },
  methods: {
    async submitForm() {
      if (this.password !== this.passwordVerify) {
        this.errorMessage = "Hasła nie są identyczne!";
        return;
      }

      this.errorMessage = "";
      this.successMessage = "";

      try {
        // Wysyłanie żądania POST do API
        const response = await axios.post("http://localhost/api/register", {
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name,
          phone_number: this.phone_number,
          password: this.password,
        });

        if (response.data.success) {
          this.successMessage = "Rejestracja udana!";
          this.email = "";
          this.firstName = "";
          this.password = "";
          this.passwordVerify = "";
        } else {
          this.errorMessage = response.data.message || "Błąd rejestracji!";
        }
      } catch (error) {
        // Obsługa błędów (np. błąd serwera)
        this.errorMessage =
          error.response?.data?.message || "Wystąpił błąd, spróbuj ponownie.";
      }
    },
  },
};
</script>

<template>
  <div class="register_box">
    <h1>Rejestracja</h1>
    <form @submit.prevent="submitForm">
      <label>
        Email address
        <input type="email" v-model="email" required />
      </label>

      <label>
        first name
        <input type="text" v-model="first_name" required />
      </label>

      <label>
        last name
        <input type="text" v-model="last_name" required>

      </label>

      <label>
        phone number
        <input type="text" v-model="phone_number">
      </label>

      <label>
        Password
        <input type="password" v-model="password" required />
      </label>

      <label>
        Verify Password
        <input type="password" v-model="passwordVerify" required />
      </label>

      <button type="submit">Sign up</button>
      <button type="button">Have account, login here</button>

      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      <p v-if="successMessage" class="success">{{ successMessage }}</p>
    </form>
  </div>
</template>

<style scoped>
.register_box {
  width: 300px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f9f9f9;
}

label {
  display: block;
  margin-bottom: 10px;
}

input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  width: 100%;
  padding: 10px;
  margin-top: 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  font-size: 14px;
  margin-top: 10px;
}

.success {
  color: green;
  font-size: 14px;
  margin-top: 10px;
}
</style>
