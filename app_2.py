from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Read (Retrieve) - Display all messages
@app.route('/')
def index():
    """
    Goal: Display all messages from the database.

    Instructions:
    - Complete the SQLite database connection and cursor.
    - Fetch all messages from the 'messages' table.
    - Close the database connection.
    - Render the 'index.html' template with the messages.

    Example Output (when completed):
    Display a list of messages on the webpage.
    """
    pass  # Remove 'pass' and complete the function


# Create - Add a new message
@app.route('/create_message', methods=["POST"])
def create_message():
    """
    Goal: Create a new message and add it to the database.

    Instructions:
    - Extract the message content from the POST request's form data.
    - Complete the SQLite database connection and cursor.
    - Insert the new message into the 'messages' table.
    - Commit the changes and close the database connection.
    - Redirect to the 'index' route to display the updated messages.

    Example Input (Form Data):
    {"content": "New message"}

    Example Output (when completed):
    The new message is added to the database, and the webpage is refreshed.
    """
    pass  # Remove 'pass' and complete the function

# Update - Edit a message
@app.route('/edit_message/<int:id>', methods=["GET", "POST"])
def edit_message(id):
    """
    Goal: Edit an existing message in the database.

    Instructions:
    - Complete the SQLite database connection and cursor.
    - Extract the updated message content from the POST request's form data.
    - Update the message with the given ID in the 'messages' table.
    - Commit the changes and close the database connection.
    - Redirect to the 'index' route to display the updated messages.

    Example Input (Form Data):
    {"content": "New message"}
    
    Example Output (when completed):
    The message is edited and updated in the database, and the webpage is refreshed.
    """
    pass  # Remove 'pass' and complete the function

# Delete - Remove a message
@app.route('/delete_message/<int:id>')
def delete_message(id):
    """
    Goal: Delete a message from the database.

    Instructions:
    - Complete the SQLite database connection and cursor.
    - Delete the message with the given ID from the 'messages' table.
    - Commit the changes and close the database connection.
    - Redirect to the 'index' route to display the updated messages.

    Example Output (when completed):
    The message is deleted from the database, and the webpage is refreshed.
    """
    pass  # Remove 'pass' and complete the function

if __name__ == '__main__':
    app.run(debug=True)
