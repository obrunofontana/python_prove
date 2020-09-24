#Crie uma aplicação Python com uma estrutura de classes que atenda aos seguintes requisitos:
#Uma PESSOA precisa realizar um EMPRÉSTIMO de EQUIPAMENTOS de manutenção predial numa companhia especializada.
#Ela pode emprestar uma LISTA DE EQUIPAMENTOS, com data de devolução pré-estabelecida no momento do empréstimo.
import datetime

#Pessoa
class Client:
    def __init__(self, id, name):
        self.id = id
        self.name = name

#Emprestimo
class Lending:
    def __init__(self, id, client, equipements, returnDate):
        self.id = id
        self.client = client
        self.equipements = equipements
        self.returnDate = returnDate

    @property
    def show(self):
        return print('asiodjasdhiuo')

#Equipamento
class Equipment:
    def __init__(self, id, description):
        self.id = id
        self.description = description

equipment_one = Equipment(1, 'Martelo')
equipment_two = Equipment(2, 'Parafuso')
equipment_three = Equipment(3, 'Prego')
equipment_four = Equipment(4, 'Furadeira')

client_one = Client(1, 'Bruno')
client_two = Client(2, 'Dougras')

lending = Lending(1, client_one, [equipment_two, equipment_four], datetime.datetime(2020, 10, 20))

print(f'O emprestimo com o codigo {lending.id} esta relacionado ao cliente {lending.client.name} '
      f' \n o mesmo emprestou: {lending.equipements[0].description} e {lending.equipements[1].description} com previsao de retorno: {lending.returnDate} ')
