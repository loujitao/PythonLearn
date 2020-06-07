import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
txt = "https://smtmm.win/type/1/#?page=17"

if __name__ == '__main__':
    html=requests.get(txt,headers=headers)
    print(html.text)