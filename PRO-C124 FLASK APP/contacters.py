from flask import Flask,jsonify,request

app = Flask(__name__)

contactss = [{
    'id': 1,
    'name': 'Vansh',
    'contact' : '1234567890'
}]

@app.route('/addcontact', methods=["POST"])
def addcontact():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'Please give information of the contact'
        }, 400)
    else:
        c = {
            'id': contactss[-1]['id'] + 1,
            'name': request.json['name'],
            'contact' : request.json['contact']
        }
        contactss.append(c)
        return jsonify({
            'status': 'success',
            'message': 'Your contact is added'
        })

@app.route('/getcontact')
def getcontact():
    return jsonify({
        'data' : contactss
    })

if (__name__ == '__main__'):
    app.run(debug=True)
