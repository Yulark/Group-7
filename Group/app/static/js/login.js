/* Login JavaScript */

document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const messageDiv = document.getElementById('loginMessage');
    const button = e.target.querySelector('button[type="submit"]');

    // Clear previous message
    messageDiv.classList.add('hidden');
    messageDiv.textContent = '';

    // Disable button and show loading state
    button.disabled = true;
    button.classList.add('loading');
    button.textContent = 'Logging in...';

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            // Show success message
            messageDiv.classList.remove('hidden');
            messageDiv.classList.add('success');
            messageDiv.textContent = '✓ Login successful! Redirecting...';

            // Redirect to dashboard after 1.5 seconds
            setTimeout(() => {
                window.location.href = '/dashboard';
            }, 1500);
        } else {
            // Show error message
            messageDiv.classList.remove('hidden');
            messageDiv.classList.add('error');
            messageDiv.textContent = '✗ ' + data.message;

            // Re-enable button
            button.disabled = false;
            button.classList.remove('loading');
            button.textContent = 'Login';
        }
    } catch (error) {
        console.error('Login error:', error);
        messageDiv.classList.remove('hidden');
        messageDiv.classList.add('error');
        messageDiv.textContent = '✗ An error occurred. Please try again.';

        // Re-enable button
        button.disabled = false;
        button.classList.remove('loading');
        button.textContent = 'Login';
    }
});

// Allow Enter key to submit form
document.getElementById('password').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        document.getElementById('loginForm').dispatchEvent(new Event('submit'));
    }
});

// Clear error message when typing
document.getElementById('username').addEventListener('input', clearMessage);
document.getElementById('password').addEventListener('input', clearMessage);

function clearMessage() {
    const messageDiv = document.getElementById('loginMessage');
    messageDiv.classList.add('hidden');
    messageDiv.classList.remove('error');
}

console.log('Login script loaded');
