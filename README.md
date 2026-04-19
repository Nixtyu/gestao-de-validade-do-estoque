Um sistema que monitora produtos e gera alertas baseados em margens de segurança (ex: 7, 15 ou 30 dias antes do vencimento)
# Gestão de Validade de Estoque

## 📌 Sobre o Projeto
Este sistema foi idealizado para resolver o problema real de perdas de produtos por vencimento em supermercados e comércios de alimentos. O objetivo é monitorar as datas de validade e gerar alertas automáticos.

## 🚀 Funcionalidades Planejadas
- Cadastro de produtos com data de validade e lote.
- Sistema de alertas:
  - 🔴 **Crítico:** Vence em até 7 dias.
  - 🟡 **Atenção:** Vence em até 15 dias.
  - 🟢 **Seguro:** Vence em mais de 30 dias.
- Relatório de produtos próximos ao vencimento para ações de promoção.

## 🏗️ Engenharia de Software (Estudos)
Como estudante de Engenharia de Software, este projeto foca em:
- Levantamento de Requisitos (Funcionais e Não Funcionais).
- Modelagem UML (Diagramas de Caso de Uso e Classes).
- Boas práticas de versionamento com Git.

## 🛠️ Tecnologias
- Linguagem: [A definir, ex: Python ou Java]
- Documentação: Markdown e Ferramentas UML.

## 📋 Requisitos Funcionais
RF01: O sistema deve permitir o cadastro de produtos informando nome, lote e data de validade.

RF02: O sistema deve emitir um alerta visual para produtos com vencimento inferior a 7 dias.

## 📊 Regra de Negócio
Devido ao alto volume de itens, o sistema deve priorizar a exibição dos itens com data de validade mais próxima (Lógica PEPS/FIFO).
