import os, random, math
from random import randint

#pythagoras = lambda a, b: math.pow(a,2)+math.pow(b,2)
#print(format(pythagoras(3,3), ".2f"))

data = {}
data["results"] = [{"item1":"item", "item2":"item", "item3":"item", "price":20, "cost":10000},
                {"item1":"item", "item2":"item", "item3":"item", "price":25, "cost": 200},
                {"item1":"item", "item2":"item", "item3":"item", "price":1, "cost":1000}]
dataset = data["results"]
    
def find_min_verd(dict_list):
    return {"price":min(dict_list, key=lambda d: d.get("price", float('inf')))["price"]}

print(find_min_verd(dataset))


lst = [{'price': 99, 'barcode': '2342355'}, {'price': 88, 'barcode': '2345566'}]

#returns dict that has lowest and highest value of a (key, value) pair
minPricedItem = min(lst, key=lambda x: x.get(x["price"], float("inf")))["price"]
maxPricedItem = max(lst, key=lambda x:x['price'])
print("min:", minPricedItem, "\nmax:",maxPricedItem)

#if "wares" not in session:
#        session["wares"] = []
#    if request.method == 'POST': #Catches submit form. 
#        product_id = request.form['add_to_cart']
#        for item in products["wares"]:
#            for key, value in item.items():
#                if key == "id" and value == product_id:
#                    #Bug in session caching dosen't allow you to append it, recreate session instance and append it back to session
#                    temp_session = session["wares"]
#                    temp_session.append(item)
#                    session["wares"] = temp_session
#                    print(session["wares"])     
#                if key == "id" and value == product_id:
                    #Bug in session caching dosen't allow you to append it, recreate session instance and append it back to session
                    #temp_session = session["wares"]
                    #temp_session.append(item)
                    #session["wares"] = temp_session
                    #print(session["wares"])     