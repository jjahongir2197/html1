from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        return f"Ro‘yxatdan o‘tildi: {name}, {email}"

    return render_template("index.html")

app.run(debug=True)
