from selenium  import webdriver
import time
import requests

base_url='https://i.zhaopin.com/'
driver_dir="D:\pyproject\PythonLearn\driver\chromedriver.exe"
driver = webdriver.Chrome(driver_dir)
headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    "cookie":'urlfrom=121113803; urlfrom2=121113803; adfbid=0; adfbid2=0; x-zp-client-id=d3520698-445a-423f-8ebc-9ae9b87cff81; sts_deviceid=1725b9b0d9a2d7-099e1b431de416-f7d1d38-2073600-1725b9b0d9b2cd; sts_sg=1; sts_sid=1725b9b0d9d35e-0ac6463728bfb2-f7d1d38-2073600-1725b9b0d9ec47; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAaNWb0ckVM0KqiAsK9kTqX00000cDPxNC00000xs000y.THLyktAJdIjA80K85yF9pywd0Znqryn3nWbYmW0snjDkn1IWm6Kd5Hn3nHT1nWndrjIhPvcdm1mYmH0knAu-nyc3nv7hn1PB0ADqI1YhUyPGujY1n1RsnjTvPW6vFMKzUvwGujYkP6K-5y9YIZK1rBtEmv4YQMGCmyqspy38mvqVQYd9ThV-IaqLpAq_uNqWULN8IANzQhG1Tjq1pyfqnHcknHD1rj01FMNzUjdCIZwsT1CEQLILIz4lpA7ETA-8QhPEUHqdIAdxTvqdThP-5yF9pywdTAPsXBudIAdxUyNbpgNV5yPsIaudIAdxmvq8IAN8IjdsmLKlFMNYUNqWmydsmy-MUWdsmzdBpy7EIAb0mLFW5HDLnjnv%26tpl%3Dtpl_11534_22672_17382%26l%3D1518144897%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3350076686_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D234%26ie%3Dutf-8%26f%3D3%26tn%3Dbaidu%26wd%3D%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%26fenlei%3D256%26rqlang%3Dcn%26inputT%3D2716%26prefixsug%3Dzhilian%26rsp%3D0; sajssdk_2015_cross_new_user=1; at=00fbf424859d4d96b936c9521dc2204b; rt=a20f4f01e9ab432b85f9eaf33f13a896; acw_tc=ac11000115906748358311904e010e8a393cbf13c06f6857103ac4d865c242; ZP-ENV-FLAG=gray; ZP_OLD_FLAG=false; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22631723877%22%2C%22%24device_id%22%3A%221725b9b0da66c0-0104ef64b9677c-f7d1d38-2073600-1725b9b0da7b6b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAaNWb0ckVM0KqiAsK9kTqX00000cDPxNC00000xs000y.THLyktAJdIjA80K85yF9pywd0Znqryn3nWbYmW0snjDkn1IWm6Kd5Hn3nHT1nWndrjIhPvcdm1mYmH0knAu-nyc3nv7%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%7D%2C%22first_id%22%3A%221725b9b0da66c0-0104ef64b9677c-f7d1d38-2073600-1725b9b0da7b6b%22%7D; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1590674835; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; privacyUpdateVersion=3; jobRiskWarning=true; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%2285b5d540-58b3-4339-9750-2f8e719e835f-sou%22}}; POSSPORTLOGIN=6; CANCELALL=0; sts_evtseq=4; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1590674870'
}








if __name__ == '__main__':
    tb_data= driver.get(base_url)
    driver.set_window_size(1500,1500)
    time.sleep(10)
    req=requests.get(base_url,headers=headers)
    req.encoding='utf-8'
    print(req.text)
