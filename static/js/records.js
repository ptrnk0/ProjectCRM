// filling reservation date input with current date
const date = new Date()
document.getElementById('reservation_date').value = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate().toString().padStart(2, "0")}`

console.log(document.getElementById('reservation_date').value)
// Calling the function for constructing forms and record table
getBookings()

// Constructing trigger by changing the reservation date for function calling
document.getElementById('reservation_date').addEventListener('change', getBookings)

function getBookings() {
    let reserved_slots = []
    const date = document.getElementById('reservation_date').value
    document.getElementById('today').innerHTML = date

    fetch("{% url 'record' %}" + '?date=' + date)
        .then(r => r.json())
        .then(data => {
            reserved_slots = []
            bookings = ""
            console.log(data)
            
            // Constructing paragraphs for reserved times
            for (const item of data) {
                console.log(item.fields)
                reserved_slots.push(item.fields.reservation_slot)
                bookings += `<p>${item.fields.first_name} - ${formatTime(item.fields.reservation_slot)} </p>`
            }

            // Constructing options for time select
            slot_options = `<option value="0" disabled>Select time</option>`
            for (let i = 10; i < 20; i++) {
                const label = formatTime(i)
                if (reserved_slots.includes(i)) {
                slot_options += `<option value=${i} disabled>${label}</option>`
                } else {
                slot_options += `<option value=${i}>${label}</option>`
                }
            }
            
            // Inserting reserved times and options
            document.getElementById('reservation_slot').innerHTML = slot_options
            if(bookings==''){
                bookings = "No records"
            }
            document.getElementById('records').innerHTML = bookings
        })
}


// Function for constructing time label
function formatTime(time) {
    const ampm = time < 12 ? 'AM' : 'PM'
    const t = time < 12 ? time : time > 12 ? time - 12 : time
    const label = `${t} ${ampm}`
    return label
}

// Submiting the form
document.getElementById('button').addEventListener('click', function (e) {
    const formdata = {
        first_name: document.getElementById('first_name').value,
        reservation_date: document.getElementById('reservation_date').value,
        reservation_slot: document.getElementById('reservation_slot').value,
    }

    fetch("{% url 'bookings' %}", { method: 'post', body: JSON.stringify(formdata) })
        .then(r => r.text())
        .then(data => {
        getBookings()
        })
})