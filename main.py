from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Joana', 93)

p1.comer('uva')
p1.parar_comer()
p1.parar_de_falar()
p1.falar('POO')
p1.parar_de_falar()
p1.falar('temperatura')
p1.comer('arroz')

print(p1.get_ano_nascimento())

print(p2.get_ano_nascimento())