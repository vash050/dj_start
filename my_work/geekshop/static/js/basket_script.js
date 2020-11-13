"use strict";

window.onload = function () {
    console.log("DOM ready");
    $('.product_price').on('click', function (event) {
        console.log("target:" + event.target);
    })
}
