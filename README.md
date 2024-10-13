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
- **GetDefaultPrinter:** Obtém a impressora por omissão do sistema.
- **ShellExecute com "print":** Executa o comando de impressão para o ficheiro especificado, enviando-o para a impressora por omissão ou outra especificada.

### Considerações:
- Para o **Wake-on-LAN**, é necessário que a BIOS e as definições de rede do computador remoto estejam configuradas para suportar WoL.
- Para a **impressão de rede**, certifique-se de que a impressora de rede está corretamente configurada e acessível.

Estes exemplos devem ajudá-lo a criar "pacotes mágicos" para ligar computadores e imprimir remotamente em Python no Windows 10.
