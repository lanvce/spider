from PIL import Image
import pytesseract


print("-----------------------------------------------------------------------------------------------")
text=pytesseract.image_to_string(Image.open('one.png'),lang='chi_sim') #chi_sim是一个解析中文简体的数据包,需要自己下载
print(text)