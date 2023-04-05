#por enquando traduz só a números de base 10!
print ("Ben-vindo ao Tradutor de Bases numéricas!")
num = input("Qual o número a traduzir?\n")
base = int(input("Qual a base do número a traduzir?\n"))
base_nov = int(input("A qual base quer traduzir o número?\n"))
size = len(num)
count = size
num_b10 = 0
algarithm = 0
while count >= 1:
  algarithm = int(num[size - count])
  num_b10 = algarithm*(base**(count-1)) + num_b10
  count -= 1
print (f"O número traduzido em base 10 é:\n{new_num}")

if base_nov == 2:
    num_b10