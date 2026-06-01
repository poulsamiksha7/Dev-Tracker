from flask import Flask, render_template,jsonify, request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('base.html')
applications=[]
@app.route('/applications', methods=['POST'])
def add_applications():
    data=request.get_json()
    applications.append(data)
    return jsonify(data),201


if __name__=='__main__':
    app.run(debug='True')