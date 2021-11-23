async function getEnqDetails()
{
     document.getElementById("loader").style.display="block";

    let response = await fetch('/get_contact_us/')
    debugger;
    var data ="";
    if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        let json = await response.json();
        debugger;
        ngForFunctionality(json)
        for(var i=0 ;i<json.length;i++)
        {
            data+=JSON.stringify(json[i])+"<br>"
        }
        document.getElementById("loader").style.display="none";
        console.log(json)
      } else {
        alert("HTTP-Error: " + response.status);
      }
    // ngForFunctionality(data)
    //document.getElementById("enqDetail").innerHTML = data;
}


function ngForFunctionality(anArray) {
    debugger;
        let value = '';
        anArray.forEach((post) => {
            value += `<br><li>Name : ${post.name} </li> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Subject : ${post.subject}<br>
            <textarea cols="50" rows="4"  id='${post._id}' value=""></textarea><br>
            <button class="button1" onclick="deleteQuery('${post._id}')">Delete</button>
            <button class="button2" onclick="replyEmail('${post.email}','${post._id}',document.getElementById('${post._id}').value)">Reply</button> <br><br> `;
        });
        document.getElementById("enqDetail").innerHTML = value;

    }

async function replyEmail(email,id,replyText) {
    debugger;
    console.log(email)
    document.getElementById("loader").style.display="block";
    var obj = {'email':email , 'id':id , 'reply': replyText}
    let response = await fetch('/updateReply/',
    {
      method:"POST",
      headers: {"Content-type": "application/json; charset=UTF-8"},
      body: JSON.stringify({email,id,replyText})
    })
    if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        let json = await response.json();
        console.log(json +'response')
        sendReplyEmail(email,id,replyText)
      } else {
        alert("HTTP-Error: " + response.status);
      }



    }


async function sendReplyEmail(email,id,replyText) {

    let response = await fetch('/send-mail/',
        {
          method:"POST",
          headers: {"Content-type": "application/json; charset=UTF-8"},
          body: JSON.stringify({email,id,replyText})
        })
        if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        let json = await response.json();
        console.log(json +'response')
        getEnqDetails()
      } else {
        alert("HTTP-Error: " + response.status);
      }

}


async function deleteQuery(docId) {

    document.getElementById("loader").style.display="block";
    let response = await fetch('/deleteDocument/',
    {
      method:"POST",
      headers: {"Content-type": "application/json; charset=UTF-8"},
      body: JSON.stringify({docId})
    })
    if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        let json = await response.json();
        console.log(json +'response')
        getEnqDetails()
      } else {
        alert("HTTP-Error: " + response.status);
      }

    }
