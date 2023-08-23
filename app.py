from flask import Flask, render_template
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

def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route("/Jobs")
def display_jobs():  
    return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=True)