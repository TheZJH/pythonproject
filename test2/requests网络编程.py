import requests

# 通过get访问一个页面
r = requests.get('https://www.baidu.com')
print(r.status_code)
print(r.text)

# 带参数的URL，传入一个dict
# r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})

# 实际请求的URL
print(r.url)

# encoding查看编码
print(r.encoding)

# 无论响应是文本还是二进制内容，用content属性获得bytes对象
print(r.content)

# 获取特定相应的JSON
# print(r.json())

# 需要传入HTTP Header时，我们传入一个dict作为headers参数
r = requests.get('https://www.douban.com/',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据
r = requests.post('https://accouts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# requests传递josn数据
parms = {'key': 'value'}
r = requests.post('https://www.douban.com/', json=parms)  # 内部自动序列化为JSON

# 上传文件
upload_files = {'files': open('report.xls', 'rb')}
# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
r = requests.post('https://www.douban.com/', files=upload_files)

# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

# 获取服务器响应头
r.headers
# 获取指定响应头
r.headers['Content-Type']

# 获取指定cookie
r.cookies['ts']

# 在请求中传入Cookie
cs = {'token': '12345', 'status': 'working'}
r = requests.get('www.baidu.com', cookies=cs)

# 指定超时
r = requests.get('www.baidu.com', timeout=2.5)  # 2.5秒后超时

# 设置代理
proxies = {
    "http": "http://192.168.31.1:3128",
    "https": "http://10.10.1.10:1080",
}
requests.get('https······························://www.baidu.com', proxies=proxies)
