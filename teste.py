from models.cliente import Cliente
from models.conta import Conta


carlos: Cliente = Cliente("Carlos", "carlos.alves@dcx.ufpb.br", "133.049.914-09", "07/12/2004")
fulano: Cliente = Cliente("Fulano", "fulaninho123@gmail.com", "400.228.999-22", "07/10/2000")

#print(carlos)
#print(fulano)

contac: Conta = Conta(carlos)
contaf: Conta = Conta(fulano)

#print(contac)
#print(contaf)
