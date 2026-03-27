class SistemaDelivery:
    def __init__(self):
        self.restaurantes = []

    # MENU PRINCIPAL
    def menu_principal(self):
        while True:
            print("\n=== SISTEMA DELIVERY ===")
            print("1 - Área do Usuário")
            print("2 - Área do Restaurante")
            print("0 - Sair")