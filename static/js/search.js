var endpoint = 'http://127.0.0.1:8000/api/clients?search='
const form = document.getElementById('search');
form.addEventListener('submit', submitHandler);

function submitHandler(e){
    e.preventDefault();     // This method will prevent from submitting a form, when clicking on a "Submit" button
    // console.log(e)
    fetch(endpoint += form.querySelector('input').value) //This function makes a PUT request endpoint. 
    .then(response=>response.json())
    .then(data=>{
        for (var i of data) {
            console.log(i);
            // var td_index = document.createElement('td').innerText = x
        }
    })
}