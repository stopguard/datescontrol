'use strict';

let $deleteItems = document.querySelectorAll('a.del-item');
$deleteItems.forEach(item => {
    item.addEventListener('click', function (event) {
        event.preventDefault();
        document.querySelector(`div.${event.target.id}`).classList.toggle('hidden');
    });
});
