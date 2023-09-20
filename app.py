from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


"""
Display all messages from the database.
This will be in the route "/" and will accept GET requests

Instructions:
- Complete the SQLite database connection and cursor.
- Fetch all messages from the 'messages' table.
- Close the database connection.
- Render the 'index.html' template with the messages.

Example Output (when completed):
Display a list of messages on the webpage.
"""


"""
Create a new message and add it to the database.
This will use "/create_message" and accept POST requests

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


"""
Edit an existing message in the database.
This will use /edit_message/[id] and accept PUT requests

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


"""
Delete a message from the database.
This will use /delete_message/[id] and accept DELETE requests

Instructions:
- Complete the SQLite database connection and cursor.
- Delete the message with the given ID from the 'messages' table.
- Commit the changes and close the database connection.
- Redirect to the 'index' route to display the updated messages.

Example Output (when completed):
The message is deleted from the database, and the webpage is refreshed.
"""

if __name__ == '__main__':
    app.run(debug=True)
