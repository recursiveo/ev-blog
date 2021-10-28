"use strict";

function $(id) {
    return document.getElementById(id);
}

var submit_review = async () => {
    var review = {
        name: 'username',
        brand: $('car-brand').value,
        model: $('car-model').value,
        review_text: $('review').value
    };
    console.log(review)
    var res = await fetch('/submit-review', {
        method: 'POST',
        headers: {"Content-type": "application/json"},
        body: JSON.stringify(review)
        //{"Content-type": "application/json; charset=UTF-8"},
    });
    if (res && res.ok) {
        let json = res.json();
        console.log(json);
    } else {
        console.log("Error : " + res.status);
    }
}

var goto_reviews = () => {

    $('show-reviews').onclick = function () {
        location.href = '/reviews';
    }
}

function goto_add_review(){
    location.href = '/add-review';
}

function goto_edit_review(){
    location.href = '/edit-review';
}