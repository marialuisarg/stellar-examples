from stellar_sdk import Keypair, Network, Server, TransactionBuilder, Asset

# Chaves das contas
secret_key_sender = ""
public_key_receiver = ""

server = Server("https://horizon-testnet.stellar.org")
source_keypair = Keypair.from_secret(secret_key_sender)
source_account = server.load_account(source_keypair.public_key)

# Construir transação
transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100
    )
    .add_text_memo("Pagamento de teste")
    .append_payment_op(
        destination=public_key_receiver,
        amount="10",            # Quantidade
        asset=Asset.native()    # Lumens (XLM)
    )
    .set_timeout(30)
    .build()
)

# Assinar e enviar
transaction.sign(source_keypair)
response = server.submit_transaction(transaction)

print("Transação enviada!")
print(response)
