  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');
  
  navToggle.addEventListener('click', () => {
      navMenu.classList.toggle('nav-menu-visible');
      navToggle.classList.toggle('nav-toggle-active');
  });