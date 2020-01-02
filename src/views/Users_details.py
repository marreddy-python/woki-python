from flask import request, json, Response, Blueprint ,render_template
from ..models.dataModel import User_details,db
from flask import jsonify,session
from flask import request 
from flask_cors import CORS, cross_origin


user_details_api = Blueprint('user_details', __name__,template_folder='templates',)


@user_details_api.route('/v1/<user_email>/<password>',methods = ['GET'])

def user_details_get(user_email,password):
    print(user_email,password)

    if request.method == "GET":

        exists = bool(User_details.query.filter_by(email=user_email,password=password).first())
        
        if exists == True:

            return jsonify(response ='USER EXISTS',status=200)
        else:
            return jsonify(response ='Email/Password did not match',status=404)


            
@user_details_api.route('/v1/', methods =['POST'])
def user_details_post(): 
    if request.method == "POST": 
        print(' METHOD CALLED ')
        data = request.json
        print(data['name'])
        user_name = data['name'] 
        user_email = data['email']
        password = data['password']
        confirm_password = data['confirm']
        
        exists = bool(User_details.query.filter_by(email=user_email).first())
        print(exists)

        if exists == True:
            return jsonify(response = 'USER ALREADY EXISTS',status=404)
        else:
            res = User_details(name = user_name,email=user_email, password=password)
            print(res)
            db.session.add(res)
            db.session.commit()
            print(user_name,user_email,password)
            return  jsonify(response ='REGISTERED SUCCESSFULLY',status=200)

        
@user_details_api.route('/v1/<user_name>/<user_email>/<password>',methods =['PUT'])
def user_details_put(user_name,user_email,password):

    if request.method == "PUT":
        print(user_email)

        admin = User_details.query.filter_by(email=user_email).first()
        admin.name = user_name
        admin.password = password

        db.session.commit()

        return 'PUT METHOD CALLED'



@user_details_api.route('/v1/<user_email>',methods =['DELETE'])
def user_details_delete(user_email):

    if request.method == "DELETE":
        exists = User_details.query.filter_by(email=user_email).delete()
        db.session.commit()
    
        return 'ACCOUNT DELETED SUCCESSFULLY'
        
       