from datetime import datetime

class Produto:
    def __init__(self, nome, data_validade, lote, sub_setor):
        self.nome = nome    
        self.data_validade = datetime.strptime(data_validade, '%d/%m/%Y')
        self.lote = lote  
        self.sub_setor = sub_setor

    def dias_para_vencer(self):
        hoje = datetime.now()
        # Calcula a diferença de dias ignorando as horas para ser mais preciso
        diferenca = self.data_validade.date() - hoje.date()
        return diferenca.days

# Seu estoque real cadastrado
estoque_mercearia = [
    Produto("Ovo maltine 190g", "01/05/2026", "LOTE-A1", "Matinal"),
    Produto("Nesquik", "01/06/2026", "L22", "Matinal"),
    Produto("Sucrilos Kellogs Power pops", "23/06/2026", "G90", "Matinal"),
    Produto("Nestle Snow 620g", "27/07/2026", "Lote 1", "Matinal"),
    Produto("Quata", "08/05/2026", "Lote 1", "Laticínios/Matinal"),
    Produto("Quata", "11/05/2026", "Lote 2", "Laticínios/Matinal"),
    Produto("Quata", "13/07/2026", "Lote 3", "Laticínios/Matinal"),
    Produto("Cha Leao Guarana Garrafa", "29/04/2026", "Lote 1", "Matinal"),
    Produto("Kinder Joy", "31/05/2026", "Lote Único", "Chocolates"),
    Produto("Chocolate Arcor Brigadeiro", "21/05/2026", "Lote Único", "Chocolates"),
    Produto("70% Cacau Cafe Espresso", "26/05/2026", "Lote Único", "Chocolates"),
    Produto("70% Cacau Caramel Macchiato", "25/05/2026", "Lote Único", "Chocolates"),
    Produto("Chocolate Lacta 40% Cacau", "30/05/2026", "Lote Único", "Chocolates"),
    Produto("Piraque Chocowafer", "02/05/2026", "Lote Único", "Chocolates"),
    Produto("Porto Alegre Creme de Leite", "29/06/2026", "Lote 1", "Mercearia"),
    Produto("Porto Alegre Creme de Leite", "15/07/2026", "Lote 2", "Mercearia"),
    Produto("Leco Creme de Leite", "19/06/2026", "Lote Único", "Mercearia"),
    Produto("Camponesa Creme de Leite", "18/05/2026", "Lote 1", "Mercearia"),
    Produto("Camponesa Creme de Leite", "15/06/2026", "Lote 2", "Mercearia"),
    Produto("Nestle Snow 230g", "06/07/2026", "Lote Único", "Matinal"),
    Produto("Aveia em Flocos Yoki", "10/07/2026", "Lote Único", "Matinal"),
    Produto("Quaker Flocos Finos", "05/07/2026", "Lote Único", "Matinal"),
    Produto("Viver Bem Aveia Flocos Grossos 500g", "25/07/2026", "Lote Único", "Produtos Light"),
    Produto("Mucilon 600g Arroz e Aveia", "01/05/2026", "Lote 1", "Matinal"),
    Produto("Mucilon 600g Arroz e Aveia", "01/07/2026", "Lote 2", "Matinal"),
    Produto("Mucilon 600g Arroz e Aveia", "01/08/2026", "Lote 3", "Matinal"),
    Produto("Mucilon Multicereais 600g", "01/05/2026", "Lote 1", "Matinal"),
    Produto("Mucilon Multicereais 600g", "01/09/2026", "Lote 2", "Matinal"),
    Produto("Torrada Adria Light", "15/05/2026", "Lote Único", "Produtos Light"),
    Produto("Nutella 350g", "16/06/2026", "Lote 1", "Mercearia"),
    Produto("Nutella 350g", "18/11/2026", "Lote 2", "Mercearia"),
    Produto("Paçoquinha Mascavo 210g", "18/05/2026", "Lote Único", "Mercearia"),
    Produto("Mucilon arroz e aveia 180g", "01/05/2026", "Lote 1", "Matinal"),
    Produto("Mucilon arroz e aveia 180g", "01/08/2026", "Lote 2", "Matinal"),
    Produto("Mucilon arroz e aveia 180g", "01/10/2026", "Lote 3", "Matinal"),
    Produto("Mucilon arroz e aveia 180g", "01/11/2026", "Lote 4", "Matinal"),
    Produto("Mucilon multicerais 180g", "01/12/2026", "Lote Único", "Matinal"),
    Produto("Mucilon milho 180g", "01/06/2026", "Lote 1", "Matinal"),
    Produto("Mucilon milho 180g", "01/07/2026", "Lote 2", "Matinal"),
    Produto("Mucilon milho 180g", "01/08/2026", "Lote 3", "Matinal"),
    Produto("Mucilon milho 180g", "01/11/2026", "Lote 4", "Matinal"),
    Produto("Massa de bolo vilma abacaxi", "12/06/2026", "Lote Único", "Mercearia"),
    Produto("Massa de bolo vilma floresta negra", "19/05/2026", "Lote 1", "Mercearia"),
    Produto("Massa de bolo vilma floresta negra", "14/07/2026", "Lote 2", "Mercearia"),
    Produto("Massa de bolo vilma laranja", "10/06/2026", "Lote 1", "Mercearia"),
    Produto("Massa de bolo vilma laranja", "23/06/2026", "Lote 2", "Mercearia"),
    Produto("Massa de bolo vilma limao", "18/06/2026", "Lote Único", "Mercearia"),
    Produto("Massa de bolo vilma chocolate suave", "24/05/2026", "Lote 1", "Mercearia"),
    Produto("Massa de bolo vilma chocolate suave", "11/06/2026", "Lote 2", "Mercearia"),
    Produto("Massa de bolo vilma broa de fuba", "30/06/2026", "Lote Único", "Mercearia"),
    Produto("Massa de bolo vilma baunilha", "29/06/2026", "Lote Único", "Mercearia"),
    Produto("Massa de bolo vilma festa", "06/05/2026", "Lote 1", "Mercearia"),
    Produto("Massa de bolo vilma festa", "04/06/2026", "Lote 2", "Mercearia"),
    Produto("Massa de bolo vilma leite condesado", "20/06/2026", "Lote Único", "Mercearia"),
    Produto("Massa de bolo vilma cenoura", "22/06/2026", "Lote Único", "Mercearia"),
]

