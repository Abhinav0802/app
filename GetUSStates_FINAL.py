from flask import Flask, jsonify, abort, request, json, make_response

app = Flask(__name__)

states = ['Alabama',    'Alaska',    'Arizona',    'Arkansas',    'California',    'Colorado',    'Connecticut',    'Delaware',    'Florida',    'Georgia',    'Hawaii',    'Idaho',    'Illinois',    'Indiana',    'Iowa',    'Kansas',    'Kentucky ',   'Louisiana',    'Maine',    'Maryland',    'Massachusetts',    'Michigan',    'Minnesota',    'Mississippi',    'Missouri',    'Montana',    'Nebraska',    'Nevada',    'New Hampshire',    'New Jersey',    'New Mexico',    'New York',    'North Carolina',    'North Dakota',    'Ohio',   'Oklahoma',    'Oregon',    'Pennsylvania',    'Rhode Island',    'South Carolina',    'South Dakota',    'Tennessee',    'Texas',    'Utah',    'Vermont',    'Virginia',    'Washington',    'West Virginia'   , 'Wisconsin',    'Wyoming']
           



@app.route('/API/getUSStates', methods=['GET'])
def get_all_states():


    if request.method=='GET':
        return jsonify({'US States': states})

@app.route('/API/getUSStates', methods=['POST'])
def add_state():
      error_message = 'WARNING !!!! You are adding an already present State !!'
      new_state =  request.json['list']
     
      
      if new_state in states:
          return jsonify(error_message)
      else:
          states.append(new_state)
          return jsonify({'new state':states})
            
          
if __name__ == '__main__':
    app.run(debug=True)
