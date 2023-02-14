import os
from zipfile import ZipFile # AZV: Existem libs mais simples. Já tentou gzip?

"""AZV: BASE_DIR ficaria melhor se inserido em um arquivo de configuração
Pq 'realpath'? Vc espera que criem atalho do seu código, por exemplo?
Geralmente não esperamos (e não queremos), por isso o uso do 'abspath'.
'realpath' é interessante quando vc cria um software desktop."""
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

"""AZV: Pq 'abrir_arquivo' está fora da classe? Não faz sentido.
Vc pode ter uma classe responsável pela "conexão" e uma classe
responsável pela "manipulação". A primeira resolve abrir o arquivo com o
tipo certo, fechar o arquivo, compactar e descompactar. A segunda lida com
os dados. Quanto a conexão com o arquivo, o problema é maior do que parece: Arquivos
só podem receber uma única conexão por vez. Leia sobre o padrão de projeto Singleton:
https://refactoring.guru/design-patterns/singleton.
Quanto a divisão da estrutura em 'responsabilidades', leia sobre o padrão de
projeto Builder: https://refactoring.guru/design-patterns/builder.
"""
def abrir_arquivo(arquivo, modo):
    arquivo = open(os.path.join(BASE_DIR, arquivo), f"{modo}")
    return arquivo

"AZV: Dois espaços acima da classe de acordo com o PEP8"
"AZV: Manipula oq? Esse nome podia ser melhor"
class Manipula:
    def __init__(self, arquivo, objeto) -> None:
        self.arquivo = arquivo
        self.objeto = objeto
        """AZV: A ideia é bem boa, mas eu mudaria o nome do atributo. O que existe
        aqui não é um objeto e sim um classe. Vc pretende gerar objetos, é diferente.
        O nome da variável me fez perder uns 30seg da vida tentando entender pq vc
        mandaria um objeto pra cá e faz um unpack mais pra baixo. Pra entender eu precisei
        olhar o main.py (e isso não é bom). Talvez se tivesse um type hint ficaria mais
        claro."""

    """AZV: Se o nome da classe for melhor, vc não precisa repetir 'arquivo_' no nome dos
    métodos, já que todos tratam de arquivos. Setter geralmente são nomeados 'set_*' e 
    nesse caso, mesmo que vc usasse a nomenclatura certa, o nome seria enganoso, já que
    a ideia de um setter é alterar o estado de um atributo. Entendo que o motivo é o conceito
    semelhante, mas no código pode levar a interpretação incorreta. Mesma coisa pro getter."""
    def arquivo_setter(self, conteudo) -> None:
        arquivo = abrir_arquivo(self.arquivo, "a")
        arquivo.write(conteudo + "\n")
        arquivo.close()

    """AZV: Esse traz todas as informações do arquivo. Mas e se eu quiser um específico?
    Por exemplo: Dados do CPF 12, no caso do cliente? Eu vou ter que ver o arquivo inteiro?
    Seria legal ter um método pra trazer apenas 1 objeto. De preferência com um index."""
    def arquivo_getter(self): # Esta correto devolver 1 objeto para cada linha do arquivo? 
                              # AZV: Sim.
        arquivo = abrir_arquivo(self.arquivo, "r")
        objetos = []
        for linha in arquivo:
            linha = linha.replace("\n", "").split(",")
            objeto = self.objeto(*linha)
            objetos.append(objeto)
        arquivo.close()
        return objetos

    def arquivo_delete(self, nome):
        arquivo = abrir_arquivo(self.arquivo, "r")
        conteudo = []
        for linha in arquivo:
            linha = linha.split(",")
            if nome in linha:
                continue
            conteudo.append(linha)
        arquivo.close()
        arquivo = abrir_arquivo(self.arquivo, "w")  #implementar arquivo temporario para não ter risco de corromper
        for y in conteudo:
            y = ",".join(y)
            arquivo.write(y)
        arquivo.close()
        return

    """AZV: Se os arquivos estão compactados (eventualmente vc compacta),
    como leio eles novamente? O processo de compactação deveria ser transparente
    pro desenvolvedor que usará tua classe. E se o desenvolvedor esquecer que precisa
    compactar? O processo correto seria:
    1) Está TUDO compactado;
    2) Preciso de informação;
    3) Descompacto arquivo e disponibilizo descompactado;
    4) Faço minha magia;
    5) Compacto novamente."""
    def compacta(self): # Foi a maneira que consegui implementar o compactamento
        zipped = ZipFile(f"{self.arquivo}.zip", "w")
        for root, dirs, files in os.walk(BASE_DIR):
            for file in files:
                if self.arquivo in file.split("/"):
                    zipped.write(os.path.relpath(os.path.join(root, file)))
        return 
