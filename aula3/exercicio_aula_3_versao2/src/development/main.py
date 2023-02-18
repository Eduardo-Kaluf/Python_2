from manipulaArquivo import ManipulaArquivo
from models import Funcionario


manip = ManipulaArquivo("func.txt", Funcionario)

jonas = Funcionario("2", "Jonas", "Gerente", "5000")
joanete = Funcionario("10", "Joanete", "Caixa", "2500")
joaozinho = Funcionario("Batman", "Joaozinho", "Ascensorista", "1000")
jorger = Funcionario("1000", "Jorger", "Presidente", "99999")

manip.insere(jonas)
manip.insere(joanete)
manip.insere(joaozinho)
manip.insere(jorger)


print(manip.consulta_especifica("2"))
print(manip.consulta_especifica("Batman"))


func = manip.consulta_geral()
for funcionario in func:
    print(funcionario)


manip.remove("1000")

print(manip.consulta_especifica("1000"))
