#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 10协程asyncio模块编写爬虫.py
# @Time      : 2022/5/13 14:08
# @Author    : weilig
import asyncio

# 获取图片地址
import json
import os
import time

import requests


def get_page():
    page_urls = []
    for i in range(1, 21):
        url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(i)
        print(url)
        page_urls.append(url)
    return page_urls


# 请求每页的url地址
def get_img():
    img_urls = []
    page_urls = get_page()
    for page_url in page_urls:
        res = requests.get(page_url)
        # res = requests.get(page_url, headers=headers)
        result = res.content.decode('utf-8')
        res_dict = json.loads(result)
        skins = res_dict["skins"]

        for hero in skins:
            item = {}
            item['name'] = hero["heroName"]
            item['skin_name'] = hero["name"]
            if hero["mainImg"] == '':
                continue
            item['imgLink'] = hero["mainImg"]
            print(item)
            img_urls.append(item)
    return img_urls


# 保存文件夹
async def save_img(index, img_url):
    path = "皮肤/" + img_url['name']
    if not os.path.exists(path):
        os.makedirs(path)
    content = requests.get(img_url['imgLink']).content
    with open('./皮肤/' + img_url['name'] + '/' + img_url['skin_name'] + str(index) + '.jpg', 'wb') as f:
        f.write(content)


def main():
    loop = asyncio.get_event_loop()  # 获取循环事件
    img_urls = get_img()  # 获取图片的url列表
    print(len(img_urls))
    tasks = [save_img(img[0], img[1]) for img in enumerate(img_urls)]  # 将图片的url列表分类构建task任务
    try:
        loop.run_until_complete(asyncio.wait(tasks))  # 启动事件循环，多个图片url下载任务进行并发
    finally:
        loop.close()  # task任务执行完成，关闭循环事件


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)
