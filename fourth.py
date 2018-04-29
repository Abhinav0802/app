from flask import Flask, jsonify, abort, request, json, make_response

app = Flask(__name__)

states = ['Alabama',    'Alaska',    'Arizona',    'Arkansas',    'California',    'Colorado',    'Connecticut',    'Delaware',    'Florida',    'Georgia',    'Hawaii',    'Idaho',    'Illinois',    'Indiana',    'Iowa',    'Kansas',    'Kentucky ',   'Louisiana',    'Maine',    'Maryland',    'Massachusetts',    'Michigan',    'Minnesota',    'Mississippi',    'Missouri',    'Montana',    'Nebraska',    'Nevada',    'New Hampshire',    'New Jersey',    'New Mexico',    'New York',    'North Carolina',    'North Dakota',    'Ohio',   'Oklahoma',    'Oregon',    'Pennsylvania',    'Rhode Island',    'South Carolina',    'South Dakota',    'Tennessee',    'Texas',    'Utah',    'Vermont',    'Virginia',    'Washington',    'West Virginia'   , 'Wisconsin',    'Wyoming']
           



@app.route('/API/getUSStates', methods=['GET'])
def test():


    if request.method=='GET':
        return jsonify({'US States': states})

@app.route('/API/getUSStates', methods=['POST'])
def create_task():
      task2= {'Message': 'WARNING !!!! You are adding an already present State !!'}
      new_state =  request.json['list']
      states.append(new_state)
      task = [new_state for new_state in states if new_state == states[0]]
      if new_state in task:
          return jsonify({'list': task2})
      else:
          return jsonify({'new state':states})
            
          
          
       
            


    
        
            
        

if __name__ == '__main__':
    app.run(debug=True)
