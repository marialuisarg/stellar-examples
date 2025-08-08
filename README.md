```
# Trabalho Prático - Sistemas Distribuídos (DCC064 - 2025/1 UFJF)

Desenvolvido por:
- Abraão de Paula Carolino
- Maria Luísa Riolino Guimarães
- Nicolas Soares Martins

Este repositório contém exemplos práticos em Python utilizando o **Stellar SDK** para interagir com a **Stellar Testnet**, como referência técnica para o trabalho final da disciplina de Sistemas Distribuídos.

Os códigos demonstram como gerar chaves, financiar contas, verificar saldo, enviar pagamentos e consultar transações.

> Todos os exemplos utilizam a **testnet** da Stellar, onde não há risco financeiro.  
> As chaves privadas usadas aqui são apenas para teste.

---

## 📂 Estrutura do Repositório

```

stellar-examples/
│
├── 01\_generate\_keypair.py        # Gera par de chaves e financia conta na testnet
├── 02\_check\_balance.py           # Consulta saldo de uma conta
├── 03\_send\_payment.py            # Envia pagamento entre contas
└── 04\_check\_transaction.py       # Consulta detalhes de uma transação

````

---

## 🚀 Pré-requisitos

- **Python 3.8+** instalado.
- **Bibliotecas** necessárias:
```bash
pip install stellar-sdk requests
````

---

## 📜 Exemplos de Uso

### 1️⃣ Gerar par de chaves e financiar conta

```bash
python 01_generate_keypair.py
```

**Saída esperada:**

```
Public Key: GDSK5...
Secret Key: SC3Y2...
Conta financiada com sucesso!
```

---

### 2️⃣ Consultar saldo de uma conta

Edite `02_check_balance.py` e substitua `public_key` pela sua chave pública.

```bash
python 02_check_balance.py
```

**Saída esperada:**

```
Saldos da conta GDSK5...:
Tipo: native - Quantidade: 10000.0000000
```

---

### 3️⃣ Enviar pagamento

Edite `03_send_payment.py` e substitua:

* `secret_key_sender` pela chave privada da conta de origem.
* `public_key_receiver` pela chave pública do destinatário.

```bash
python 03_send_payment.py
```

**Saída esperada:**

```
Transação enviada!
{'_links': {...}, 'hash': 'abc123...', 'ledger': 123456, ...}
```

---

### 4️⃣ Consultar transação

Edite `04_check_transaction.py` e substitua `transaction_id` pelo hash da transação.

```bash
python 04_check_transaction.py
```

**Saída esperada:**

```
Detalhes da transação:
{'_links': {...}, 'id': 'abc123...', 'source_account': 'GDSK5...', ...}
```

---

## 📚 Referências

* [Documentação Oficial Stellar](https://developers.stellar.org/)
* [Stellar SDK para Python](https://github.com/StellarCN/py-stellar-base)
* [Horizon API — Testnet](https://horizon-testnet.stellar.org)
* [Stellar Laboratory](https://laboratory.stellar.org/)
```
