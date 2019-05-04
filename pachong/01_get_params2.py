import urllib.request
import urllib.parse
import string


def get_params():
	url = "http://www.baidu.com/s?"

	params = {
		"wd":"中文",
		"kew":"zhang",
		"value":"san"
		}
	str_params = urllib.parse.urlencode(params)
	"""将字典的key转化为asscii码且符合前端格式"""
	print(str_params)
	final_url = url + str_params
	print(final_url)
	request = urllib.request.Request(final_url)
	response = urllib.request.urlopen(request)
	data = response.read().decode("utf-8")
	print(request.headers)
	with open("02header.html","w") as f:
		f.write("data")
get_params()