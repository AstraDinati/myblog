// script.js

function toggleMobileMenu() {
    var navMenu = document.querySelector('.nav-menu');
    var socLin = document.querySelector('.social-links');
    navMenu.classList.toggle('show-mobile');
    socLin.classList.toggle('show-mobile');
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

function toggleTagsCloud() {
    var tagCont = document.querySelector('.tag-container');
    tagCont.classList.toggle('show-mobile');

    toggleMobileMenu();
}

// Добавьте следующий код для закрытия панели тегов при клике за её пределами
document.addEventListener('click', function (event) {
    var tagCont = document.querySelector('.tag-container');
    var targetElement = event.target; // Кликнутый элемент

    // Проверяем, является ли кликнутый элемент кнопкой для открытия панели тегов
    if (targetElement.classList.contains('nav-link') && targetElement.textContent.trim() === 'Tags') {
        return;
    }

    // Проверяем, является ли кликнутый элемент частью панели тегов
    if (!tagCont.contains(targetElement)) {
        // Если не является, закрываем панель тегов
        tagCont.classList.remove('show-mobile');
    }
});
