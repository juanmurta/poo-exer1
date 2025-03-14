import time
import pyautogui
import pyperclip


class MeuRobo:

    def __init__(self, tempo_espera):
        self.tempo_espera = tempo_espera
        pyautogui.PAUSE = 1

    def abrir_programa(self, nome_programa):
        pyautogui.press("win")
        pyautogui.write(nome_programa)
        pyautogui.press("enter")

    def entrar_site(self, site):
        self.escrever_enter(site)
        self.aguardar()

    def escrever_enter(self, texto):
        pyperclip.copy(texto)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    def aguardar(self):
        time.sleep(self.tempo_espera)

    def pesquisar_no_campo(self, texto):
        self.escrever_enter(texto)
        self.aguardar()

    def clicar(self, x, y, botao='left'):
        pyautogui.click(x, y, button=botao)

    def pegar_posicao(self):
        for i in range(5):
            print(f'Pegando posicao em {5 - i} segundos')
            time.sleep(1)
        print(pyautogui.position())

    def extrair_link(self, x, y):
        self.clicar(x, y, botao='right')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('enter')

        texto = pyperclip.paste()
        print(texto)


robo = MeuRobo(2)
robo.abrir_programa('chrome')
robo.entrar_site('https://www.google.com')
robo.clicar(x=2685, y=587)
robo.pesquisar_no_campo('classe')
robo.aguardar()
robo.extrair_link(x=2685, y=587)
