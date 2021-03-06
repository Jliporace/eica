from braser.vitollino import Vitollino, Actor
from .mundo import Mundo
from .roda import Roda
from .chaves import Chaves
from .eica import Jogo, Imagem, Botao
from .inventario import Inventario, MonoInventario
from . import Folha, Ponto, __version__


class JogoEica(Vitollino):
    JOGO = None
    """Essa  é a classe Jogo que recebe os poderes da classe Circus de poder criar um jogo"""

    def __init__(self, gid):
        super().__init__(1000, 800, alpha=True)  # super é invocado aqui para preservar os poderes recebidos do Circus
        Eica()


class Menu(Jogo):
    """Essa  é a classe Jogo que recebe os poderes da classe Circus de poder criar um jogo"""

    def __init__(self, jogo):
        super().__init__()  # super é invocado aqui para preservar os poderes recebidos do Circus
        Botao(Folha.itens, Ponto(15, 15), 36 + 1, jogo.ativaroda, self, escala=(0.6, 0.6))
        Botao(Folha.itens, Ponto(735+50, 15), 36 + 3, jogo.ativachaves, self, escala=(0.6, 0.6))


class Eica(Jogo):
    """Essa  é a classe Jogo que recebe os poderes da classe Circus de poder criar um jogo"""

    def __init__(self):
        super().__init__()  # super é invocado aqui para preservar os poderes recebidos do Circus
        Imagem(Folha.eica, Ponto(-500, -200), self, (1.8, 1.8))
        ''''''
        self.mundo = Mundo(x=-150)  # MonoInventario(lambda _=0: None)
        self.homem = Homem(self.clica)
        self.roda = Roda(acao=self.homem.esconde)
        self.chaves = Chaves(y=100)
        self.menu = Menu(self)

    def ativaroda(self, item=None):
        self.roda.ativa()

    def ativachaves(self, item=None):
        self.chaves.ativa()

    def clica(self, item):
        """Aqui colocamos as imagems na tela do jogo"""
        self.mundo.ativa()
        # self.ativa()

    def preload(self):
        """Aqui no preload carregamos as imagens de ladrilhos dos items usados no jogo"""
        self.spritesheet(*Folha.animal.all())
        self.spritesheet(*Folha.itens.all())
        self.spritesheet(*Folha.minitens.all())


class Homem(Jogo):
    """Essa  é a classe Homem que controla os personagens do jogo"""

    def __init__(self, acao=None, frame=2, x=250, y=300):
        super().__init__()
        acao = acao or self._click
        # Imagem(Folha.eica, Ponto(0, 0), self, (1.6, 1.6))
        self.homem = Botao(Folha.sapiens, Ponto(x=250, y=450), frame, acao, self, (0.1, 0.1))

    def esconde(self, ativa=False):
        """Esconde o Homem"""
        print("homem action Esconde", ativa)
        self.homem.botao.visible = ativa

    def _click(self, _=None, __=None):
        """Ativa o jogo do Mundo"""
        print("homem action", JogoEica.JOGO.mundo)
        self.ativa()
        JogoEica.JOGO.mundo.ativa(self.ativo)


def main(gid=None):
    # JogoEica.JOGO = JogoEica(gid)
    JogoEica.JOGO = JogoEica(gid)
    return __version__


if __name__ == "__main__":
    main()
