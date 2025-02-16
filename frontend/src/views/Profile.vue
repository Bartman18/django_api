<template>
  <div class="container">
    <div class="main-body">
      <div class="row gutters-sm">
        <div class="col-md-4 mb-3">
          <div class="card">
            <div class="card-body text-center">
              <img src="https://bootdey.com/img/Content/avatar/avatar7.png" alt="Użytkownik" class="rounded-circle profile-img">
              <div class="mt-3">
                <h4>{{ userData.first_name || "Klient Detailingowy" }}</h4>
                <p class="text-secondary mb-1">{{ userData.role || "Klient" }}</p>
                <p class="text-muted font-size-sm">{{ userData.address || "Brak adresu" }}</p>
                <button class="btn btn-primary" @click="openEditModal">Edytuj profil</button>
                <button class="btn btn-outline-danger" @click="logout">Wyloguj</button>
              </div>
            </div>
          </div>

          <!-- Contact Info -->
          <div class="card mt-3">
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <h6>Email:</h6>
                <span class="text-secondary">{{ userData.email || "Nie podano" }}</span>
              </li>
              <li class="list-group-item">
                <h6>Telefon:</h6>
                <span class="text-secondary">{{ userData.phone_number || "Nie podano" }}</span>
              </li>

            </ul>
          </div>
        </div>

        <div class="col-md-8">
          <div class="card mb-3">
            <div class="card-body">
              <h5 class="mb-4"><i class="fas fa-car"></i> Ostatnie usługi detailingowe</h5>
              <ul class="list-group">
                <li v-for="service in userData.last_services" :key="service.id" class="list-group-item">
                  <strong>{{ service.name }}</strong> - {{ service.date }}
                </li>
                <li v-if="!userData.last_services?.length" class="list-group-item text-muted">Brak wykonanych usług.</li>
              </ul>
            </div>
          </div>

          <div class="card mb-3">
            <div class="card-body">
              <h5 class="mb-4"><i class="fas fa-shopping-cart"></i> Historia zamówień</h5>
              <ul class="list-group">
                <li v-for="order in userData.orders" :key="order.id" class="list-group-item">
                  <strong>Zamówienie #{{ order.id }}</strong> - {{ order.date }} ({{ order.status }})
                </li>
                <li v-if="!userData.orders?.length" class="list-group-item text-muted">Brak zamówień.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <UserDataModal
      :showModal="showEditModal"
      :userData="userData"
      @close="showEditModal = false"
      @save="handleSaveUserData"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useRouter } from "vue-router";
import UserDataModal from "@/components/UserDataModal.vue";

const router = useRouter();
const userData = ref({});
const showEditModal = ref(false);

const fetchUserData = async () => {
  try {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) {
      router.push("/login");
      return;
    }

    const response = await fetch("http://127.0.0.1:8000/api/user/", {
      headers: {Authorization: `Bearer ${accessToken}`},
    });

    if (response.ok) {
      userData.value = await response.json();
    } else {
      console.error("Błąd pobierania danych użytkownika.");
    }
  } catch (error) {
    console.error("Błąd połączenia z API", error);
  }
};

const openEditModal = () => {
  showEditModal.value = true;
};

const handleSaveUserData = async (updatedData) => {
  try {
    const accessToken = localStorage.getItem("access_token");
    const response = await fetch("http://127.0.0.1:8000/api/user/", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
      },
      body: JSON.stringify(updatedData),
    });

    if (response.ok) {
      userData.value = await response.json();
      alert("Dane użytkownika zostały zaktualizowane!");
    } else {
      console.error("Błąd aktualizacji danych użytkownika.");
    }
  } catch (error) {
    console.error("Błąd połączenia z API", error);
  }
};

const logout = () => {
  localStorage.removeItem("access_token");
  router.push("/");
};



onMounted(fetchUserData);
</script>

<style scoped>
</style>
