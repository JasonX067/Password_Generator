import random
import string

tam = int(input("Qual vai ser o tamanho da senha?"))

def generate_password (length):

  characteres = string.ascii_letters + string.digits + string.punctuation

  password = ''.join(random.choice(characteres) for i in range(length))
  
  return password

print(generate_password(tam))

  