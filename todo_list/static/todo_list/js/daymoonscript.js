"use strict";



document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#nd').onclick = function() {
        let content_color = document.querySelector('.content'), lchapter_color = document.querySelector('.left-chapter'), rchapter_color = document.querySelector('.right-chapter');
        if (content_color.style.background === "whitesmoke") {content_color.style.background = "black", htmlcolor.style.color = 'white', lchapter_color.style.background = 'grey', rchapter_color.style.background = 'grey', lchapter_color.style.color = 'gold', rchapter_color.style.color = 'gold';}

        else {content_color.style.background = "whitesmoke", content_color.style.color = 'black', lchapter_color.style.background = 'wheat', rchapter_color.style.background = 'wheat', lchapter_color.style.color = 'white', rchapter_color.style.color = 'white';};
    };
});

