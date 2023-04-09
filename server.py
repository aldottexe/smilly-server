from flask import Flask, request 
import json

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def sendReports():
   if request.method == 'POST':
      with open("data.json","r") as f:
         stored = json.load(f)

         newReport = json.loads(request.data)
         stored['reports'].append(newReport)

         print("stored:", stored)
      with open("data.json", "w") as f:
         json.dump(stored, f)



   with open("data.json", "r") as data:
      return data.read()

@app.route("/poster")
def poster():
   with open("sendPost.html") as f:
      return f.read()

if __name__ == "__main__":
   app.run("0.0.0.0", 80)