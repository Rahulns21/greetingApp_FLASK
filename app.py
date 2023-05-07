from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.route('/')
def index():
    flash('What\'s your name?')
    return render_template('index.html')

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    name = request.form['name_input'].title()
    if len(name) == 0:
        flash('Name cannot be empty!')
    elif len(name) < 3:
        flash('Name must be minimum 3 characters')
    else:
        flash(f'Hi {str(name)}, great to see you')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)