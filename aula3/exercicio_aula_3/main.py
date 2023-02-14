"""Considere separar a estrutura do teu sistema em pastas:
/
|-- src
|-- docs
|-- test

Em 'src' ficariam seu códigos de forma geral. Dentro também estaria
Separado em pastas, de acordo com a necesidade.
Em 'docs' ficaria a documentação. A descrição do exercício, por
exemplo, iria pra lá.
Em 'test' irão seus testes, que ainda não existem, mas existirão.
"""
from manipula import Manipula
from classes import Funcionario


manip = Manipula("func.txt", Funcionario)

"""AZV: Receber uma string pra adicionar no arquivo é feio. Receba um objeto, deixe
a classe responsável pela manipulação estruturar."""
manip.arquivo_setter("Jonas,Gerente,1200")  # Adicionando linha no arquivo
"""AZV: E se tiver dois Jonas? E se fosse Enzo?"""
manip.arquivo_delete("Jonas")  # Deletando a linha que o nome Jonas aparece
func = manip.arquivo_getter()  # Pegando objetos do arquivo

"""AZV: Evite usar o __str__ pra entregar informações pro teu usuário."""
for funcionario in func:  # Mostrando na tela as informações dos objetos
    print(funcionario)

"""AZV: Vish"""
manip.compacta()  # Compactando arquivo para Zip


"""AZV: CSV é feio hehe. O que impede o usuário de parar de usar o teu software
e começar a usar o Excel? Vc vai mesmo querer competir com a Microsoft?"""

# Conteudo inicial do arquivo
"""Joao Pereira,Gerente,3000
Joana,Funcionario generico,500
Joaninha,Funcionario generico,1200"""
