from flask import Flask
from flask import request
import json
from flask import redirect
from flask import render_template
app=Flask(__name__,static_folder="static",static_url_path="/")

@app.route("/getSum")
def getSum():
  maxNumber=request.args.get("max", 100)
  maxNumber=int(maxNumber)
  minNumber=request.args.get("min", 1)
  minNumber=int(minNumber)
  result=0
  for n in range(minNumber, maxNumber+1):
    result+=n
  return "總合："+ str(result)

@app.route("/test")
def test():
  return "This is Test MF"

@app.route("/user/<username>")
def handleUser(username):
  if username == "阿鬼":
    return "你好 "+ username
  else:
    return "Hello "+ username
  

@app.route("/json")
def index():
  lang=request.headers.get("accept-language")
  if lang.startswith("en"):
    return json.dumps({
      "states":"ok",
      "text":"Hello Flask Mother Father"})
  else:
    return json.dumps({
      "states":"ok",
      "text":"你好，台灣"}, ensure_ascii=False)
  

@app.route("/en/")
def index_en():
    return json.dumps({
      "status":"ok",
      "text":"Hello Flask Mother Father"})
@app.route("/zh/")
def index_zh():
    return json.dumps({
      "status":"ok",
      "text":"你好，母親父親"}, ensure_ascii=False)
@app.route("/")
def home():
  # print("請求方法", request.method)
  # print("通訊設定", request.scheme)
  # print("主機名稱", request.host)
  # print("路徑", request.path)
  # print("完整網址", request.url)
  # print(request.headers.get("user-agent"))
  # print(request.headers.get("accept-language"))
  # print(request.headers.get("referrer"))

  lang=request.headers.get("accept-language")
  if lang.startswith("en"):
    return redirect("/en/")
  else:
    return redirect("/zh/")

@app.route("/temp")
def index_temp():
    return render_template("index", name="VA")



app.run(port=5487)