# Ordenando o estoque por data (Lógica PVPS)
estoque_ordenado = sorted(estoque_mercearia, key=lambda x: x.data_validade)

# --- FUNÇÃO DE ALERTA GERAL ---
def mostrar_vencimentos_criticos(lista_produtos):
    print("\n--- 🚨 ALERTA GERAL: VENCIMENTOS PRÓXIMOS (ATÉ 7 DIAS) ---")
    encontrou_critico = False
    
    for p in lista_produtos:
        prazo = p.dias_para_vencer()
        if prazo <= 7:
            status = "⚠️ CRÍTICO" if prazo <= 3 else "🟡 ATENÇÃO"
            print(f"{status} | {p.nome} | Lote: {p.lote} | Vence em {prazo} dias")
            encontrou_critico = True
            
    if not encontrou_critico:
        print("Tudo sob controle! Nenhum produto vencendo nos próximos 7 dias.")

# --- EXECUÇÃO ---

print("\n--- ROTEIRO COMPLETO DE REPOSIÇÃO (ORDEM DE VENCIMENTO) ---")
for p in estoque_ordenado:
    prazo = p.dias_para_vencer()
    # Mostra tudo, mas sinaliza o que está perto
    check = "🚩" if prazo <= 7 else "✅"
    print(f"{check} {p.nome} (Lote: {p.lote}) | Faltam {prazo} dias")

# Aciona o Alerta Geral
mostrar_vencimentos_criticos(estoque_ordenado)

@echo off
python "%userprofile%\OneDrive\Área de Trabalho\validade.py"
pause
