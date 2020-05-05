#获取普通图片验证码
import requests
#import http.cookiejar#获取cookie，很简单也很重要
url = 'http://www.xyjyjt.com/xylogin/login.php'
re_cookies = requests.get(url).cookies

#获取验证码图片并保存到本地
import pytesseract
from PIL import Image

def yzm_sb():
    image_url = 'http://www.xyjyjt.com/include/vdimgck.php'
    yzm_image = requests.get(image_url)
    local = open('image.gif', 'wb')
    local.write(yzm_image.content)
    local.close()

    #解析图片成字符
    img = Image.open('image.gif')
    
    #在这里测试
    img = img.convert('L')
    threshold = 165
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)
    
    img = img.point(table, '1')#去掉背景模糊网格线的好方法
    img.show()
    
    
    yzm = pytesseract.image_to_string(img)
    yzm = yzm.strip()
    yzm = yzm.replace(' ','')
    return yzm

#获取验证码
yzm = yzm_sb()
flag = 1
while flag:
    if len(yzm) != 4:
        yzm = yzm_sb()
    else:
        flag = 0
print(yzm)