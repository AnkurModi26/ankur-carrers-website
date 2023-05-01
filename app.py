from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Anaylst',
    'location': 'Banglore, India',
    'Salary': 'Rs.1,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scentis',
    'location': 'Delhi, India',
    'Salary': 'Rs.9,00,000'
  },
  {
    'id': 3,
    'title': 'Data Scentis',
    # 'location': 'Delhi, India',
    # 'Salary': 'Rs.15,00,000'
  },
  {
    'id': 4,
    'title': 'Back-End Enginner ',
    'location': 'SanFrancisco, USA',
    # 'Salary': '$2500000'
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="IT")


app.run(host='0.0.0.0', debug=True)
