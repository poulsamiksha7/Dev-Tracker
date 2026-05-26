from flask import Flask, render_template,jsonify
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('base.html')
@app.route('/tasks')
def tasks():
    return jsonify({'tasks':[
        {
            "id": 1,
            "title": "Buy medicine",
            "done": False
        }
    ]})

if __name__=='__main__':
    app.run(debug='True')