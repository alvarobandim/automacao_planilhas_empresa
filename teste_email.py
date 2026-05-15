import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication # <-- NOVA PEÇA DE ENGENHARIA

# --- CONFIGURAÇÕES DO ROBÔ ---
email_robo = "alvarogabandim@gmail.com"
senha_robo = "oqcuwfygoxondsfz" 
email_destino = "alvarogabandim@gmail.com" 

# --- PARTE 1: MONTANDO O ENVELOPE E A CARTA ---
print("Robô: Montando o envelope...")
envelope = MIMEMultipart()
envelope["From"] = email_robo
envelope["To"] = email_destino
envelope["Subject"] = "Relatório Consolidado Automatizado"

texto = "Prezados,\n\nSegue em anexo o relatório consolidado com a volumetria de chamados das filiais.\n\nAtenciosamente,\nRobô de Automação"
envelope.attach(MIMEText(texto, "plain"))

# --- PARTE 2: PEGANDO A PLANILHA E ANEXANDO ---
print("Robô: Pegando a planilha na bancada...")

# 1. Abrimos o arquivo em modo de Leitura Binária
with open("relatorio_consolidado.xlsx", "rb") as arquivo_fisico:
    
    # 2. Convertemos para o "Pen Drive digital" do e-mail
    anexo = MIMEApplication(arquivo_fisico.read(), Name="relatorio_consolidado.xlsx")

# 3. Colocamos a etiqueta oficial de anexo
anexo["Content-Disposition"] = 'attachment; filename="relatorio_consolidado.xlsx"'

# 4. Jogamos o anexo dentro do envelope principal
envelope.attach(anexo)


# --- PARTE 3: INDO ATÉ A AGÊNCIA DOS CORREIOS ---
print("Robô: Indo até a agência do Gmail...")
try:
    agencia = smtplib.SMTP("smtp.gmail.com", 587)
    agencia.starttls()
    agencia.login(email_robo, senha_robo)
    agencia.send_message(envelope)
    print("Sucesso: Relatório entregue com anexo!")
except Exception as erro:
    print("Falha na entrega. Erro:", erro)
finally:
    agencia.quit()