import tkinter as tk
from tkinter import messagebox, Menu
import socket
import struct

# Função para enviar o pacote Wake-on-LAN
def wake_on_lan(mac_address):
    try:
        # Criar o pacote mágico
        mac_bytes = bytes.fromhex(mac_address.replace(':', '').replace('-', ''))
        magic_packet = b'\xff' * 6 + mac_bytes * 16

        # Enviar o pacote via broadcast
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(magic_packet, ('<broadcast>', 9))

        messagebox.showinfo("Sucesso", "Pacote Wake-on-LAN enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar o pacote: {e}")

# Função para ligar o PC remoto
def ligar_pc_remoto():
    ip = entry_ip.get()
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
gjanela.mainloop()
