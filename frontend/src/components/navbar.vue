<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">MojaFirma</router-link>

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Strona główna</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/shop">Oferta</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/reservation">Cennik</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/appointment">Zarezerwuj wizytę</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/contact">Kontakt</router-link>
          </li>
        </ul>

        <div class="auth-buttons">

            <router-link v-if="authStore.isAuthenticated" class="nav-profile" to="/profile">Profil</router-link>

          <button v-if="authStore.isAuthenticated" class="btn btn-outline-danger" @click="handleLogout">
            Wyloguj
          </button>

          <button v-else class="btn btn-outline-primary" @click="handleLoginModal">
            Zaloguj
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useAuthStore } from "@/stores/authStore";
import { computed } from "vue";

const authStore = useAuthStore();
const emit = defineEmits(["openModal"]);


const handleLoginModal = () => {
  emit("openModal");
};


const handleLogout = () => {
  authStore.logout();
};
</script>

<style scoped>
.navbar {
  width: 100%;
  padding: 10px 20px;
  background: #fff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.navbar-nav {
  display: flex;
  gap: 15px;
}

.collapse {
  display: flex;
  justify-content: space-between;
  width: 100%;
  align-items: center;
}

.auth-buttons {
  display: flex;
  gap: 10px;
}

button {
  margin-left: auto;
}

.navbar-brand {
  font-weight: bold;
  font-size: 1.2rem;
}

.nav-link {
  font-size: 16px;
  font-weight: 500;
  transition: color 0.3s ease-in-out;
}

.nav-link:hover {
  color: #007bff;
}

.nav-profile {
  display: flex;
  font-size: 16px;
  font-weight: 500;
  transition: color 0.3s ease-in-out;
  text-decoration: none;
  text-align: center;
}

.nav-profile:hover {
    color: #007bff;

}

@media (max-width: 768px) {
  .navbar {
    padding: 10px;
  }

  .auth-buttons {
    width: 100%;
    justify-content: center;
    margin-top: 10px;
  }
}
</style>
