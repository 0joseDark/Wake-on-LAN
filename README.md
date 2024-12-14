# Wake-on-LAN
 Wake-on-LAN comandos
 
 Para realizar tarefas como ligar um computador remotamente (Wake-on-LAN) ou enviar documentos para uma impressora de rede, 
 é necessário utilizar funcionalidades específicas de redes e sistemas operativos. 
 Esses "pacotes mágicos" podem ser feitos em Python com a ajuda de bibliotecas especializadas. 
 Vamos ver como implementar as duas funcionalidades em Python no Windows 10:

### 1. Ligar um Computador Remotamente (Wake-on-LAN)

O **Wake-on-LAN** (WoL) permite ligar um computador remotamente através da rede, enviando um "pacote mágico" para o endereço MAC do dispositivo que se deseja ligar.

#### Instalação da biblioteca necessária:
Primeiro, precisamos instalar a biblioteca `wakeonlan` que permite enviar o pacote WoL.

```bash
pip install wakeonlan
```

#### Exemplo de código para enviar o "pacote mágico":
```python
from wakeonlan import send_magic_packet

def ligar_computador(mac_address):
    try:
        send_magic_packet(mac_address)
        print(f"Pacote mágico enviado para {mac_address}.")
    except Exception as e:
        print(f"Erro ao enviar o pacote mágico: {e}")

if __name__ == "__main__":
    # Substitua pelo endereço MAC do computador que deseja ligar
    mac_address = "00:11:22:33:44:55"
    ligar_computador(mac_address)
```

### Explicação:
- **MAC Address:** O endereço MAC é o identificador único do hardware de rede. Substitua o valor `00:11:22:33:44:55` pelo endereço MAC do computador que deseja ligar.
- **send_magic_packet:** Esta função envia o pacote WoL para o computador, permitindo que ele se ligue.

