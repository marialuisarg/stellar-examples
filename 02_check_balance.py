from stellar_sdk import Server

public_key = ""
server = Server("https://horizon-testnet.stellar.org")

account = server.accounts().account_id(public_key).call()

print(f"Saldos da conta {public_key}:")
for balance in account['balances']:
    print(f"Tipo: {balance['asset_type']} - Quantidade: {balance['balance']}")
