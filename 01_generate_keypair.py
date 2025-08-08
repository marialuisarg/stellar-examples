from stellar_sdk import Keypair
import requests

# Gerar um novo par de chaves
keypair = Keypair.random()
public_key = keypair.public_key
secret_key = keypair.secret

print("Public Key:", public_key)
print("Secret Key:", secret_key)

# Financiar usando Friendbot (testnet)
url = f"https://friendbot.stellar.org/?addr={public_key}"
response = requests.get(url)

if response.status_code == 200:
    print("Conta financiada com sucesso!")
else:
    print("Erro ao financiar:", response.text)
