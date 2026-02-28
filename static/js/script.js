function toggleTheme() {
    const htmlElement = document.documentElement;
    const currentTheme = htmlElement.getAttribute('data-theme');
    const themeIcon = document.getElementById('theme-icon');

    if (currentTheme === 'dark') {
        // Переключаем на светлую тему
        htmlElement.removeAttribute('data-theme');
        themeIcon.textContent = '🌙';
        localStorage.setItem('theme', 'light');
    } else {
        // Переключаем на темную тему
        htmlElement.setAttribute('data-theme', 'dark');
        themeIcon.textContent = '☀️';
        localStorage.setItem('theme', 'dark');
    }
}

// Функция для установки начальной темы
function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    const htmlElement = document.documentElement;
    const themeIcon = document.getElementById('theme-icon');

    if (savedTheme === 'dark') {
        htmlElement.setAttribute('data-theme', 'dark');
        themeIcon.textContent = '☀️';
    } else {
        htmlElement.removeAttribute('data-theme');
        themeIcon.textContent = '🌙';
    }
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    initTheme();

    // Назначаем обработчик клика на кнопку
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', toggleTheme);
    }
});
