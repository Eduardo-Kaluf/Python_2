import os
import gzip
import shutil
from configs import FILES


class ArquivoConexoes:
    def __init__(self, arquivo) -> None:
        self.arquivo = arquivo

    def abrir(self, modo: str = "r", descompactar: bool = True):  # Pesquisar o que usar no type hint de Arquivos
        if descompactar:
            self.descompactar()
        arquivo = open(os.path.join(FILES, self.arquivo), f"{modo}")
        return arquivo

    def descompactar(self) -> None:
        with gzip.open(os.path.join(FILES, f"{self.arquivo}.log.gz"), "rb") as f_in:
            with open(os.path.join(FILES, f"{self.arquivo}"), "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

    def compactar(self) -> None:
        arquivo = self.abrir("r", False)
        with gzip.open(os.path.join(FILES, f"{self.arquivo}.log.gz"), "wb") as zipped:
            for linha in arquivo:
                zipped.write(linha.encode())
            arquivo.close()
        os.remove(os.path.join(FILES, f"{self.arquivo}"))
