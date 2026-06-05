from flask import Flask, render_template,jsonify, request, flash, url_for ,redirect
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///devtracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='devtracker2026'

db=SQLAlchemy(app)
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),unique=True,nullable=False)
    email=db.Column(db.String(150),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)

class Applications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    application_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self):              
        return f'<Task {self.id}>'
@app.route('/')
def home():
    return render_template('base.html')
# applications=[]
@app.route('/applications', methods=['POST'])
def applications(status='Pending'):
    if request.method=='POST':
        data=request.get_json()
        if not data:
            flash('All Feilds are required! ')
            return redirect(url_for('applications'))
        new_applications=Applications(job_title=data.get('job_title'),
                                      status=data.get('status'),
                                      application_id=data.get('application_id'))
        db.session.add(new_applications)
        db.session.commit()
        return jsonify({
            'id':new_applications.id,
            'job_title':new_applications.job_title,
            'status':new_applications.status
        }),201

@app.route('/applications/<int:id>', methods=['PUT'])
def update_application(id):
    application = Applications.query.get_or_404(id)
    data = request.get_json()
    application.job_title = data.get('job_title')
    application.status = data.get('status')
    db.session.commit()
    return jsonify({
        'id': application.id,
        'job_title': application.job_title,
        'status': application.status
    }), 200

@app.route('/applications/<int:id>', methods=['DELETE'])
def delete_application(id):
    app=Applications.query.get_or_404(id)
    db.session.delete(app)
    db.session.commit()
    return jsonify({'message':'ID Deleted'}),200


@app.route('/applications', methods=['GET'])

def get_applications():
    apps = Applications.query.all()
    result=[]
    for app in apps:
        result.append({
            'id':app.id,
            'job_title':app.job_title,
            'status':app.status
        })
    return jsonify({'applications':result})
with app.app_context():
    db.create_all()
if __name__=='__main__':
    app.run(debug='True')