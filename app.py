from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model_carprice.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        m = float(request.form["milage"])
        a = float(request.form["age"])

        p = model.predict([[m, a]])

        print(p)
        return render_template("index.html", price = round(p[0],2))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5001, debug=True)