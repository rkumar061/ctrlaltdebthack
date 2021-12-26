from flask import Flask, request, jsonify
from models import UserModel,db

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_table.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()







@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return "this willl create data"
 
    if request.method == 'POST':
        data = request.json
        if data.get('name') and data.get('name') and data.get('password') and data.get('role'):
            email = data['email']
            password = data['password']
            name = data['name']
            role = data['role']
            user = UserModel.query.filter_by(email=email).first()   
            if user:
                return jsonify({"message": "user already exists"})
            else:
                try:
                    user = UserModel(name = name, email = email, password = password,role=role)
                    db.session.add(user)
                    db.session.commit()
                    return jsonify({"email":email,"message": "success"})
                except:
                    return jsonify({"message": "something went wrong"})
            
        else:
            return jsonify({'message':'incomplete data'})
            

@app.route("/login", methods=['GET', 'POST'])
def main():
    
    if request.method == 'POST':
        data = request.json
        if data.get('email') and data.get('password'):
            email = data['email']
            password = data['password']
            user = UserModel.query.filter_by(email=email).first()
            if user and user.password == password:
                return jsonify({"message": "success", "name": user.name, "email": user.email, "role": user.role})
            else:
                return jsonify({"message": "fail"})
        else:
            return jsonify({"message": "incomplete data"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)