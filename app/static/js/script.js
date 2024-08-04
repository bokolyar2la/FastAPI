async function regFunction(event) {
    event.preventDefault();  // Prevent default form action

    // Get the form and collect data from it
    const form = document.getElementById('registration-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Check response success
        if (!response.ok) {
            // Get error data
            const errorData = await response.json();
            displayErrors(errorData);  // Display errors
            return;  // Stop function execution
        }

        const result = await response.json();

        if (result.message) {  // Check for success message
            window.location.href = '/pages/login';  // Redirect user to login page
        } else {
            alert(result.message || 'Unknown error');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during registration. Please try again.');
    }
}

async function loginFunction(event) {
    event.preventDefault();  // Prevent default form action

    // Get the form and collect data from it
    const form = document.getElementById('login-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Check response success
        if (!response.ok) {
            // Get error data
            const errorData = await response.json();
            displayErrors(errorData);  // Display errors
            return;  // Stop function execution
        }

        const result = await response.json();

        if (result.message) {  // Check for success message
            window.location.href = '/pages/profile';  // Redirect user to profile page
        } else {
            alert(result.message || 'Unknown error');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during login. Please try again.');
    }
}

async function logoutFunction() {
    try {
        // Send POST request to delete the cookie on the server
        let response = await fetch('/auth/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        // Check server response
        if (response.ok) {
            // Redirect user to login page
            window.location.href = '/pages/login';
        } else {
            // Read possible error message from the server
            const errorData = await response.json();
            console.error('Logout error:', errorData.message || response.statusText);
        }
    } catch (error) {
        console.error('Network error', error);
    }
}

// Function to display errors
function displayErrors(errorData) {
    let message = 'An error occurred';

    if (errorData && errorData.detail) {
        if (Array.isArray(errorData.detail)) {
            // Handle array of errors
            message = errorData.detail.map(error => {
                if (error.type === 'string_too_short') {
                    return `Field "${error.loc[1]}" must contain at least ${error.ctx.min_length} characters.`;
                }
                return error.msg || 'An error occurred';
            }).join('\n');
        } else {
            // Handle single error
            message = errorData.detail || 'An error occurred';
        }
    }

    // Display error message
    alert(message);
}
