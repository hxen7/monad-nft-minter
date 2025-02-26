#MINT de NFT na Magic Eden via Keystore

from web3 import Web3
from eth_account import Account
import time
import getpass

# Configuração do Web3 com o endpoint RPC da Monad Testnet
rpc_url = "XXXXXX1" 
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Verifica se está conectado
if not w3.is_connected():
    raise Exception("Não foi possível conectar ao RPC da Monad Testnet")

# Configurações da transação
chain_id = 10143  # ID da Monad Testnet
contract_address = "XXXXXX2"

# Dados da transação (hex fornecido)
transaction_data = "XXXXXX3"  #adicione a transation data

# Carrega e descriptografa o keystore
def load_account_from_keystore():
    keystore_file = input("Digite o caminho do arquivo keystore: ") 
    try:
        with open(keystore_file, "r", encoding="utf-8") as keyfile:
            encrypted_key = keyfile.read()
    except FileNotFoundError:
        print(f"Arquivo keystore não encontrado: {keystore_file}")
        raise
    except Exception as e:
        print(f"Erro ao ler arquivo keystore: {e}")
        raise

    password = getpass.getpass("Digite a senha do Keystore: ")

    print("Descriptografando Keystore...")
    try:
        private_key = Account.decrypt(encrypted_key, password)
        if isinstance(private_key, bytes):
            private_key = private_key.hex()
        account = Account.from_key(private_key)
        print(f"Endereço da conta: {account.address}")
        return account, private_key
    except ValueError:
        print("Senha incorreta ou keystore inválido.")
        raise
    except Exception as e:
        print(f"Erro ao descriptografar keystore: {e}")
        raise

# Função para mintar o NFT
def mint_nft(account, private_key):
    try:
        # Obtém o nonce da conta
        nonce = w3.eth.get_transaction_count(account.address)

        # Configura a transação
        tx = {
            "chainId": chain_id,
            "from": account.address,
            "to": contract_address,
            "data": transaction_data,
            "gas": 0x33147,  # Valor fornecido nas transações exemplo
            "gasPrice": 0xe87547000,  # Valor fornecido nas transações exemplo
            "nonce": nonce,
            "value": 0x0  # Sem envio de valor nativo
        }

        # Estima o gás (opcional, já que foi fornecido, mas boa prática)
        gas_estimate = w3.eth.estimate_gas(tx)
        tx["gas"] = gas_estimate  # Substitui pelo estimado, se necessário

        # Assina a transação
        signed_tx = w3.eth.account.sign_transaction(tx, private_key)

        # Envia a transação
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"Transação enviada! Hash: {w3.to_hex(tx_hash)}")

        # Aguarda a confirmação
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        if tx_receipt.status == 1:
            print("NFT mintado com sucesso!")
        else:
            print("Falha na transação.")
    except Exception as e:
        print(f"Erro ao mintar NFT: {str(e)}")

# Executa o bot
if __name__ == "__main__":
    print(f"Iniciando bot para mintar NFT na Monad Testnet em {time.ctime()}")
    try:
        account, private_key = load_account_from_keystore()
        mint_nft(account, private_key)
    except Exception as e:
        print(f"Erro ao executar o bot: {str(e)}")
