from flask import Flask
app = Flask(__name__)
empDB=[

 {

 'id':'101',

 'name':'Saravanan S',

 'title':'Technical Leader'

 },

 {

 'id':'201',

 'name':'Rajkumar P',

 'title':'Sr Software Engineer'

 }

 ]



@app.route('/empdb/',methods=['GET'])

def getAllEmp():

    return jsonify({'emps':empDB})
