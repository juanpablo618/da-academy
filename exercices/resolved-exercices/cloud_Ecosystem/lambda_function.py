import json
import random

from datetime import date

cars = ["juan", "Cuello", "Nico", "Gaston", "Gustavo", "Carlos", "Javier", "Leandro", "Rafael"]

def lambda_handler(event, context):
    
    today = date.today()
    
    print("Hi ", cars[random.randrange(8)]+"!"+"Current time is: "+str(today))



lambda_handler(event, context)