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


if __name__ == "__main__":
    app.run(debug=True)