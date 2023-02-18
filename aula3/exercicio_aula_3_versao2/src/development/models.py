from dataclasses import dataclass
from decimal import Decimal
from datetime import date


@dataclass
class Funcionario:
    identificador: str
    nome: str
    cargo: str
    salario: Decimal

    def __repr__(self) -> str:
        return (f"""IDENTIFICADOR: {self.identificador} //\n   NOME: {self.nome}
                 \n   CARGO: {self.cargo}\n   SALARIO: {self.salario}\n""")


@dataclass
class Cliente:
    identificador: str
    nome: str
    cep: str
    telefone: str

    def __repr__(self) -> str:
        return (f"""IDENTIFICADOR: {self.identificador} //\n   NOME: {self.nome}
                 \n   CEP: {self.cep}\n   TELEFONE: {self.telefone}\n""")


@dataclass
class Produto:
    identificador: str
    nome: str
    preco: Decimal
    validade: date

    def __repr__(self) -> str:
        return (f"""IDENTIFICADOR: {self.identificador} //\n   NOME: {self.nome}
                 \n   PRECO: {self.preco}\n   VALIDADE: {self.validade}\n""")