### 2. Imprimir numa Impressora de Rede
[imprimir-Wake-on-LAN](https://github.com/0joseDark/Wake-on-LAN/blob/main/impressora.md)

Para imprimir documentos numa impressora de rede, podemos usar a biblioteca `win32print`, que faz parte do pacote `pywin32`. Este pacote permite controlar impressoras no Windows, inclusive impressoras de rede.

#### Instalação da biblioteca necessária:
Primeiro, precisamos instalar o pacote `pywin32`:

```bash
pip install pywin32
```

#### Exemplo de código para imprimir:
```python
import win32print
import win32api

def imprimir_documento(caminho_ficheiro):
    try:
        # Obter a impressora por omissão
        impressora = win32print.GetDefaultPrinter()
        print(f"Impressora por omissão: {impressora}")

        # Enviar o documento para a impressora
        win32api.ShellExecute(0, "print", caminho_ficheiro, None, ".", 0)
        print(f"O ficheiro {caminho_ficheiro} foi enviado para a impressora {impressora}.")
    except Exception as e:
        print(f"Erro ao enviar o documento para a impressora: {e}")

if __name__ == "__main__":
    # Substitua pelo caminho do ficheiro que deseja imprimir
    caminho_ficheiro = "C:\\caminho\\para\\o\\documento.pdf"
    imprimir_documento(caminho_ficheiro)
```

### Explicação:
- **GetDefaulAqui estão alguns módulos Python que permitem o uso do **Wake-on-LAN (WOL)**, com explicações sobre como funcionam:

### 1. **wakeonlan**
   - **Descrição**: Este é um dos módulos mais simples e populares para enviar pacotes mágicos para dispositivos na rede local. Ele usa apenas o endereço MAC do dispositivo para enviá-lo.
   - **Instalação**:
     ```bash
     pip install wakeonlan
     ```
   - **Como funciona**: O módulo constrói o pacote mágico e o transmite pela rede. O pacote mágico contém 6 bytes de `0xFF` seguidos pelo endereço MAC repetido 16 vezes. Quando uma placa de rede que suporta WOL recebe esse pacote, ela acorda o sistema.
   - **Exemplo**:
     ```python
     from wakeonlan import send_magic_packet

     send_magic_packet('AA:BB:CC:DD:EE:FF')  # Substitua pelo endereço MAC real
     ```

### 2. **wol**
   - **Descrição**: Este módulo também permite o envio de pacotes WOL e oferece funcionalidades para definir o endereço de IP de broadcast (ou multicast), que pode ser útil se precisar de enviar o pacote para redes específicas.
   - **Instalação**:
     ```bash
     pip install wol
     ```
   - **Como funciona**: Ele oferece mais controle sobre o envio do pacote WOL, permitindo o uso de diferentes métodos de broadcast.
   - **Exemplo**:
     ```python
     import wol

     wol.send_wol('AA:BB:CC:DD:EE:FF', ip_address='192.168.1.255')  # Broadcast IP
     ```

### 3. **etherwake** (usando via subprocess)
   - **Descrição**: Não é exatamente um módulo Python, mas você pode chamar o **`etherwake`** (uma ferramenta CLI) via Python para enviar pacotes WOL. Este utilitário é comumente usado em distribuições Linux.
   - **Instalação no Linux**:
     ```bash
     sudo apt install etherwake
     ```
   - **Como funciona**: Ele é chamado via terminal para enviar pacotes WOL. Em Python, você pode usar `subprocess` para chamar este comando.
   - **Exemplo**:
     ```python
     import subprocess

     subprocess.run(['sudo', 'etherwake', 'AA:BB:CC:DD:EE:FF'])
     ```

### 4. **socket** (módulo embutido no Python)
   - **Descrição**: Não é um módulo específico para WOL, mas o **`socket`** é um módulo embutido no Python que permite a construção e envio de pacotes de rede manualmente, incluindo o pacote mágico usado no WOL. Você pode criar o pacote mágico no formato correto e enviá-lo diretamente pela rede.
   - **Como funciona**: O `socket` pode ser usado para enviar o pacote para a rede através de UDP broadcast.
   - **Exemplo**:
     ```python
     import socket

     def wake_on_lan(mac_address):
         # Remove caracteres não hexadecimais do endereço MAC
         mac_address = mac_address.replace(':', '').replace('-', '')
         # Cria o pacote mágico
         magic_packet = bytes.fromhex('FF' * 6 + mac_address * 16)
         # Envia o pacote via socket UDP broadcast
         with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
             sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
             sock.sendto(magic_packet, ('<broadcast>', 9))  # Porta 9 padrão para WOL

     wake_on_lan('AA:BB:CC:DD:EE:FF')
     ```

### 5. **pywakeonlan**
   - **Descrição**: Um módulo alternativo para enviar pacotes WOL. Ele é bastante semelhante ao `wakeonlan` com funcionalidades muito básicas para enviar pacotes mágicos.
   - **Instalação**:
     ```bash
     pip install pywakeonlan
     ```
   - **Como funciona**: Simplesmente envia o pacote WOL com o endereço MAC especificado.
   - **Exemplo**:
     ```python
     from pywakeonlan import send_magic_packet

     send_magic_packet('AA:BB:CC:DD:EE:FF')
     ```

### 6. **netwake**
   - **Descrição**: Uma biblioteca menos conhecida que também implementa Wake-on-LAN. Ele é projetado para ser muito leve, focando exclusivamente no envio de pacotes mágicos.
   - **Instalação**:
     ```bash
     pip install netwake
     ```
   - **Como funciona**: Oferece uma API simples para enviar pacotes WOL, sem muitas funcionalidades adicionais.
   - **Exemplo**:
     ```python
     import netwake

     netwake.wake('AA:BB:CC:DD:EE:FF')
     ```

### 7. **net-tools (ferramenta externa para Linux)**
   - **Descrição**: Ferramentas externas como **net-tools** também podem ser usadas em sistemas baseados em Linux para enviar pacotes WOL via linha de comando e chamadas de subprocesso em Python, assim como o `etherwake`.

---

### Resumo

- **Módulos Simples (WOL direto)**:  
  - `wakeonlan`, `pywakeonlan`, `wol`, `netwake`.
  
- **Ferramentas de Linha de Comando**:  
  - `etherwake`, `net-tools` (usado via `subprocess`).

- **Solução Customizada**:  
  - Usar o módulo embutido **`socket`** do Python para criar manualmente pacotes mágicos e transmiti-los pela rede.

Esses módulos cobrem uma ampla gama de necessidades, desde o simples envio de pacotes WOL até soluções mais configuráveis para redes complexas.tPrinter:** Obtém a impressora por omissão do sistema.
- **ShellExecute com "print":** Executa o comando de impressão para o ficheiro especificado, enviando-o para a impressora por omissão ou outra especificada.

### Considerações:
- Para o **Wake-on-LAN**, é necessário que a BIOS e as definições de rede do computador remoto estejam configuradas para suportar WoL.
- Para a **impressão de rede**, certifique-se de que a impressora de rede está corretamente configurada e acessível.

Estes exemplos devem ajudá-lo a criar "pacotes mágicos" para ligar computadores e imprimir remotamente em Python no Windows 10.
- Explicação passo a passo:
1. O script utiliza o módulo tkinter para criar a interface gráfica.
2. A função `wake_on_lan` cria um pacote mágico a partir do endereço MAC fornecido e envia-o via UDP para o endereço de broadcast na porta 9.
3. A função `ligar_pc_remoto` verifica se o campo MAC está preenchido e chama a função `wake_on_lan`.
4. A janela contém dois campos de entrada para o IP (opcional) e MAC, um botão para enviar o pacote e outro para sair.
5. O menu "Ficheiro" inclui a opção "Sair" para fechar a aplicação.
6. O script exibe mensagens de sucesso ou erro usando caixas de diálogo tkinter.
   ![Wake-on-LAN](https://github.com/0joseDark/Wake-on-LAN/blob/main/image/Wake-On-Lan.jpg)



