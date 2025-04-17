from colorama import Fore, Style, init
init(autoreset=True)

def get_weather(city):
    return f"{Fore.YELLOW}{city} için hava durumu: Güneşli, 25°C"

city = input("Şehir giriniz: ")
print(get_weather(city))
