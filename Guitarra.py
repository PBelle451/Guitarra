from abc import ABC, abstractmethod
class Instrumento(ABC):
    @abstractmethod
    def cordas(self):
        pass
    def trastes(self):
        pass

class Guitarra(Instrumento):
    def cordas(self):
        qtd = int(input("Insira a quantidade de cordas da guitarra: "))
        if qtd < 6 or qtd > 12:
            print("ERRO")
        else:
            print(f"A guitarra tem {qtd} cordas")

    def trastes(self):
        qtd = int(input("Insira a quantidade de trastes da guitarra: "))
        if qtd < 22 or qtd > 24:
            print("ERRO")
        else:
            print(f"A guitarra tem {qtd} trastes")

class Baixo(Instrumento):
    def cordas(self):
        qtd = int(input("Insira a quantidade de cordas do baixo: "))
        if qtd < 4 or qtd > 12:
            print("ERRO")
        else:
            print(f"O baixo tem {qtd} cordas")

    def trastes(self):
        qtd = int(input("Insira a quantidade de trastes do baixo: "))
        if qtd < 22 or qtd > 24:
            print("ERRO")
        else:
            print(f"O baixo tem {qtd} trastes")

if __name__ == '__main__':
    g1 = Guitarra()
    b1 = Baixo()
    g1.cordas()
    g1.trastes()
    b1.cordas()
    b1.trastes()