import requests

# Configurações da API
API_KEY = "7822cc73e334f7a241e6e17f385422ae"  # Substitua pela sua chave da API
CITY = "São Paulo"
ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# Parâmetros da requisição
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric",  # Para exibir a temperatura em Celsius
    "lang": "pt_br"  # Para obter a descrição do clima em português
}

try:
    response = requests.get(ENDPOINT, params=params)
    response.raise_for_status()  # Lança erro para códigos HTTP ruins (4xx, 5xx)
    
    # Decodifica a resposta JSON garantindo UTF-8
    data = response.json()

    temperatura = data["main"]["temp"]
    umidade = data["main"]["humidity"]
    clima = data["weather"][0]["description"]

    print(f"Clima em {CITY}:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Umidade: {umidade}%")
    print(f"Descrição: {clima.capitalize()}".encode('utf-8').decode('utf-8'))  # Garante a exibição correta

except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a API: {e}")