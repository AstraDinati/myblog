// script.js

function toggleTagsCloud() {
    var tagCont = document.querySelector('.tag-container');
    tagCont.classList.toggle('show');

    toggleMobileMenu();
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
