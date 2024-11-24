from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail directly with your Gmail credentials
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail SMTP server
app.config['MAIL_PORT'] = 465  # SSL Port
app.config['MAIL_USE_TLS'] = False  # Use TLS (False as we're using SSL)
app.config['MAIL_USE_SSL'] = True  # Enable SSL
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'your-app-password'  # Replace with your Gmail app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'  # Replace with your default sender email

mail = Mail(app)

# Home Route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Collect form data
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Validate form fields
        if not name or not email or not subject or not message:
            return "Please fill in all fields."

        # Create the email message
        msg = Message(subject, recipients=['echelonclub25@gmail.com'])  # Send to your email
        msg.body = f"Message from: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send the email
            mail.send(msg)
            return redirect(url_for('thank_you'))  # Redirect to thank-you page on success
        except Exception as e:
            return f"Error: {e}"

    return render_template('index.html')  # Home page

# About Route
@app.route('/about')
def about():
    return render_template('about.html')  # Renders the About page

# Projects Route
@app.route('/projects')
def projects():
    return render_template('projects.html')  # Renders the Projects page

# Gallery Route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')  # Renders the Gallery page

# Contact Route (with form submission handling)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Collect form data
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Validate form fields
        if not name or not email or not subject or not message:
            return "Please fill in all fields."

        # Create the email message
        msg = Message(subject, recipients=['echelonclub25@gmail.com'])  # Send to your email
        msg.body = f"Message from: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send the email
            mail.send(msg)
            return redirect(url_for('thank_you'))  # Redirect to thank-you page on success
        except Exception as e:
            return f"Error: {e}"

    return render_template('contact.html')  # Renders the Contact page

# Thank You Route (after form submission)
@app.route('/thank_you')
def thank_you():
    return 'Thank you for contacting us!'  # A simple thank-you message

# Team Route
@app.route('/team')
def team():
    return render_template('team.html')  # Renders the Team page

#Clubacheivements Route
@app.route('/clubacheivements')
def clubacheivements():
    return render_template('clubacheivements.html') # Renders the clubacheivements page

if __name__ == '__main__':
    app.run(debug=True)
