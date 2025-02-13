<template>
  <div class="app-container">
    <Navbar @openModal="showLoginModal = true" />
    <Test v-if="showLoginModal" :showModal="showLoginModal" @close="showLoginModal = false" />
    <router-view />
  </div>
</template>

<script setup>
import { ref } from "vue";
import Navbar from "./components/Navbar.vue";
import Test from "./components/Test.vue";

const showLoginModal = ref(false);
</script>

<style>

.app-container {
  width: 100vw;
  height: 100vh;
  background-color: #282c34;
  color: black;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  margin: 0;
  padding: 0;
}

#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-family: Arial, sans-serif;
  width: 100%;
  height: 100%;
}
</style>
