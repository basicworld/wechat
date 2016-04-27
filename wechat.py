# -*- coding:utf8 -*-
""""""
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from wechat_sdk import WechatC
conf = WechatConf(
    token='githubcombasicworld',
    appid='wx29533c7d857ec5ae',
    appsecret='c6dfe1319b2a6cb5e2cbf1314ff9f6ae',
    encrypt_mode='normal',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    encoding_aes_key='Xg1R5t08GAL6Q5cBdedXst8Xib30qadRIH6EbnA0VfC'  # 如果传入此值则必须保证同时传入 token, appid
)
from wechat_sdk import WechatBasic
wechat = WechatBasic(conf=conf)
