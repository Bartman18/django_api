<template>
  <Teleport to="body">
    <transition name="fade">
      <div v-if="showModal" class="modal-overlay" @click.self="$emit('close')">
        <div class="modal-content">
          <button @click="$emit('close')" class="close-btn">✕</button>
          <h2>Edytuj dane użytkownika</h2>

          <div class="form-container">
            <input
              type="text"
              v-model="localUserData.first_name"
              placeholder="Imię"
              class="input-field"
            />
            <input
              type="text"
              v-model="localUserData.last_name"
              placeholder="Nazwisko"
              class="input-field"
            />
            <input
              type="email"
              v-model="localUserData.email"
              placeholder="Email"
              class="input-field"
            />
            <input
              type="tel"
              v-model="localUserData.phone_number"
              placeholder="Numer telefonu"
              class="input-field"
            />
          </div>

          <button @click="saveChanges" class="submit-btn">Zapisz zmiany</button>
        </div>
      </div>
    </transition>
  </Teleport>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps({
  showModal: Boolean,
  userData: Object,
});

const emit = defineEmits(["close", "save"]);

const localUserData = ref({ ...props.userData });

watch(
  () => props.userData,
  (newData) => {
    localUserData.value = { ...newData };
  },
  { deep: true }
);


const saveChanges = () => {
  emit("save", localUserData.value);
  emit("close");
};
</script>

<style scoped>
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
  padding: 20px;
  border-radius: 8px;
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

.form-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 20px;
}

.input-field {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 16px;
  outline: none;
  transition: border-color 0.3s ease;
}

.input-field:focus {
  border-color: #007bff;
}
</style>
