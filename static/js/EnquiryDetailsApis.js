async function getEnqDetails()
{

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
            value += `<li>${post.name} - ${post.subject}</li> <button onclick="replyEmail('${post.email}')">Reply</button>`;
        });
        document.body.innerHTML = value;
    }

function replyEmail(email) {

    alert(email)

    }