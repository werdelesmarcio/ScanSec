import socket
import sys

def scan_port(ip, port):
    """
    Função para verificar se uma porta está aberta em um endereço IP.

    Args:
        ip (str): Endereço IP a ser verificado.
        port (int): Porta a ser verificada.

    Returns:
        bool: True se a porta estiver aberta, False caso contrário.
    """
    try:
        # Cria um socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define o tempo limite de conexão
        sock.settimeout(0.5)
        # Conecta-se ao endereço IP e porta
        sock.connect((ip, port))
        sock.close()
        return True
    except socket.error:
        return False

def main():
    """
    Função principal que verifica as portas de um endereço IP e exibe os serviços em execução.
    """
    if len(sys.argv) != 2:
        print("Uso: python scanner_de_portas.py <endereço_ip>")
        sys.exit(1)

    ip = sys.argv[1]

    # Define as portas a serem verificadas
    portas = range(1, 65535)

    # Itera pelas portas
    for porta in portas:
        if scan_port(ip, porta):
            # Obtém o nome do serviço
            services = socket.getservbyport(porta, 'TCP')
            # servico = socket.getservbyport(porta, 'tcp')
            print(f"Porta {porta} aberta: {services}")

if __name__ == "__main__":
    main()