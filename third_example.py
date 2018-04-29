from flask import Flask, jsonify, abort, request, json

app = Flask(__name__)

states = [

    {   
        'list': ['Alabama',    'Alaska',    'Arizona',    'Arkansas',    'California',    'Colorado',    'Connecticut',    'Delaware',    'Florida',    'Georgia',    'Hawaii',    'Idaho',    'Illinois',    'Indiana',    'Iowa',    'Kansas',    'Kentucky ',   'Louisiana',    'Maine',    'Maryland',    'Massachusetts',    'Michigan',    'Minnesota',    'Mississippi',    'Missouri',    'Montana',    'Nebraska',    'Nevada',    'New Hampshire',    'New Jersey',    'New Mexico',    'New York',    'North Carolina',    'North Dakota',    'Ohio',   'Oklahoma',    'Oregon',    'Pennsylvania',    'Rhode Island',    'South Carolina',    'South Dakota',    'Tennessee',    'Texas',    'Utah',    'Vermont',    'Virginia',    'Washington',    'West Virginia'   , 'Wisconsin',    'Wyoming']
           }
]


@app.route('/API/getUSStates', methods=['GET'])
def test():


    if request.method=='GET':
        return jsonify({'US States': states})

@app.route('/API/getUSStates', methods=['POST'])
def create_task():

    states2 = {
       
        'list': request.json['list']
       
    }
    task2= {'Message': 'Already present bro !'}
    if states2 == states  :
        return jsonify({'list': task2})
    else:
        states.append(states2)
        return jsonify({'new state': states})

    

if __name__ == '__main__':
    app.run(debug=True)
