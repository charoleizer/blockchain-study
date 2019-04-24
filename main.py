#https://medium.com/@felipemfp/entendendo-como-funciona-uma-blockchain-com-python-4e5a66f09e16

from blockchain import Blockchain


if __name__ == '__main__':
    blockchain = Blockchain()

    #O primeiro Nonce e hask que aparece, são os dados inciais, necessário para o Start.
    #TODO Verificar se não há uma outra forma de dar o start.
    blockchain.add_new_block('1')
    blockchain.add_new_block('1')
    blockchain.add_new_block('2')

    print(blockchain.get_all())