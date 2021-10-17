'use strict';

let burgerItem = document.querySelector('a.show-hide-sidemenu');
let sideMenu = document.querySelector('div.sidemenu')
burgerItem.addEventListener('click', function(event) {
    event.preventDefault();
    sideMenu.classList.toggle('hidden');
    event.target.parentElement.classList.toggle('active')
})