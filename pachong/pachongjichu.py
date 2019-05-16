import requests

r = requests.get("https://www.bilibili.com/s?wd=美女")
with open("01_encode.html","w",encoding="utf_8") as f:
	f.write(r.text)
with open("01_encode.html","r") as b:
	b.read()
print(r.text)


