"use strict";

window.onload = function () {
    console.log("DOM ready");
//    $('.basket_record').on('click', '.product_price', function (event) {
//        console.log("target:", event.target);
//    })
    let categoryNames = document.querySelectorAll('input[type=number]');
    categoryNames.forEach(function (item) {
       item.onchange = function (event) {
       let qty = event.target.value
       let pk = event.target.name
       console.log("qty:", qty, ", pk" , pk);
       }
    })
}
