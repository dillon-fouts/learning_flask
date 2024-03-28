from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    # Process form data here
    # Example: getting data from a form with input fields 'name' and 'email'
    name = request.form.get("name")
    email = request.form.get("email")
    # Process the data as required
    return redirect(url_for("index"))  # Redirect back to the homepage

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)