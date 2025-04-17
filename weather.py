# Basit Hava Durumu Uygulaması (Main Branch)
# Hazırlayan: Ege Çağın Tepe

def get_weather(city):
    # Gerçek API yerine örnek veri döndürüyoruz
    return f"{city} için hava durumu: Güneşli, 25°C"

city = input("Şehir giriniz: ")
print(get_weather(city))
