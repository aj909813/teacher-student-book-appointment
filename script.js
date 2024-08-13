document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const role = document.getElementById('role').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    // Example of client-side form validation
    if (name && email && role && date && time) {
        // Send data to the backend (Python Flask)
        fetch('/book', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email, role, date, time }),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('confirmation').innerHTML = `<p>${data.message}</p>`;
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please fill in all the fields');
    }
});