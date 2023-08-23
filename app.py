from flask import Flask, render_template,jsonify
app = Flask(__name__)
JOBS =[{'id':1,
        'title': 'Data Analyst',
       'location':'Bangalore',
        'salary': 'Rs.12,00,000' },
        {'id':2,
         'title': 'Data Scientist',
         'location': 'Delhi',
         'salary': 'Rs. 11,00,000'
         }]
@app.route("/api/jobs")  
def list_jobs():
    return jsonify(JOBS)

def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/Jobs")

if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=True)