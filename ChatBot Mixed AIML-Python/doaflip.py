import aiml
import requests
import re

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
mode = 0

def classify(text):
    key = "698dffc0-7c7e-11ec-aa96-6925fa064154fb6fec4c-040a-4036-b141-e089dea20220"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

while True:
    if mode == 0:
        input_text = input(">Skater: ")
        if input_text == "set mode":
            mode = 1
        else:
            response = kernel.respond(input_text)
            print(">Bot: "+response)
    elif mode == 1:
        question = input("> ")
        if question == "set mode":
            mode = 0
        else:
            answer = classify(question)
            answerclass = answer["class_name"]
            confidence = answer["confidence"]

            if confidence < 75:
              print('No lo tengo registrado como algun posible truco')
            elif answerclass == "trucos":
              print('Trucos de flat son los que se caen en el suelo')
            elif answerclass == "No_son_trucos":
              print('Palabras que no coinciden con ningun truco conocido')
            elif answerclass == "trucos_rampa":
              print('Trucos de los que se necesita una rampa para saltarlos al copi o aprovechar la inercia de la rampa')
            elif answerclass == "trucos_de_grab":
              print('Los trucos de grab consisten en algun tipo de agarre de la tabla estando en el aire')
            elif answerclass == "trucos_old_school":
                print('Los trucos de old school son los clasicos, donde empezo el skate, cuanto todavia no tenian tail y no se podian hacer trucos de saltar con pop, son muy bonitos visualmente')
