from flask import Flask, request,jsonify
import json
import requests
application = Flask(__name__)
#"Content-Type": "application/json"
parameters = { "key": "5b6061eec9a7163d416beb0923c8f830", "rId":""}

@application.route('/')
def index():
    return "Welcome to ChefAlexa's RESTful API!"

#temp testing code
@application.route('/api/add1', methods=['GET'])
def api_add1():
	return str(int(request.args.get('num')) + 10)


@application.route('/harambe/extract_ingredient',methods =['GET'])
def extract_ingredient():
	receipe = " ".join(str(request.args.get('recipe')).split('_'))
	GET_URL = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/autocomplete"
	header={
	  "X-Mashape-Key": "5ZjOXA7FMamsh4fTmzaEwHnOh2a4p1T053Djsn3LzLw2PS0Kch",
	  "Accept": "application/json"
	}
  	param ={"number": 5, "query": receipe}
  	response = requests.get(GET_URL, headers=header, params=param)
  	idSearch = {}
  	for dicts in response.json():
  		idSearch[dicts["title"]] = dicts["id"]
  	return jsonify(idSearch)


'''
@application.route('/api/apiTesting', methods=['GET'])
def api_apiTesting():
	GET_URL = "http://food2fork.com/api/get"
	#return str(request.args.get('rId'))
	header["rId"] = str(request.args.get('rId'))
	#return("recipe ID"+ header["rId"])
	response = requests.get(GET_URL, params=parameters)
	ingredient = response.json().get("ingredients")
'''
#TO-DO: fix the method to POST base on dish
#route :
'''
@application.route('/api/return_ingredient', methods=['GET'])
def return_ingredient():
	dish name = request.args.get('dish')
	#request.args.get()
'''
#return shaved off string ingredient to front-end
'''
@application.route('/api/ingredient_to_shopping_cart', methods=['GET'])
def ingredient_to_shopping_cart():
	return(some shaved off list of ingredient)
'''

if __name__ == '__main__':
	application.run(debug=True)
