# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@IDE--Env : PyCharm--
@Project  :  ChatGPT_api
@File     :  server.py
@Time     :  2023/2/10 17:26
@Author   :  gpc
@Contact  :  phone@163.com
@License  :  (C)Copyright 2021
@Desc     :  None
"""
import requests
from flask import Flask
from flask import request
from flask_cors import *
import traceback
import json
import logging
import time


app = Flask(__name__)
CORS(app, supports_credentials=True)
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
conf = json.load(open("config.json"))


def chatgpt35_api(request_data):
    """offical api"""
    # data = {
    #     "messages": [{"role": "user", "content": prompt}],
    #     "max_tokens": conf["max_tokens"],
    #     "model": conf["model"],
    #     "top_p": conf["top_p"],
    #     "temperature": 0.5,
    #     "n": num
    # }
    headers = {
        "content-type": "application/json",
        'Authorization': "Bearer " + conf["key"]
    }
    response = requests.post(url=conf["url"], headers=headers, json=request_data)
    answer = [elem["message"] for elem in response.json()['choices']]
    return answer


@app.route('/api/chatgpt/v2', methods=['GET', 'POST'])
def extract_info():
    code = 200
    log_text = ""
    answer = ""
    elapse = ""
    try:
        request_data = json.loads(request.get_data(as_text=True))
        log_text = "access message as below\naccess parameter: \n"
        log_text += "\tqps_data: {qps_data}".format(qps_data=request_data)
        st = time.time()
        answer = chatgpt35_api(request_data)  # 20220419
        elapse = f"{round(time.time() - st, 3)} s"
        msg = "成功"
    except Exception as e:
        log_text += "exception args: {args}".format(args=e.args)  # 异常信息
        log_text += traceback.format_exc() + "\n"  # 异常详细信息
        code = 500
        msg = "服务器内部错误！"
    data = {"answer": answer, "elapse": elapse}
    response = json.dumps({"code": code, "msg": msg, "data": data}, ensure_ascii=False)
    log_text += "\nreturned data: \n\t{data}".format(data=data)  # 接口返回数据
    logging.info(log_text)
    return response


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    from time import strftime, localtime
    with open("log.txt", "a+", encoding="utf8") as f:
        f.write("\nService on port 5200 started ^_-\n" + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n")
    app.run(host='0.0.0.0', port=5200, processes=True)  # threaded=True