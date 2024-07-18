# Import necessary libraries
from flask import Flask, render_template
import os

# Initialize Flask app
app = Flask(__name__, template_folder='dashboard')

# Define the root route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to serve other HTML files dynamically based on the URL
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Check if the script is executed directly and run the app
if __name__ == '__main__':
    app.run(debug=True)