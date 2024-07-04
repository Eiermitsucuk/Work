document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Simple validation (additional validation can be added here)
    if (name === '' || email === '' || message === '') {
        alert('All fields are required!');
        return;
    }

    // Create an object to hold form data
    const formData = {
        name: name,
        email: email,
        message: message
    };

    // Send data to the server (example endpoint)
    fetch('https://raw.githubusercontent.com/Eiermitsucuk/New/main/Contact%20Forms.txt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response-message').innerText = 'Thank you for your message!';
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('response-message').innerText = 'There was an error sending your message.';
    });
});
