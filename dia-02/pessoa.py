class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def dirigir(self, veiculo:str) -> None:
        print(f"Dirigindo um(a) {veiculo}")
    
    def cantar(self) -> None:
        print("lalalala")

    def apresentar_idade(self) -> int:
        print(self.idade)