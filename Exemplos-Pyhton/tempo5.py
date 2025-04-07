import requests
import time
import json

# Configurações da API
API_KEY = "7822cc73e334f7a241e6e17f385422ae"  # Substitua pela sua chave da API
CITY = "Maringá"
ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# Parâmetros da requisição
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric",  # Temperatura em Celsius
    "lang": "pt_br"  # Descrição do clima em português
}

def obter_clima():
    try:
        response = requests.get(ENDPOINT, params=params)
        response.raise_for_status()  # Lança erro para códigos HTTP ruins (4xx, 5xx)
        
        # Garante que a resposta seja tratada como UTF-8
        response.encoding = 'utf-8'
        data = response.json()

        # Formata corretamente o JSON sem caracteres errados
        json_formatado = json.dumps(data, indent=4, ensure_ascii=False)

        temperatura = data["main"]["temp"]
        umidade = data["main"]["humidity"]
        clima = data["weather"][0]["description"]

        print("\n===== Clima Atualizado =====")
        print(f"Local: {CITY}")
        print(f"Temperatura: {temperatura}°C")  # O símbolo ° já está correto
        print(f"Umidade: {umidade}%")
        print(f"Descrição: {clima.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")

# Atualiza o clima em tempo real a cada 10 segundos
while True:
    obter_clima()
    time.sleep(10)  # Aguarda 10 segundos antes de buscar novamente