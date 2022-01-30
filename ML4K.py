import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "3fb84010-8210-11ec-9666-4f69995563d21ac312b5-4c62-43ac-8a7b-4b142a572f42"
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
  elif answerclass == "Ollie":
    print('Ese truco es un Ollie')
  elif answerclass == "KickFlip":
    print('Ese truco es un KickFlip')
  elif answerclass == "HellFlip":
    print('Ese truco es un HellFlip')
  elif answerclass == "VarialFlip":
    print('Ese truco es un VarialFlip')
  elif answerclass == "Backside":
    print('Ese truco es un Backside')
  elif answerclass == "ShoveIt":
    print('Ese truco es un ShoveIt')
  elif answerclass == "Frontside":
    print('Ese truco es un Frontside')
  elif answerclass == "TreeFlip":
    print('Ese truco es un TreeFlip')
  elif answerclass == "VarialHell":
    print('Ese truco es un VarialHell')
  elif answerclass == "FrontsideFlip":
    print('Ese truco es un FrontsideFlip')
  elif answerclass == "BacksideFlip":
    print('Ese truco es un BacksideFlip')
  elif answerclass == "FrontsideHell":
    print('Ese truco es un FrontsideHell')
  elif answerclass == "Powerside":
    print('Ese truco es un Powerside')


print('Identificar truco')

while True:
  answer_question()