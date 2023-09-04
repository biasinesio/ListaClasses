'''1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado
“calcular_area” que retorna a área do círculo.'''

class Circulo:
    def calcular_area(self, raio):
        self.raio = raio
        area = 3.14 *(self.raio ** 2)
        return area
    
cal = Circulo()
print("\n","A area do circulo cujo raio = 4, e igual a:", cal.calcular_area(4),"\n")

'''2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
chamado “detalhes” que retorna uma string com as informações do livro.'''

class Livro:
    def detalhes (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        return titulo + autor 

info = Livro()
print (info.detalhes("Titulo: O codigo da Vinci ", "Autor: Dan Brown"),"\n")

'''3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
chamado “calcular_area” que retorna a área do retângulo.'''

class Retangulo:
    def calcular_area(self, base, altura):
        self.base = base
        self.altura = altura
        return base * altura
    
calc = Retangulo()
print ("O valor da area de um retangulo cuja base = 5 e altura = 7, e igual a:", calc.calcular_area(5 , 7),"\n")

'''4. Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
métodos “depositar” e “sacar” para manipular o saldo.'''

class ContaBancaria:
    def depositar (self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
        return titular

    def sacar (self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
        return saldo 

manipular = ContaBancaria()
print ("Depositar para o", manipular.depositar(1500, "Titular: Joao da Silva"))
print ("Sacar. Saldo =", manipular.sacar(1500, " Titular: Joao da silva"),"\n")


'''5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
chamado “falar” que imprime uma mensagem com o nome da pessoa.'''
 
class Pessoa:
    def falar (self, nome, idade):
        self.nome = nome
        self.idade = idade
        print ("Nome:", self.nome)
        print ("Idade:", self.idade)
        return nome, idade
    
falando = Pessoa()
print (falando.falar("Ola Joao", 28), "\n")



'''6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).'''

class Produto:
  def calcular_total (self, nome, preco, quantidade):
       self.nome = nome
       self.preco = preco
       self.quantidade = quantidade
       return (preco * quantidade)
  
cal = Produto()
print ("O valor total do produto e: ", cal.calcular_total("Camisa", 23, 7),"\n")


'''7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método
chamado “detalhes” que retorna uma string com as informações do carro.'''

class Carro:
    def detalhes (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        return marca + modelo + ano
    
info = Carro()
print ("Os dados do carro sao: ", info.detalhes("Fiat, ", "Palio, ", "1994"),"\n")
    
       


'''8. Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
“calcular_media” que retorna a média das notas do aluno.'''

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        if len (self.notas) == 0:
            return 0.0
        soma = sum(self.notas)
        media = soma / len(self.notas)
        return media

notas_aluno = [8.5, 9.0, 7.5, 8.0]
aluno = Aluno ("Pedro", notas_aluno)
media = aluno.calcular_media()
print (f"A media das notras do aluno {aluno.nome} e {media}", "\n")

'''9. Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”. Implemente um
método chamado “calcular_perimetro” que retorna o perímetro do triângulo.'''

class Triangulo:
    def calcular_perimetro(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        return lado1 + lado2 + lado3

perimetro = Triangulo()
print ("O perimetro do triangulo e: ", perimetro.calcular_perimetro(5, 5, 9), "\n")

'''10. Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um
método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário
do funcionário.'''
 
class Funcionário:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento >  0:
            self.salario += (self.salario * percentual_aumento /100)
            
funcionario1 = Funcionário("João", 5000, "Analista")
print(f"Salario antes do aumento: R${funcionario1.salario}")
funcionario1.aumentar_salario(10)
print(f"Novo Salario: R${funcionario1.salario}")