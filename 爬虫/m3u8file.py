from urllib.request import urlretrieve
import m3u8
from random import randint


def main(url):
    m2 = m3u8.load(url)
    print('开始下载 ts列表...')
    for sm in m2.segments:
        url2 = sm.absolute_uri
        print(url2 +"\t"+ sm.uri )
        urlretrieve(url2, sm.uri)
    print('下载完毕')

    # 合并ts片段，存为与文件夹同名的ts文件
    fn = input('开始合并文件,输入文件名:')
    fn = f"{randint(1000, 9999)}" if fn == '' else fn
    fn = fn + '.mp4'

    with open(fn, 'wb') as f:
        for sm in m2.segments:
            with open(sm.uri, 'rb') as g:
                f.write(g.read())
    print('合并文件完毕。。。')


if __name__ == '__main__':
        m3u8Url='https://hls.cntv.myalicdn.com/asp/hls/1200/0303000a/3/default/aa16c6ba677f413e9455f0f0667907ce/1200.m3u8?maxbr=2048'
        main(m3u8Url)
