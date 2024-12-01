from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail with your Gmail credentials
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail SMTP server
app.config['MAIL_PORT'] = 465  # SSL Port
app.config['MAIL_USE_TLS'] = False  # Use TLS (False as we're using SSL)
app.config['MAIL_USE_SSL'] = True  # Enable SSL
app.config['MAIL_USERNAME'] = 'echelonclub25@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'ptwgqtpjhconqrig'  # Replace with your Gmail app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'echelonclub25@gmail.com'  # Replace with your default sender email

mail = Mail(app)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')  # Home page

# Registration Form Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Collect form data
        fullname = request.form['fullname']
        rollnumber = request.form['rollnumber']
        branch = request.form['branch']
        skills = request.form['skills']
        reason = request.form['reason']

        # Validate form fields (ensure required fields are not empty)
        if not fullname or not rollnumber or not branch or not reason:
            return render_template('index.html', error="Please fill in all required fields.")

        # Create the email message
        msg = Message("New Registration", recipients=['echelonclub25@gmail.com'])  # Send to your email
        msg.body = f"New Registration\n\nFull Name: {fullname}\nRoll Number: {rollnumber}\nBranch: {branch}\nSkills: {skills}\nReason: {reason}"

        try:
            # Send the email
            mail.send(msg)
            return redirect(url_for('thank_you'))  # Redirect to thank-you page on success
        except Exception as e:
            return f"Error: {e}"

    return render_template('index.html')  # Render the registration form page

# Thank You Page Route (after form submission)
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')  # A custom thank-you page

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
            return render_template('contact.html', error="Please fill in all fields.")

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

# Team Route
@app.route('/team')
def team():
    return render_template('team.html')  # Renders the Team page

if __name__ == '__main__':
    app.run(debug=True)
