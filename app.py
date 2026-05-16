from flask import Flask, render_template

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Products page
@app.route("/products")
def products():
    return render_template("products.html")

# Individual product page
@app.route("/product")
def product_detail():
    return render_template("product_detail.html")

# Menu
# Cakes Page
@app.route("/cakes")
def cakes():
    return render_template("menu/cakes.html")

# Tarts Page
@app.route("/tarts")
def tarts():
    return render_template("menu/tarts.html")

# Macarons Page
@app.route("/macarons")
def macarons():
    return render_template("menu/macarons.html")

# Profiteroles Page
@app.route("/profiteroles")
def profiteroles():
    return render_template("menu/profiteroles.html")

# BigCakes Page
@app.route("/bigcakes")
def bigcakes():
    return render_template("menu/bigcakes.html")

# Specials Page
@app.route("/specials")
def specials():
    return render_template("menu/specials.html")

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Order page
@app.route('/order')
def order():
    return render_template('order.html')

if __name__ == "__main__":
    app.run(debug=True)