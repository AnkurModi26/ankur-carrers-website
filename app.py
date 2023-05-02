from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Anaylst',
    'location': 'Banglore, India',
    'Salary': 'Rs.100000'
  },
  {
    'id': 2,
    'title': 'Data Scentis',
    'location': 'Delhi, India',
    'Salary': 'Rs.900000'
  },
  {
    'id': 3,
    'title': 'Font-End Engineer',
    'location': 'Delhi, India',
    # 'Salary': 'Rs1500000'
  },
  {
    'id': 4,
    'title': 'Back-End Enginner ',
    'location': 'SanFrancisco, USA',
    'Salary': '$2500000'
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="IT")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


app.run(host='0.0.0.0', debug=True)
