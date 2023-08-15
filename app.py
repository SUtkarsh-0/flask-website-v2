from flask import Flask, render_template,jsonify
from database import load_jobs_from_db,load_job_from_db


app= Flask(__name__)


@app.route("/")  #the main route to load the templates and all the jobs form the server
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html',jobs=jobs)

@app.route("/api/jobs")  #api route to load jobs as jsonify text
def list_jobs():
    jobs= load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")  #id as a parameter for the fn below
def show_job(id):
    job = load_job_from_db(id)
    
    if not job:
        return "Not Found", 404
    
    return render_template('jobpage.html',job=job)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)