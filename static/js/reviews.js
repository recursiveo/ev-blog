function $(id) {
    return document.getElementById(id)
}

fetch('/reviews-get-data').then(
    function (res) {
        return res.json()
    }).then(function (res) {
    console.log(res);
    res.forEach(item => {

    })
    // $('user').innerText = res.username;
    // $('brand').innerText = res.post_id;
    // $('model').innerText = res.post_id;
    // $('data').innerText = res.data;
})