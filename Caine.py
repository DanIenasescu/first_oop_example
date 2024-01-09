class Caine:
    def __init__(self, rasa, varsta):
        self.rasa = rasa
        self.varsta = varsta

    def latra(self):
        print("Ham!")


if __name__ == "__main__":
    cainele_meu = Caine("Labrador", 3)

    # Accesarea atributelor și apelarea metodelor
    print(cainele_meu.rasa)
    print(cainele_meu.varsta)
    cainele_meu.latra()
