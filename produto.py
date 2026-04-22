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

estoque_mercearia = [
    # Repare: Mesmo produto, mas LOTES e VALIDADES diferentes
    Produto("Ovo maltine 190g", "01/05/2026", "LOTE-A1", "Matinal"),
    Produto("Nesquik", "01/06/2026", "L22", "Matinal"),
    Produto("Sucrilos Kellogs Power pops", "23/06/2026", "G90", "Matinal")
    Produto("Nestle Snow 620g", "27/07/2026", "Lote 1", "Matinal")
    
    # Quatá
    Produto("Quata", "08/05/2026", "Lote 1", "Laticínios/Matinal"),
    Produto("Quata", "11/05/2026", "Lote 2", "Laticínios/Matinal"),
    Produto("Quata", "13/07/2026", "Lote 3", "Laticínios/Matinal"),
    
    # Bebidas e Chás
    Produto("Cha Leao Guarana Garrafa", "29/04/2026", "Lote 1", "Matinal"),
    
    # Chocolates e Wafers
    Produto("Kinder Joy", "31/05/2026", "Lote Único", "Chocolates"),
    Produto("Chocolate Arcor Brigadeiro", "21/05/2026", "Lote Único", "Chocolates"),
    Produto("70% Cacau Cafe Espresso", "26/05/2026", "Lote Único", "Chocolates"),
    Produto("70% Cacau Caramel Macchiato", "25/05/2026", "Lote Único", "Chocolates"),
    Produto("Chocolate Lacta 40% Cacau", "30/05/2026", "Lote Único", "Chocolates"),
    Produto("Piraque Chocowafer", "02/05/2026", "Lote Único", "Chocolates"),
    
    # Cremes de Leite
    Produto("Porto Alegre Creme de Leite", "29/06/2026", "Lote 1", "Mercearia"),
    Produto("Porto Alegre Creme de Leite", "15/07/2026", "Lote 2", "Mercearia"),
    Produto("Leco Creme de Leite", "19/06/2026", "Lote Único", "Mercearia"),
    Produto("Camponesa Creme de Leite", "18/05/2026", "Lote 1", "Mercearia"),
    Produto("Camponesa Creme de Leite", "15/06/2026", "Lote 2", "Mercearia"),
    
    # Matinais e Cereais
    Produto("Nestle Snow 230g", "06/07/2026", "Lote Único", "Matinal"),
    Produto("Aveia em Flocos Yoki", "10/07/2026", "Lote Único", "Matinal"),
    Produto("Quaker Flocos Finos", "05/07/2026", "Lote Único", "Matinal"),
    Produto("Viver Bem Aveia Flocos Grossos 500g", "25/07/2026", "Lote Único", "Produtos Light"),
    
    # Mucilon
    Produto("Mucilon 600g Arroz e Aveia", "01/05/2026", "Lote 1", "Matinal"),
    Produto("Mucilon 600g Arroz e Aveia", "01/07/2026", "Lote 2", "Matinal"),
    Produto("Mucilon 600g Arroz e Aveia", "01/08/2026", "Lote 3", "Matinal"),
    Produto("Mucilon Multicereais 600g", "01/05/2026", "Lote 1", "Matinal"),
    Produto("Mucilon Multicereais 600g", "01/09/2026", "Lote 2", "Matinal"),
    
    # Torradas e Light
    Produto("Torrada Adria Light", "15/05/2026", "Lote Único", "Produtos Light")
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
    # --- FUNÇÃO DE FILTRO ---
def filtrar_por_setor(lista_produtos, setor_escolhido):
    print(f"\n--- FILTRANDO APENAS: {setor_escolhido.upper()} ---")
    encontrou = False
    for p in lista_produtos:
        if p.sub_setor.lower() == setor_escolhido.lower():
            prazo = p.dias_para_vencer()
            print(f"[{p.lote}] {p.nome} - Vence em {prazo} dias")
            encontrou = True
    
    if not encontrou:
        print("Nenhum produto encontrado neste setor.")

# Testando o filtro:
filtrar_por_setor(estoque_organizado, "Chocolates")
