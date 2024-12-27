from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Success route
@app.route('/success/<name>')
def success(name):
    return f'<h1>Welcome {name}! Enjoy the experience!</h1>'

# Login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')  # Fetch 'nm' from form
        if user:
            return redirect(url_for('success', name=user))
        else:
            return "Name not provided in form data!", 400
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)