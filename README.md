# Monad NFT Minter

Este é um script em Python para mintar NFTs na Monad Testnet na Magic Eden (ME) diretamente pelo smart contract, sem necessitar de acessar a interface da ME.

## Funcionalidades
- Carregamento seguro de credenciais a partir de um arquivo keystore.
- Envio de transações para mintar NFTs em um contrato pré-configurado.
- Tratamento de erros para falhas de conexão, transação ou keystore inválido.

## Pré-requisitos
- Python 3.7 ou superior.
- Bibliotecas necessárias:
  - `web3.py`
  - `eth-account`
- Um arquivo keystore;
- Acesso ao endpoint RPC da Monad Testnet (exemplo: via Alchemy).

### Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/<seu-usuario>/monad-nft-minter.git
   cd monad-nft-minter

## OBS:
- Adicionar a Data da transação em HEX;
- Adicionar o contrato do NFT;
- Trocar o RPC;
