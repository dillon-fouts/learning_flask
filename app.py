from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = []

# Define routes
@app.route("/")
def index():
    return render_template("index.html", books=books)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    author = request.form.get("author")
    pages = request.form.get("pages")
    classification = request.form.get("classification")
    details = request.form.getlist("details")
    how = request.form.get("how")
    
    # Modify classification to include hyphen
    if classification == "nonfiction":
        classification = "non-fiction"
    
    # Modify details to display shorter versions
    details_mapping = {
        "I own this book": "own",
        "I've read this book": "read",
        "I liked this book": "liked",
        "I would recommend this book to others": "recommend"
    }
    details_short = ", ".join([details_mapping.get(detail, detail) for detail in details])
    
    # Modify acquisition to display shorter versions
    acquisition_mapping = {
        "I purchased it": "purchased",
        "It was a gift": "gift",
        "I checked it out from the library": "library",
        "A friend loaned it to me": "friend"
    }
    how_short = acquisition_mapping.get(how, how)
    
    books.append({
        "title": title,
        "author": author,
        "pages": pages,
        "classification": classification,
        "details": details_short,
        "how": how_short
    })
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

