

# https://rate.tmall.com/list_detail_rate.htm?
params={
    'itemId':'549861525895',
    'spuId':'847343296',
    'sellerId':'725677994',
    'order':'3',
    'currentPage':'1',
    'append':'0',
    'content':'1',
    'tagId':'',
    'posi':'',
    'picture':'',
    'ua':'098%23E1hvipvBvovvUvCkvvvvvjiPPsqptjrPn2SvAjljPmPwzj1UPsdvQjl8Ps5pAjrE9phv2HifISNFzHi47IauzsyCvvBvpvvvdphvmZCmb9Q8vhCRKUwCvvBvppvviQhvChCvCCpPvpvhvv2MMQyCvh1vnrUvIqvsxeCB0R9t%2BFBCWDAvD40OwAtdpbmD5i3sB5Hj%2BnezrmphwhKn3feAOHHzLwexRdIAcVvHfwofdervfvc61CI4wx60747BkphvCyEmmvQfeTyCvv3vpvoBtGXZiqyCvm3vpvmOvvCv4ZCvhCpvvhU3phvZvvvvp0nvpCpvvvC2oyCvhCpvvh8VvphvCyCCvvvvv2yCvvBvpvvv9phv2HiwzJMtjHi47es%2BzT6CvvDvpIOWQ9Cv7CervpvEphmlhmvvpV3vRphvChCvvvmrvpvEphVH2C6vpVgK',
    'isg':'BMzMjs2M-0jRm-_-A-5Z8scEnSw-rXDKAL9pcSaNH3cWsW27ThQZP0HjVfks-agH',
    '_ksTS':'1532490499188_807',
    'callback':'jsonp808',
}

import requests
from urllib.parse import urlencode
url = 'https://rate.tmall.com/list_detail_rate.htm?{params}'.format(params=urlencode(params))
print(requests.get(url=url))

