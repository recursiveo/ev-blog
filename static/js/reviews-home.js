"use strict";

let id_to_edit = "";

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

function check_id(){
    let id = $('id').value;
    id_to_edit = id;
    fetch('/check_id', {
        method: 'POST',
        headers: {"Content-type": "application/json"},
        body: JSON.stringify(id)
    }).then(
        data=>{return data.json();}
    ).then(
        res=>{
            if(res !== "NULL"){
                $('review').disabled = false;
                $('review').value = res;

                $('submit-review').disabled = false;
            }else {
                console.log(res);
            }
        }
    )
    // if(res && res.ok){
    //     let json = res.json();
    //     console.log(json);
    // }else{
    //     console.log("Error" + res.status);
    // }
}

function edit_review(){
    let id = id_to_edit;
    let review_text = $('review').value;
    console.log(review_text);
    fetch('/modify_review',{
        method: 'POST',
        headers: { 'Content-type': 'application/json'},
        body: JSON.stringify({uid : id, review_text : review_text})
    }).then(
        data=> {return data.json();}
    ).then(
        res => {
            console.log(res);
        }
    )
}