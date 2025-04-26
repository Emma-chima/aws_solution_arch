import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list holding some default jokes
jokes = [
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don’t scientists trust atoms? Because they make up everything!"
]

@app.route('/')
def index():
    # Select a random joke to display
    selected_joke = random.choice(jokes)
    return render_template('index.html', joke=selected_joke)

@app.route('/add', methods=['POST'])
def add_joke():
    # Retrieve the new joke from the form data
    new_joke = request.form.get('new_joke')
    if new_joke:
        jokes.append(new_joke)
    # Redirect back to the homepage to display a joke (now including the new one)
    return redirect(url_for('index'))

@app.route('/health')
def health_check():
    return 'Healthy', 200


if __name__ == "__main__":
    # Run the application in debug mode for development purposes
    app.run(port=5000, debug=True)
