from flask import Flask, request, jsonify
import json
import requests
application = Flask(__name__)
#"Content-Type": "application/json"


@application.route('/')
def index():
    return "Welcome to ChefAlexa's RESTful API!"


#Identify the ID of the closest recipe of the user's dish request and 
#return a dictionary of the ingredient and instruction of the recipe
@application.route('/harambe/extract_ingredient',methods =['GET'])
def extract_ingredient():
	recipe = " ".join(request.args.get('recipe').encode("utf-8").split('_'))
	GET_URL = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/autocomplete"
	header={
	  "X-Mashape-Key": "5ZjOXA7FMamsh4fTmzaEwHnOh2a4p1T053Djsn3LzLw2PS0Kch",
	  "Accept": "application/json"
	}
  	param ={"number": 5, "query": recipe}
  	recipe_list = requests.get(GET_URL, headers=header, params=param)
  	id_search = {}
  	other_recipt = {"recipes":[]}
  	print(recipe_list.json())
  	for dicts in recipe_list.json():
  		id_search[dicts["title"].encode("utf-8")] = dicts["id"]
  		other_recipt["recipes"].append(dicts["title"].encode("utf-8"))
  	del other_recipt["recipes"][0]
  	other_recipt["recipes"] = " , ".join(other_recipt["recipes"])

  	dish_data = recipe_ingredient(id_search[id_search.keys()[0]])
  	dish_data.update(other_recipt)

  	return jsonify(dish_data)


#get the ingredient and instruction from the API based on recipe ID
def recipe_ingredient(dish_id):
	GET_URL = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/"+str(dish_id)+"/analyzedInstructions"
	header={
	    "X-Mashape-Key": "5ZjOXA7FMamsh4fTmzaEwHnOh2a4p1T053Djsn3LzLw2PS0Kch",
	    "Accept": "application/json"
 	}
 	instruct_step = requests.get(GET_URL, headers=header)
 	m = instruct_step.json()
 	k = m[0]["steps"]
 	instructions = []
 	instruct_ingredients = []
 	for dicts in k:
 		instructions.append(dicts["step"].encode("utf-8"))
 		instruct_ingredients+=dicts["ingredients"]
	ingredient = [dicts["name"].encode("utf-8") for dicts in instruct_ingredients]
	return {"ingredients":" , ".join(ingredient),"instructions": " ".join(instructions) }


if __name__ == '__main__':
	application.run(debug=True)