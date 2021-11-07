from urllib.parse import quote
from urllib.parse import unquote


def getCode():
    url_text = input("Please enter url:")
    youwant = input("Please select the type of operation you want, encode or decode:")
    aa = "encode"  # 编码
    bb = "decode"   # 解码
    if youwant == aa:
        url_text = quote(url_text)
    elif youwant == bb:
        url_text = unquote(url_text)
    else:
        print('Input error!! Please enter encode or decode:')
    print(url_text)
    return None


if __name__ == '__main__':
    getCode()
