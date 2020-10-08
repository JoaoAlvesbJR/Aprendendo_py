class Computador:
    def __init__(self, placa_mae, ram, hd, monitor):
        self.placa_mae = placa_mae
        self.ram = ram
        self.hd = hd
        self.monitor = monitor

    def Ligar (self):
        print("Estou ligando")

    def Desligar (self):
        print("Estou desligando")

    def ExibirInfo(self):
        print(self.placa_mae, self.ram, self.hd, self.monitor)

computador1 = Computador("A320", "8", "1T", "HQ 75") 
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInfo()
