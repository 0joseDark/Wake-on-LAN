# pip install wakeonlan
import tkinter as tk
from tkinter import messagebox, Menu
from wakeonlan import send_magic_packet

# Função para enviar o pacote Wake-on-LAN
def wake_on_lan(mac_address):
    try:
        # Enviar o pacote mágico usando o módulo wakeonlan
        send_magic_packet(mac_address)
        messagebox.showinfo("Sucesso", "Pacote Wake-on-LAN enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar o pacote: {e}")

# Função para ligar o PC remoto
def ligar_pc_remoto():
    ip = entry_ip.get()  # IP não é usado diretamente, mas pode ser útil para o contexto
    mac = entry_mac.get()

    if not mac:
        messagebox.showwarning("Atenção", "Por favor, insira um endereço MAC.")
        return

    wake_on_lan(mac)

# Função para sair da aplicação
def sair():
    janela.destroy()

# Criar a janela principal
janela = tk.Tk()
janela.title("Wake-on-LAN")
janela.geometry("400x200")

# Criar o menu
menu_bar = Menu(janela)
menu_arquivo = Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Sair", command=sair)
menu_bar.add_cascade(label="Ficheiro", menu=menu_arquivo)
janela.config(menu=menu_bar)

# Rótulos e campos de entrada
label_ip = tk.Label(janela, text="Endereço IP (opcional):")
label_ip.pack(pady=5)
entry_ip = tk.Entry(janela, width=30)
entry_ip.pack(pady=5)

label_mac = tk.Label(janela, text="Endereço MAC:")
label_mac.pack(pady=5)
entry_mac = tk.Entry(janela, width=30)
entry_mac.pack(pady=5)

# Botões
botao_ligar = tk.Button(janela, text="Ligar PC Remoto", command=ligar_pc_remoto)
botao_ligar.pack(pady=10)

botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.pack(pady=10)

# Iniciar o loop principal da interface
janela.mainloop()

# Explicação passo a passo:
# 1. O módulo wakeonlan é usado para simplificar o envio do pacote mágico.
# 2. A função `wake_on_lan` utiliza `send_magic_packet` para enviar o pacote baseado no MAC fornecido.
# 3. O usuário insere o endereço MAC e clica no botão para enviar o pacote.
# 4. A interface gráfica é criada com tkinter, contendo campos de entrada e botões para interatividade.
# 5. O menu "Ficheiro" inclui uma opção para sair da aplicação.
