import urllib.request
from urllib.parse import urlencode
import pyperclip


params = {'text': pyperclip.paste()} # GET请求参数，即要发送的文本

#clip.php的作用是将接收到的文本写入clip.txt文件
text = urllib.request.urlopen("https://51simple.com/clip.php?" + urlencode(params))
