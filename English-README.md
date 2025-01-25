# Wake-on-LAN

Wake-on-LAN Commands

To perform tasks such as turning on a computer remotely (Wake-on-LAN) or sending documents to a network printer, specific network and operating system functionalities are required. These "magic packets" can be created in Python with the help of specialized libraries. Let’s see how to implement these two features in Python on Windows 10:

### 1. Turning on a Computer Remotely (Wake-on-LAN)

**Wake-on-LAN** (WoL) allows turning on a computer remotely over the network by sending a "magic packet" to the MAC address of the device you want to turn on.

#### Installing the required library:
First, you need to install the `wakeonlan` library, which enables sending the WoL packet.

```bash
pip install wakeonlan
```

#### Example of code to send the "magic packet":
```python
from wakeonlan import send_magic_packet

def turn_on_computer(mac_address):
    try:
        send_magic_packet(mac_address)
        print(f"Magic packet sent to {mac_address}.")
    except Exception as e:
        print(f"Error sending magic packet: {e}")

if __name__ == "__main__":
    # Replace with the MAC address of the computer you want to turn on
    mac_address = "00:11:22:33:44:55"
    turn_on_computer(mac_address)
```

### Explanation:
- **MAC Address:** The MAC address is the unique identifier of the network hardware. Replace the value `00:11:22:33:44:55` with the MAC address of the computer you want to turn on.
- **send_magic_packet:** This function sends the WoL packet to the computer, allowing it to turn on.

### 2. Printing to a Network Printer
[Printing with Wake-on-LAN](https://github.com/0joseDark/Wake-on-LAN/blob/main/English-impressoras.md)

To print documents to a network printer, you can use the `win32print` library, which is part of the `pywin32` package. This package allows controlling printers in Windows, including network printers.

#### Installing the required library:
First, you need to install the `pywin32` package:

```bash
pip install pywin32
```

#### Example code to print:
```python
import win32print
import win32api

def print_document(file_path):
    try:
        # Get the default printer
        printer = win32print.GetDefaultPrinter()
        print(f"Default printer: {printer}")

        # Send the document to the printer
        win32api.ShellExecute(0, "print", file_path, None, ".", 0)
        print(f"The file {file_path} was sent to the printer {printer}.")
    except Exception as e:
        print(f"Error sending the document to the printer: {e}")

if __name__ == "__main__":
    # Replace with the path to the file you want to print
    file_path = "C:\\path\\to\\document.pdf"
    print_document(file_path)
```

### Explanation:
- **GetDefaultPrinter:** Retrieves the system's default printer.
- **ShellExecute with "print":** Executes the print command for the specified file, sending it to the default or specified printer.

### Considerations:
- For **Wake-on-LAN**, the BIOS and network settings of the remote computer must be configured to support WoL.
- For **network printing**, ensure the network printer is properly configured and accessible.

These examples should help you create "magic packets" to turn on computers and print remotely in Python on Windows 10.

--- 
