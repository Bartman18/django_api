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
              <button @click="handleLogin" class="submit-btn">Zaloguj się</button>
            </div>

            <div v-else class="form-container">
              <input type="email" v-model="registerEmail" placeholder="Email" class="input-field" required>
              <input type="password" v-model="registerPassword" placeholder="Hasło" class="input-field" required>
              <input type="password" v-model="confirmPassword" placeholder="Powtórz hasło" class="input-field" required>
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

defineProps(["showModal"]);
const emit = defineEmits(["close"]);

const isLoginMode = ref(true);
const loginEmail = ref("");
const loginPassword = ref("");
const registerEmail = ref("");
const registerPassword = ref("");
const confirmPassword = ref("");

const handleLogin = () => {
  if (!loginEmail.value || !loginPassword.value) {
    alert("Proszę wypełnić wszystkie pola!");
    return;
  }
  alert(`Logowanie: ${loginEmail.value}`);
  emit("close");
};

const handleRegister = () => {
  if (!registerEmail.value || !registerPassword.value || !confirmPassword.value) {
    alert("Proszę wypełnić wszystkie pola!");
    return;
  }
  if (registerPassword.value !== confirmPassword.value) {
    alert("Hasła się nie zgadzają!");
    return;
  }
  alert(`Rejestracja: ${registerEmail.value}`);
  emit("close");
};

const toggleMode = () => {
  isLoginMode.value = !isLoginMode.value;
};
</script>

<style>
/* Modal CSS */
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
  gap : 15px;

}
.input-field {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
  outline: none;
  transition: border-color 0.3s ease;
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

</style>
