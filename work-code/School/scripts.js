document.getElementById('newsletterForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var responseMessage = document.getElementById('responseMessage');

    if(name && email) {
        responseMessage.textContent = 'Thank you for signing up, ' + name + '!';
        // Here you can add your logic to handle the form data, e.g., send it to your server
    } else {
        responseMessage.textContent = 'Please fill out both fields.';
    }
});
