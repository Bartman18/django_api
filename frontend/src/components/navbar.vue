<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>

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
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/shop">Shop</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/reservation">Reservation</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/dashboard">Panel</router-link>
          </li>
        </ul>

        <!-- Przycisk Zaloguj po prawej stronie -->
        <button class="btn btn-outline-primary" @click="$emit('openModal')">
          Zaloguj
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup>
defineEmits(["openModal"]);
</script>

<style scoped>
/* Stylizacja Navbar */
.navbar {
  width: 100%;
  padding: 10px 20px;
}

/* Flexbox dla nawigacji */
.navbar-nav {
  display: flex;
  gap: 15px; /* Odstępy między elementami */
}

/* Wyrównanie przycisku "Zaloguj" do prawej */
.collapse {
  display: flex;
  justify-content: space-between;
  width: 100%;
  align-items: center;
}

button {
  margin-left: auto; /* Przesuwa przycisk "Zaloguj" maksymalnie w prawo */
}
</style>
