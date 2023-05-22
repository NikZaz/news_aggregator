document.addEventListener('DOMContentLoaded', function() {
    var menuItems = document.querySelectorAll('.nav__menu-item');
    
    menuItems.forEach(function(item) {
      item.addEventListener('click', function() {
        menuItems.forEach(function(item) {
          item.classList.remove('active');
        });
        this.classList.add('active');
      });
    });
  });
  
  document.querySelector('.header__menu-login-link').addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector('#login-modal').style.display = "block";
  });
  
  document.querySelector('.close').addEventListener('click', function(e) {
    document.querySelector('#login-modal').style.display = "none";
  });
  
  document.querySelector('#register-tab').addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector('#login-form').style.display = "none";
    document.querySelector('#register-form').style.display = "block";
  });
  
  document.querySelector('#login-tab').addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector('#login-form').style.display = "block";
    document.querySelector('#register-form').style.display = "none";
  });
