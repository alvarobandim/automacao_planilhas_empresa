"""
Script de automação: Consolidação de Relatórios de Filiais.
Objetivo: Ler arquivos Excel de um diretório específico, extrair a métrica de 
chamados resolvidos e gerar um relatório final consolidado para a diretoria.
"""

import os
import pandas as pd

diretorio_origem = "relatorios_filiais"
total_chamados_empresa = 0

arquivos_filiais = os.listdir(diretorio_origem)

# Processa cada relatório individualmente para acumular os resultados
for arquivo in arquivos_filiais:
    print(f"Lendo dados da filial: {arquivo}")
    
    caminho_arquivo = f"{diretorio_origem}/{arquivo}"
    df_filial = pd.read_excel(caminho_arquivo)
    
    # Extrai e soma a volumetria de chamados do arquivo corrente
    total_chamados_empresa += df_filial["Chamados_Resolvidos"].sum()

print("--- Processamento dos relatórios concluído ---")

# Gera o DataFrame consolidado e exporta o arquivo final
df_consolidado = pd.DataFrame({"Total_Geral_Empresa": [total_chamados_empresa]})
df_consolidado.to_excel("relatorio_consolidado.xlsx", index=False)

print("Relatório executivo 'relatorio_consolidado.xlsx' gerado com sucesso.")