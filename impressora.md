Ligar uma impressora de rede envolve configurar o seu PC para comunicar com a impressora através de um endereço IP na mesma rede. Vou explicar como fazer isso em diferentes situações:

---

### **Configurar uma Impressora de Rede no Windows 10**
1. **Obtenha o endereço IP da impressora**:
   - Verifique na interface da impressora ou no manual para saber o endereço IP.
   - Caso não saiba, pode usar o comando `arp -a` no Prompt de Comando para listar dispositivos conectados à rede.

2. **Adicione a impressora no Windows**:
   - Vá a **Configurações > Dispositivos > Impressoras e Scanners**.
   - Clique em **Adicionar uma impressora ou scanner**.
   - Se a impressora não for detectada automaticamente, escolha **A impressora que desejo não está listada**.
   - Selecione **Adicionar uma impressora usando um endereço TCP/IP ou nome de host**.
   - Insira o endereço IP da impressora e configure o modelo de driver, caso necessário.

---

### **Exemplo de Script Python para Testar a Conexão com uma Impressora de Rede**
O script abaixo verifica se o endereço IP da impressora está acessível na rede:

```python
import socket

def testar_conexao(ip, porta=9100):
    try:
        # Tentativa de conexão com a porta padrão (9100)
        with socket.create_connection((ip, porta), timeout=5):
            print(f"Conexão com a impressora em {ip}:{porta} foi bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar à impressora: {e}")

# Substitua pelo endereço IP da sua impressora
ip_impressora = "192.168.1.100"
testar_conexao(ip_impressora)
```

---

### **Enviar Dados Simples para Impressora de Rede**
Caso a impressora suporte comandos diretos, pode enviar texto ou comandos RAW:

```python
def enviar_dados_para_impressora(ip, dados, porta=9100):
    try:
        with socket.create_connection((ip, porta), timeout=5) as sock:
            sock.sendall(dados.encode('utf-8'))
            print("Dados enviados com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar dados: {e}")

# Exemplo de uso
ip_impressora = "192.168.1.100"
dados = "Teste de impressão via Python\n"
enviar_dados_para_impressora(ip_impressora, dados)
```

---

### **Explicação das Portas**
- Impressoras de rede geralmente usam a porta **9100** para recepção de dados via protocolo RAW.
- Outros protocolos, como LPR, podem usar portas diferentes (ex.: **515**).

---
