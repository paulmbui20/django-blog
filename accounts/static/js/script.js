document.addEventListener('DOMContentLoaded', (event) => {
    const htmlElement = document.documentElement;
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');

    // Set the default theme to dark if no setting is found in local storage
    const currentTheme = localStorage.getItem('theme') || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    htmlElement.setAttribute('data-bs-theme', currentTheme);
    themeIcon.classList.toggle('fa-moon', currentTheme === 'light');
    themeIcon.classList.toggle('fa-sun', currentTheme === 'dark');

    themeToggle.addEventListener('click', function () {
        const newTheme = htmlElement.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
        htmlElement.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        themeIcon.classList.toggle('fa-moon', newTheme === 'light');
        themeIcon.classList.toggle('fa-sun', newTheme === 'dark');
    });
});


function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: "smooth", // Smooth scrolling effect
  });
}
