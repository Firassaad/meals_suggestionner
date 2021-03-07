
from collections import OrderedDict
from flask import Flask
from flask import jsonify
from flask import json
import zeep
import random
from flask import request
from flask_cors import CORS
import collections
from flask import request
orderedDict = collections.OrderedDict()

app = Flask(__name__)
CORS(app)

cors = CORS(app, resources={r"/*": {"origins":["http://localhost:4200"]}},supports_credentials=True)

app.config['JSON_SORT_KEYS'] = False

class Meal:
  def __init__(self, name, cal):
    self.name = name
    self.cal = cal

p1 = Meal("Apéricube", 16) ;            p2 = Meal("Bretzel ", 80) ;          p3 = Meal("Noix de cajou", 612) ;       p4 = Meal("Daurade", 77)
p5 = Meal("Sardines fraîches", 77) ;    p6 = Meal("Saumon frais", 200) ;     p7 = Meal("Agneau ", 	112) ;         p8 = Meal("Boeuf (cervelle)", 130)
p9 = Meal("Dinde", 125) ;               p10 = Meal("Artichaut", 40) ;        p11 = Meal("Asperges", 26) ;            p12 = Meal("Carotte", 38);p13 = Meal("Champignons", 28)
p14 = Meal("Epinards", 	25) ;         p15 = Meal("Lentilles", 338) ;       p16 = Meal("Patate douce", 110) ;       p17 = Meal("Pomme de terre (purée)", 95)

@app.route('/calc', methods=['GET', 'POST'])
def getNeeds():
    cal = request.args.get("cal")
    print("cal rout =" ,cal)
    return retList(cal)


def retList(a: str):
    liste = [p1, p2, p3 ,p4 ,p5 ,p6, p7 ,p8 ,p9 ,p10, p11, p12 ,p13 ,p14,p15,p16,p17]
    L=[]  
    sum = 0
    for i in liste:    
        x = random.choice(liste)
        #delete to not repeat the same element il the list
        liste.remove(x)
        sum=sum+x.cal
        print(">>>>>>>>>>>>",sum)
        marge =50        
        if(sum < int(a) + marge +20):
            L.append({'name' : str(x.name) , 'cal' :str(x.cal)})
        if(sum<=int(a)+marge and sum>=int(a)-marge):
            print(sum)
            sum = 0
            break

    return jsonify(L)

if __name__ == '__main__':
    app.run(port=8080, debug=True, host='localhost', use_reloader=False)
