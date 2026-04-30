from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/desserts')
def desserts():
    return render_template('desserts/desserts.html')

@app.route('/cakes')
def cakes():
    return render_template('desserts/cakes.html')

@app.route('/tarts')
def tarts():
    return render_template('desserts/tarts.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        amount = request.form['amount']
        cake_type = request.form['cake_type']
        flavour = request.form['flavour']
        size = request.form['size']
        occasion = request.form['occasion']
        message = request.form['message']

        print("New cake order received:")
        print(name, email, amount, cake_type, flavour, size, occasion, message)

        return render_template('success.html', name=name)


    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
