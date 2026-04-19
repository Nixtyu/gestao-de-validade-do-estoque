from datetime import datetime

class Produto:
    def __init__(self, nome, codigo_barras, data_validade, setor):
        self.nome = nome
        self.codigo_barras = codigo_barras
        self.data_validade = datetime.strptime(data_validade, '%d/%m/%Y')
        self.setor = setor

    def dias_para_vencer(self):
        hoje = datetime.now()
        diferenca = self.data_validade - hoje
        return diferenca.days

# Testando o código
p1 = Produto("Leite Integral 1L", "789123456", "25/04/2026", "Laticínios")
print(f"O produto {p1.nome} vence em {p1.dias_para_vencer()} dias.")
