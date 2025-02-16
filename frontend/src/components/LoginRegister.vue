<template>
  <Teleport to="body">
    <transition name="fade">
      <div v-if="showModal" class="modal-overlay" @click.self="$emit('close')">
        <div class="modal-content">
          <button @click="$emit('close')" class="close-btn">✕</button>

          <div class="tab-content">
            <h2>{{ isLoginMode ? 'Logowanie' : 'Rejestracja' }}</h2>

            <div v-if="isLoginMode" class="form-container">
              <input type="email" v-model="loginEmail" placeholder="Email" class="input-field" required>
              <input type="password" v-model="loginPassword" placeholder="Hasło" class="input-field" required>
              <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
              <button @click="handleLogin" class="submit-btn">Zaloguj się</button>
            </div>

            <div v-else class="form-container">
              <input type="email" v-model="registerEmail" placeholder="Email" class="input-field" required>
              <input type="text" v-model="firstName" placeholder="Imię" class="input-field" required>
              <input type="text" v-model="lastName" placeholder="Nazwisko" class="input-field" required>
              <input type="tel" v-model="phoneNumber" placeholder="Numer telefonu" class="input-field" required>
              <input type="password" v-model="registerPassword" placeholder="Hasło" class="input-field" required>
              <input type="password" v-model="confirmPassword" placeholder="Powtórz hasło" class="input-field" required>
              <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
              <button @click="handleRegister" class="submit-btn">Zarejestruj się</button>
            </div>

            <p class="toggle-mode">
              <span v-if="isLoginMode">
                Nie masz konta? <a href="#" @click.prevent="toggleMode" class="mode-link">Zarejestruj się</a>.
              </span>
              <span v-else>
                Masz konto? <a href="#" @click.prevent="toggleMode" class="mode-link">Zaloguj się</a>.
              </span>
            </p>
          </div>
        </div>
      </div>
    </transition>
  </Teleport>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/authStore';

defineProps(["showModal"]);
const emit = defineEmits(["close"]);

const authStore = useAuthStore();
const isLoginMode = ref(true);
const loginEmail = ref("");
const loginPassword = ref("");
const registerEmail = ref("");
const firstName = ref("");
const lastName = ref("");
const phoneNumber = ref("");
const registerPassword = ref("");
const confirmPassword = ref("");
const errorMessage = ref("");


const handleLogin = async () => {
  errorMessage.value = "";

  if (!loginEmail.value || !loginPassword.value) {
    errorMessage.value = "Wypełnij wszystkie pola!";
    return;
  }

  const result = await authStore.login(loginEmail.value, loginPassword.value);

  if (result === true) {
    emit("close");
  } else {
    errorMessage.value = result;
  }
};


const handleRegister = async () => {
  errorMessage.value = "";

  if (!registerEmail.value || !registerPassword.value || !confirmPassword.value || !firstName.value || !lastName.value || !phoneNumber.value) {
    errorMessage.value = "Wypełnij wszystkie pola!";
    return;
  }
  if (registerPassword.value !== confirmPassword.value) {
    errorMessage.value = "Hasła się nie zgadzają!";
    return;
  }

  const userData = {
    email: registerEmail.value,
    first_name: firstName.value,
    last_name: lastName.value,
    phone_number: phoneNumber.value,
    password: registerPassword.value,
    password2: confirmPassword.value,
  };

  const result = await authStore.register(userData);

  if (result === true) {
    emit("close");
  } else {
    errorMessage.value = result;
  }
};

const toggleMode = () => {
  isLoginMode.value = !isLoginMode.value;
};
</script>

<style>

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 12px;
  width: 350px;
  text-align: center;
  position: relative;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.close-btn {
  position: absolute;
  right: 15px;
  top: 15px;
  border: none;
  background: none;
  font-size: 20px;
  cursor: pointer;
}

.submit-btn {
  padding: 10px;
  width: 100%;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s;
}

.submit-btn:hover {
  background: #0056b3;
}

.toggle-mode {
  margin-top: 20px;
  font-size: 14px;
  color: #666;
}

.form-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.input-field {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
  outline: none;
  transition: border-color 0.3s ease;
}

.input-field:focus {
  border-color: #007bff;
}

.mode-link {
  color: #007bff;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s ease;
}

.mode-link:hover {
  color: #0056b3;
}

.error-message {
  color: red;
  font-size: 14px;
  margin-top: 10px;
}
</style>

