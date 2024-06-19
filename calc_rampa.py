import math

# Definir a classe Rampa
class Rampa:
    def __init__(self, num_degraus=None, altura_degrau=None, inclinacao_porcentagem=None, desnivel=None, 
                 projecao_horizontal=None, num_patamares=None, comprimento_patamar=None):
        # Atributos da classe
        self.num_degraus = num_degraus
        self.altura_degrau = altura_degrau
        self.inclinacao_porcentagem = inclinacao_porcentagem
        self.desnivel = desnivel
        self.projecao_horizontal = projecao_horizontal
        self.num_patamares = num_patamares
        self.comprimento_patamar = comprimento_patamar
        
    # Método para calcular o número de degraus
    def calcular_numero_degraus(self):
        # Se o desnível e a altura do degrau são fornecidos, calcula o número de degraus
        if self.desnivel is not None and self.altura_degrau is not None:
            return round(self.desnivel / self.altura_degrau)
        # Se o número de degraus é fornecido, retorna ele
        elif self.num_degraus is not None:
            return self.num_degraus
        else:
            return None
        
    # Método para calcular o comprimento da rampa
    def calcular_comprimento_rampa(self):
        # Se o desnível e a inclinação são fornecidos, calcula o comprimento da rampa
        if self.desnivel is not None and self.inclinacao_porcentagem is not None:
            inclinacao_rad = math.atan(self.inclinacao_porcentagem / 100)
            comprimento_rampa = self.desnivel / math.sin(inclinacao_rad)
            # Adiciona o comprimento dos patamares, se houver
            comprimento_total = comprimento_rampa + (self.num_patamares * self.comprimento_patamar if self.num_patamares and self.comprimento_patamar else 0)
            return round(comprimento_total, 2)
        else:
            return None
        
    # Método para calcular a inclinação da rampa em porcentagem
    def calcular_inclinacao_porcentagem(self):
        # Se o desnível e a projeção horizontal são fornecidos, calcula a inclinação
        if self.desnivel is not None and self.projecao_horizontal is not None:
            inclinacao_porcentagem = (self.desnivel * 100) / self.projecao_horizontal
            return round(inclinacao_porcentagem, 2)
        else:
            return None
        
    # Método para calcular o desnível a ser vencido
    def calcular_desnivel(self):
        # Se o número de degraus e a altura do degrau são fornecidos, calcula o desnível
        if self.num_degraus is not None and self.altura_degrau is not None:
            self.desnivel = self.num_degraus * self.altura_degrau
        # Se a inclinação e a projeção horizontal são fornecidas, calcula o desnível
        elif self.inclinacao_porcentagem is not None and self.projecao_horizontal is not None:
            self.desnivel = (self.inclinacao_porcentagem / 100) * self.projecao_horizontal
        return round(self.desnivel, 2) if self.desnivel is not None else None

# Função para exibir as opções de cálculo
def exibir_opcoes_calculo():
    print("Escolha a propriedade que deseja calcular:")
    print("1 - Número de degraus")
    print("2 - Comprimento da rampa")
    print("3 - Inclinação da rampa")
    print("4 - Desnível a ser vencido")

# Exemplo de uso
exibir_opcoes_calculo()
opcao = int(input("Escolha uma opção de cálculo (1-4): "))
rampa = Rampa()

if opcao == 1:
    # Calcular número de degraus
    desnivel = float(input("Informe o desnível a ser vencido (em metros): "))
    altura_degrau = float(input("Informe a altura de cada degrau (em metros): "))
    rampa.desnivel = desnivel
    rampa.altura_degrau = altura_degrau
    print("Número de degraus:", rampa.calcular_numero_degraus())
elif opcao == 2:
    # Calcular comprimento da rampa
    resposta = input("Você tem a altura dos degraus e a quantidade de degraus? (sim/não): ").lower()
    if resposta == "sim":
        altura_degrau = float(input("Informe a altura de cada degrau (em metros): "))
        num_degraus = int(input("Informe o número de degraus: "))
        rampa.altura_degrau = altura_degrau
        rampa.num_degraus = num_degraus
        desnivel = rampa.calcular_desnivel()
        print("O desnível a ser vencido é:", desnivel, "metros")
    else:
        desnivel = float(input("Informe o desnível a ser vencido (em metros): "))
        inclinacao_porcentagem = float(input("Informe a inclinação da rampa em porcentagem: "))
        rampa.desnivel = desnivel
        rampa.inclinacao_porcentagem = inclinacao_porcentagem
    
    num_patamares = int(input("Informe o número de patamares: "))
    comprimento_patamar = float(input("Informe o comprimento do patamar (em metros): "))
    rampa.num_patamares = num_patamares
    rampa.comprimento_patamar = comprimento_patamar
    print("Comprimento da rampa:", rampa.calcular_comprimento_rampa(), "metros")
elif opcao == 3:
    # Calcular inclinação da rampa
    desnivel = float(input("Informe o desnível a ser vencido (em metros): "))
    projecao_horizontal = float(input("Informe a projeção horizontal (em metros): "))
    rampa.desnivel = desnivel
    rampa.projecao_horizontal = projecao_horizontal
    inclinacao = rampa.calcular_inclinacao_porcentagem()
    print("Inclinação da rampa:", inclinacao, "%")
elif opcao == 4:
    # Calcular desnível a ser vencido
    resposta = input("Você tem a altura dos degraus e a quantidade de degraus? (sim/não): ").lower()
    if resposta == "sim":
        altura_degrau = float(input("Informe a altura de cada degrau (em metros): "))
        num_degraus = int(input("Informe o número de degraus: "))
        rampa.altura_degrau = altura_degrau
        rampa.num_degraus = num_degraus
        print("O desnível a ser vencido é:", rampa.calcular_desnivel(), "metros")
    else:
        inclinacao_porcentagem = float(input("Informe a inclinação da rampa em porcentagem: "))
        projecao_horizontal = float(input("Informe a projeção horizontal (em metros): "))
        rampa.inclinacao_porcentagem = inclinacao_porcentagem
        rampa.projecao_horizontal = projecao_horizontal
        print("O desnível a ser vencido é:", rampa.calcular_desnivel(), "metros")
