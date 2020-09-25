#Escreva uma classe Python que contenha um método que faça a validação da força da senha fornecida pelo usuário.
# Uma senha forte deve atender aos seguintes critérios:

#Possuir ao menos 1 caractere numérico;
#Possuir ao menos 1 caractere especial;
#Ao chamar o método o programa deve retornar se a senha é valida ou não.

def validatePassword(password):
    valid = 'Senha é INVÁLIDA'

    if (any(char.isdigit() for char in password)) and ((any(not char.isalnum() for char in password))):
        valid = 'Senha é VÁLIDA'

    return valid


print(f'A senha é: {validatePassword("bruno1!") }')
