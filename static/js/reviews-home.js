"use strict";

let id_to_edit = "";
let id_to_del = "";

function $(id) {
    return document.getElementById(id);
}

let submit_review = async () => {
    let review = {
        name: 'username',
        brand: $('car-brand').value,
        model: $('car-model').value,
        review_text: $('review').value
    };
    console.log(review)
    $('msg_area').innerHTML = "Please wait...";
    $('submit-review').disabled = true;
    $('car-brand').disabled = true;
    $('car-model').disabled = true;
    $('review').disabled = true;
    let res = await fetch('/submit-review', {
        method: 'POST',
        headers: {"Content-type": "application/json"},
        body: JSON.stringify(review)
        //{"Content-type": "application/json; charset=UTF-8"},
    });
    if (res && res.ok) {
        let json = res.json();
        console.log(json);
        $('msg_area').innerHTML = "";
        alert("*** Review Posted ***");
        $('submit-review').disabled = false;
        $('car-brand').disabled = false;
        $('car-model').disabled = false;
        $('review').disabled = false;
    } else {
        console.log("Error : " + res.status);
    }
}

let goto_reviews = () => {

    // $('show-reviews').onclick = function () {
    //     location.href = '/reviews';
    // }
    let brand = $('car').value;
    let url_string = '/reviews?brand='+brand
    fetch(url_string).then(
        response => {
            return response.text();
        }
    ).then(
        res => {
            document.body.innerHTML = res;
        }
    )
}

function goto_add_review(){
    location.href = '/add-review';
}

function goto_edit_review(){
    location.href = '/edit-review';
}

function goto_delete_review(){
    location.href = '/delete-review';
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
                 $('review').disabled = true;
                 $('review').value = "Invalid review ID. Please enter valid id.";
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
    $('submit-review').disabled = true;
    $('msg_area').innerHTML = "Please wait...";

    fetch('/modify_review',{
        method: 'POST',
        headers: { 'Content-type': 'application/json'},
        body: JSON.stringify({uid : id, review_text : review_text})
    }).then(
        data=> {return data.json();}
    ).then(
        res => {
            console.log(res);
            $('msg_area').innerHTML = "";
            alert("*** Your review changes are posted ***");
            $('submit-review').disabled = false;

        }
    )
}

function delete_review(){
    console.log(id_to_del)
    $('delete_review').disabled = true;
    $('msg_area').innerHTML = "Please wait...";
    fetch('/delete_review', {
        method: 'POST',
        headers: {'Content-type' : 'application/json'},
        body: JSON.stringify({uid: id_to_del})
    }).then(
        data => {
            return data.json();
        }
    ).then(res => {
        console.log(res);
        $('msg_area').innerHTML = "";
         alert("*** Review Deleted ***");

          $('delete_review').disabled = false;
        }
    )
}

function check_id_to_delete(){
    let id = $('id_to_del').value;
    console.log(id);
    id_to_del = id;
    fetch('/check_id', {
        method: 'POST',
        headers: {"Content-type": "application/json"},
        body: JSON.stringify(id)
    }).then(
        data=>{return data.json();}
    ).then(
        res=>{
            if(res !== "NULL"){
                $('review').value = res;
                $('delete_review').disabled = false;
            }else {
                 $('review').disabled = true;
                 $('review').value = "Invalid review ID. Please enter valid id.";
                 $('delete_review').disabled = true;
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