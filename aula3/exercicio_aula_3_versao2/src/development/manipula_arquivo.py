from typing import List
from arquivo_conexoes import ArquivoConexoes


class ManipulaArquivo:
    def __init__(self, arquivo: str, classe) -> None:  # Pesquisar o que usar no type hint de classes
        self.arquivo = arquivo
        self.classe = classe
        self.conexao = ArquivoConexoes(self.arquivo)

    def insere(self, objeto) -> None:
        arquivo = self.conexao.abrir("a")
        informacoes = "//".join(objeto.__dict__.values())
        arquivo.write(f"{informacoes}\n")
        arquivo.close()
        self.conexao.compactar()

    def consulta_especifica(self, identificador: str) -> object:  # Pensar em nome melhor para o método
        arquivo = self.conexao.abrir()
        for linha in arquivo:
            linha = linha.replace("\n", "").split("//")
            if identificador == linha[0]:
                retorno = self.classe(*linha)
            else:
                retorno = "Nenhum usuário com o identificador especificado"
            arquivo.close()
            self.conexao.compactar()
            return retorno

    def consulta_geral(self) -> List[object]:
        arquivo = self.conexao.abrir()
        objetos = []
        for linha in arquivo:
            linha = linha.replace("\n", "").split("//")
            objeto = self.classe(*linha)
            objetos.append(objeto)
        arquivo.close()
        self.conexao.compactar()
        return objetos

    def remove(self, identificador: str) -> None:
        arquivo = self.conexao.abrir()
        conteudo = []
        for linha in arquivo:
            linha = linha.split("//")
            if identificador == linha[0]:
                continue
            conteudo.append(linha)
        arquivo.close()
        self.conexao.compactar()
        arquivo = self.conexao.abrir("w")  # implementar arquivo temporario para não ter risco de corromper
        for y in conteudo:
            y = "//".join(y)
            arquivo.write(y)
        arquivo.close()
        self.conexao.compactar()
