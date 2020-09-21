import execjs
import json
import requests

url = "http://ppt.sotary.com/opi/v1/search.ashx?fid={}&size=48&keyword="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
           "Referer": "http://ppt.sotary.com/web/wxapp/index.html"
           }
fid = 1111111111

def get_des_psswd(data):
    jsstr = get_js()
    ctx = execjs.compile(jsstr) #加载JS文件
    return (ctx.call('Codage2025.decode', data))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数

def get_js():
    f = open("./a.js", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr

def req(id):
    respon = requests.get(url.format(id), headers=headers)
    # print(respon.content)
    result = get_des_psswd(str(respon.content, encoding='utf-8'))
    return result

if __name__ == '__main__':
  while fid!= -1:
      result = req(fid)
      jsRes= json.loads(result)
      print(jsRes)
      rows = jsRes.get("rows")
      if len(rows) == 0:
          fid = -1
      else:
          id = rows[len(rows) - 1].get("id")
          # print(id)
          fid = id