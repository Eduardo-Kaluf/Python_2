"""AZV: Considere mudar o nome desse arquivo para models.py"""

"""AZV: Dataclass?"""
class Funcionario:
    def __init__(self, nome, cargo, salario) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    """O objetivo do __str__ é ser legível para usuários. Existe o
    __repr__ cujo objetivo é ser usado por desenvolvedores. Tenha como padrão
    sempre implementar o __repr__, o __str__ somente quando necessário"""

    def __str__(self) -> str:
        return(f"{self.nome}, {self.cargo}, {self.salario}")

"""AZV: Dataclass?"""
class Cliente:
    def __init__(self, nome, cep, telefone) -> None:
        self.nome = nome
        self.cep = cep
        self.telefone = telefone

    def __str__(self) -> str:
        return(f"{self.nome}, {self.cep}, {self.telefone}")

"""AZV: Dataclass?"""
class Produto:
    def __init__(self, nome, preco, validade) -> None:
        self.nome = nome
        self.preco = preco
        self.validade = validade

    def __str__(self) -> str:
        return(f"{self.nome}, {self.preco}, {self.validade}")
