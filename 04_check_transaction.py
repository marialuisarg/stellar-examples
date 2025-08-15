from stellar_sdk import Server

# ID da transação (hash)
transaction_id = ""
server = Server("https://horizon-testnet.stellar.org")

transaction = server.transactions().transaction(transaction_id).call()

print("Detalhes da transação:")
print(transaction)
