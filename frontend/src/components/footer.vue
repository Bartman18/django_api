<script setup>

</script>

<template>
  <footer class="footer">
    <div class="footer___content">
      <div class="footer__info">
        <p class="footer__author">© 2025 Gandalf</p>
        <p class="footer__email">
          <a class="footer__email-link" href="mailto:test@test.com">
            <i class="fas fa-envelope"></i> test@test.com
          </a>
        </p>
      </div>

      <nav class="footer_nav">
        <router-link class="nav-link" to="/">O nas</router-link>
        <router-link class="nav-link" to="/">kontakt</router-link>

        <router-link class="nav-link" to="/">regulamin</router-link>


      </nav>

      <div class="footer__social">
        <a href="https://facebook.com" target="_blank" class="footer__social-link">
          <i class="fab fa-facebook-f"></i>
        </a>
        <a href="https://twitter.com" target="_blank" class="footer__social-link">
          <i class="fab fa-twitter"></i>
        </a>
        <a href="https://instagram.com" target="_blank" class="footer__social-link">
          <i class="fab fa-instagram"></i>
        </a>

      </div>








    </div>


  </footer>
</template>


<style scoped>
footer {
  width: 100%;
  position: fixed;
  left: 0;
  bottom: 0;
  text-align: center;
  padding: 3px;
  background-color: #f8f9fa;
  color: #212529;
  align-items: center;


}

.footer___content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  padding: 0 20px;
}


.footer__info {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer__author {
  margin: 0;
  font-size: 0.9rem;
}

.footer__email-link{
  text-decoration: none;
  color:black;

}

.footer__email-link:hover {
  color: #3498db
}


.footer__social {
  display: flex;
  justify-content: flex-end;
  gap: 20px;

}

.footer__social-link {
  color: inherit;
}


.footer__social-link:hover {
  color: #3498db;
}

.footer_nav {
  display: flex;
  flex-direction: row;
  gap: 10px;
  align-items: center;
}





</style>
