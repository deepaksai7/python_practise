import requests
import json

SUBSCRIPTION_KEY="your_key"
vision_service_address="https://imageanalyzerpython.cognitiveservices.azure.com/"
address=vision_service_address+"vision/v2.0/analyze"
parameters={'visualFeatures':'Description,Color',
'language':'en'}
image_path="C:\myspace\codes\python_tutorial\images\polarbear.jpg"
image_data=open(image_path,"rb").read()
headers={'Content-Type':'application/octet-stream',
'Ocp-Apim-Subscription-Key':SUBSCRIPTION_KEY}

response=requests.post(address,headers=headers,params=parameters,data=image_data)
response.raise_for_status()

results=response.json()
print(json.dumps(results))
