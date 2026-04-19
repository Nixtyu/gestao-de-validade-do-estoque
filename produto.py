from datetime import datetime

class Produto:
    def __init__(self, nome, data_validade, lote, sub_setor):
        self.nome = nome
        self.data_validade = datetime.strptime(data_validade, '%d/%m/%Y')
        self.lote = lote  # Agora o sistema diferencia o lote!
        self.sub_setor = sub_setor

    def dias_para_vencer(self):
        hoje = datetime.now()
        diferenca = self.data_validade - hoje
        return diferenca.days

# Simulação:
estoque_mercearia = [
    # Repare: Mesmo produto, mas LOTES e VALIDADES diferentes
    Produto("Chocolate Barra 90g", "10/05/2026", "LOTE-A1", "Chocolates"),
    Produto("Chocolate Barra 90g", "20/06/2026", "LOTE-B2", "Chocolates"),
    
    Produto("Cereal Matinal 500g", "15/05/2026", "L22", "Matinal"),
    Produto("Granola Light", "19/04/2026", "G90", "Produtos Light")
]

print(f"--- RELATÓRIO SETOR: MERCEARIA ---")

for p in estoque_mercearia:
    prazo = p.dias_para_vencer()
    # Usando o lote para identificar exatamente qual caixa precisa sair primeiro
    print(f"Produto: {p.nome} | Lote: {p.lote} | Vence em: {prazo} dias.")
    # Função para ordenar o estoque (Primeiro que Vence, Primeiro que Sai)
# O Python vai olhar a data_validade de cada um e colocar o menor prazo no topo
estoque_ordenado = sorted(estoque_mercearia, key=lambda x: x.data_validade)

print("\n--- ROTEIRO DE REPOSIÇÃO (SISTEMA PVPS) ---")
for p in estoque_ordenado:
    prazo = p.dias_para_vencer()
    if prazo <= 7:
        aviso = "⚠️ PUXAR PARA FRENTE AGORA!"
    else:
        aviso = "✅ OK"
        
    print(f"{aviso} | {p.nome} (Lote: {p.lote}) - Faltam {prazo} dias")
