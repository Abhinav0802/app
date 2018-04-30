# REST Web Services using Python + Flask
# Using GET and POST method

URL
 http://localhost:5000/API/getUSStates

METHODS USED:
GET | POST

CALL EXAMPLES (WINDOWS CMD):
GET:
curl -i http://localhost:5000/API/getUSStates

POST:
curl -i -H "Content-Type: application/json" -X POST -d "{"""list""":"""Alaska"""}" http://localhost:5000/API/getUSStates

GET REQUEST RESPONSE :
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 896
Server: Werkzeug/0.14.1 Python/3.5.2
Date: Mon, 30 Apr 2018 00:19:41 GMT

{
  "US States": [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky ",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
  ]
}


POST RESPONSE :

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 58
Server: Werkzeug/0.14.1 Python/3.5.2
Date: Mon, 30 Apr 2018 00:20:46 GMT

"WARNING !!!! You are adding an already present State !!"



