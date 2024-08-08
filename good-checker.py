import requests as req
import webbrowser as wb
import time

def checker():
    url = "https://shop.hololivepro.com/products/minatoaqua_an6th"
    res = req.get(url)
    print("レスポンスコード：" , res.status_code)
    if(res.status_code != 404):
        print("つながりました！")
        wb.open(url)
        return res.status_code
    else:
        print("つながりませんでした。")
        return res.status_code


while True:
    time.sleep(1)
    if(checker() != 404):
        break
