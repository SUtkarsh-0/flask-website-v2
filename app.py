from flask import Flask, render_template

app= Flask(__name__)

JOBS =[
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'bengaluru,India',
        'salary': '10LPA'
    },
    {
        'id':2,
        'title': 'Data Scientist',
        'location': 'delhi,India',
        'salary': '12LPA'
    },
    {
        'id':3,
        'title': 'Frontend engineer',
        'location': 'remote',
        'salary': '15LPA'
    },
    {
        'id':4,
        'title': 'Backend engineer',
        'location': 'Remote',
        'salary': '20LPA'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)