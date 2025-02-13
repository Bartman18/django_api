<script setup>
import { ref } from "vue";
import axios from "axios";

// Reaktywne dane
const email = ref("");
const password = ref("");
const errorMessage = ref("");
const successMessage = ref("");

// Funkcja do logowania
const login = async () => {
  try {
    const response = await axios.post("http://localhost/api/login", {
      email: email.value,
      password: password.value,
    });

    if (response.data.success) {
      successMessage.value = "Logowanie udane!";
      errorMessage.value = "";
      email.value = "";
      password.value = "";
    } else {
      errorMessage.value = response.data.message || "Błąd logowania!";
      successMessage.value = "";
    }
  } catch (error) {
    errorMessage.value =
      error.response?.data?.message || "Wystąpił błąd, spróbuj ponownie.";
    successMessage.value = "";
  }
};
</script>

<template>
  <div class="login-box">
    <form @submit.prevent="submitForm">
      <label>
        Email
        <input type="email" v-model="email">
      </label>

      <label>
        Password
        <input type="password" v-model="password">
      </label>

      <button type="submit">Login</button>



    </form>

  </div>
</template>

<style scoped>
<style scoped>
.login_box {
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
