from flask import Flask, render_template

app: Flask = Flask(__name__)

profiles = {
    "1": {
        "Name": "Jonas",
        "Surname": "Jonaitis",
        "Age": 10
    },

    "2": {
        "Name": "Petass",
        "Surname": "Pertaitis",
        "Age": 11
    }
}

# @app.route('/home')
# def hello():
#     return render_template("index.html", my_user = user)
#

@app.route('/profile/<id>') #<betkoks kintamas>
def profile(id):
    #traukiam is db
    user = profiles[id]
    return f'Name: {user["Name"]}, Surname: {user["Surname"]}, Age: {user["Age"]}'

if __name__ == '__main__':
    app.run(debug=False)