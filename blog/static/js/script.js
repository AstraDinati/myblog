// script.js
function toggleTagsCloud() {
    var tagCont = document.querySelector('.tag-container');
    tagCont.classList.toggle('show');

    toggleMobileMenu();
}

document.addEventListener('DOMContentLoaded', (event) => {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    const themeColorMetaTag = document.querySelector('meta[name="theme-color"]');

    document.documentElement.setAttribute('data-theme', savedTheme);

    // Установка соответствующего цвета мета-тега theme-color
    if (savedTheme === 'dark') {
        themeColorMetaTag.setAttribute('content', '#1f1f1f');
    } else {
        themeColorMetaTag.setAttribute('content', '#ffffff');
    }
});


function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    const themeColorMetaTag = document.querySelector('meta[name="theme-color"]');

    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    console.log("Тема изменена на: " + newTheme);

    // Изменение цвета мета-тега theme-color в зависимости от темы
    if (newTheme === 'dark') {
        themeColorMetaTag.setAttribute('content', '#1f1f1f'); // Тёмный цвет для тёмной темы
    } else {
        themeColorMetaTag.setAttribute('content', '#ffffff'); // Светлый цвет для светлой темы
    }
}


function toggleMobileMenu() {
    var navMenu = document.querySelector('.nav-menu');
    navMenu.classList.toggle('show-mobile');
}

// Добавляем слушатель событий для закрытия меню при клике вне его пределов
document.addEventListener('click', function (event) {
    var navMenu = document.querySelector('.nav-menu');
    var targetElement = event.target;

    // Проверяем, является ли кликнутый элемент частью бургера или меню
    var isClickInsideBurger = targetElement.closest('.header-burger');
    var isClickInsideMenu = targetElement.closest('.nav-menu');

    if (!isClickInsideBurger && !isClickInsideMenu) {
        // Закрываем меню, если клик был вне его пределов
        navMenu.classList.remove('show-mobile');
    }
});

document.addEventListener('click', function (event) {
    var tagCont = document.querySelector('.tag-container');
    var targetElement = event.target;

    if (!tagCont) {
        return;
    }

    var isClickInsideTagList = targetElement.closest('.tag-list');
    var isClickInsideContainer = targetElement.closest('.tag-container');

    // Проверяем, существует ли класс 'show' у элемента
    if (tagCont.classList && tagCont.classList.contains('show') && !isClickInsideTagList && !isClickInsideContainer) {
        tagCont.classList.remove('show');
    }
});