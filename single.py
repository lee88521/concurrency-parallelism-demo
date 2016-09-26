# encoding:utf-8

from time import time
from itertools import chain

from download import setup_download_dir, get_links, download_link


def main():
    ts = time()

    url1 = 'http://www.toutiao.com/a6333981316853907714'
    url2 = 'http://www.toutiao.com/a6334459308533350658'
    url3 = 'http://www.toutiao.com/a6313664289211924737'
    url4 = 'http://www.toutiao.com/a6334337170774458625'
    url5 = 'http://www.toutiao.com/a6334486705982996738'
    download_dir = setup_download_dir('single_imgs')
    links = list(chain(
        get_links(url1),
        get_links(url2),
        get_links(url3),
        get_links(url4),
        get_links(url5),
    ))
    for link in links:
        download_link(download_dir, link)
    print('一共下载了 {} 张图片'.format(len(links)))
    print('Took {}s'.format(time() - ts))


if __name__ == '__main__':
    main()

"""
一共下载了 253 张图片
Took 166.0219452381134s
"""
