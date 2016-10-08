from flask import Flask, request
application = Flask(__name__)

@application.route('/')
@application.route('/index')
def index():
    return "Welcome to ChefAlexa's RESTful API!"


@application.route('/api/add1', methods=['GET'])
def api_add1():
	return str(int(request.args.get('num')) + 1)


if __name__ == '__main__':
	application.run(debug=True)
