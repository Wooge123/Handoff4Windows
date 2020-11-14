import urllib.request
import pyperclip

#读取服务器上的文本内容
text = urllib.request.urlopen("https://51simple.com/clip.txt").read().decode("utf-8")

pyperclip.copy(text)