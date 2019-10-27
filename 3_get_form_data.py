from flask import Flask, render_template, request
app = Flask(__name__)
users = []


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/table')
def Table():
    return render_template('table.html')


@app.route('/register', methods=["POST", "GET"])
def Register():
    if request.method == "POST":
        form_data = request.form.to_dict()
        users.append(form_data)
        print(users)
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
