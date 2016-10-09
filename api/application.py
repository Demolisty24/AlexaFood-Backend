from flask import Flask, request, jsonify
import json
import requests
application = Flask(__name__)
#"Content-Type": "application/json"

@application.route('/')
def index():
    return "Welcome to ChefAlexa's RESTful API!"

#temp testing code
@application.route('/api/add1', methods=['GET'])
def api_add1():
	return str(int(request.args.get('num')) + 10)

#
@application.route('/harambe/extract_ingredient',methods =['GET'])
def extract_ingredient():
	recipe = " ".join(request.args.get('recipe').encode("utf-8").split('_'))
	#print(recipe)
	GET_URL = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/autocomplete"
	header={
	  "X-Mashape-Key": "5ZjOXA7FMamsh4fTmzaEwHnOh2a4p1T053Djsn3LzLw2PS0Kch",
	  "Accept": "application/json"
	}
  	param ={"number": 5, "query": recipe}
  	recipeList = requests.get(GET_URL, headers=header, params=param)
  	#print(recipeList.json())
  	idSearch = {}
  	for dicts in recipeList.json():
  		idSearch[dicts["title"].encode("utf-8")] = dicts["id"]
  	#print(idSearch)
  	return jsonify(recipe_ingredient(idSearch[idSearch.keys()[0]]))

def recipe_ingredient(recipeId):
	#print("*"*80)
	#print(recipeId)
	GET_URL = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/"+str(recipeId)+"/analyzedInstructions"
	header={
	    "X-Mashape-Key": "5ZjOXA7FMamsh4fTmzaEwHnOh2a4p1T053Djsn3LzLw2PS0Kch",
	    "Accept": "application/json"
 	}
 	instructStep = requests.get(GET_URL, headers=header)
 	m = instructStep.json()
 	#print("="*100)
 	#print(m)
 	k = m[0]["steps"]
 	instructions = []
 	instructIngredients = []
 	for dicts in k:
 		instructions.append(dicts["step"].encode("utf-8"))
 		instructIngredients+=dicts["ingredients"]
	ingredient = [dicts["name"].encode("utf-8") for dicts in instructIngredients]
	#print("-"*80)
	#print(ingredient)
	return {"ingredients":" ".join(ingredient),"instructions": " ".join(instructions) }

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

if __name__ == '__main__':
	application.run(debug=True)