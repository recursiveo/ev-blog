var userobj ={
    email:'',
    name:'',
    password:''
}
function userData(name,email,password)
{
    debugger;
    console.log("hiiiiiiiiii")
    userobj.name = name;
    userobj.email = email;
    userobj.password = password;
    debugger;
    console.log(userobj)
    //send_mail()
    register_details()
}

async function register_details()
{
    debugger;
    let response = await fetch('/signup/',
    {
      method:"POST",
      headers: {"Content-type": "application/json; charset=UTF-8"},
      body: JSON.stringify({userobj})
    })
    if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        let json = await response.json();
        console.log(json +'response')
      } else {
        alert("HTTP-Error: " + response.status);
      }
}
