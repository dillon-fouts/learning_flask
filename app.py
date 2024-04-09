from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

experience = []

# Define routes
@app.route("/")
def index():
    return render_template("index.html", experience=experience)

@app.route("/add", methods=["POST"])
def add():
    age = request.form.get("age")
    gender = request.form.get("gender")
    country = request.form.get("country")
    degree = request.form.get("highest_deg")
    code_experience = request.form.getlist("code_experience")
    title = request.form.get("current_title")
    company_size = request.form.get("company_size")
      
    experience.append({
        "age": age,
        "gender": gender,
        "country": country,
        "degree": degree,
        "code_experience": code_experience,
        "title": title,
        "size": company_size
    })
    
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

