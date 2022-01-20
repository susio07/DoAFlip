import aiml
import requests
import re

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

def classify(text):
    key = "3587d4b0-7933-11ec-9f6e-bd4ae3c2cec5cfff2a8d-8855-409e-be09-49c446c6861a"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():
  question = input("> ")
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


print('Quieres saber en que consiste cada truco')

while True:
    input_text = input(">Skater: ")
    if input_text == "Como se hace un *":
        print('haolajaajjaja')
    response = kernel.respond(input_text)
    print(">Bot: "+response)