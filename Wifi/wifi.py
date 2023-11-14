import time
import pywifi
import psutil


def desativar_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assume que há pelo menos uma interface Wi-Fi

    print("Desabilitando placa Wi-Fi...")

    # Desconectar da rede atual
    iface.disconnect()
    time.sleep(1)  # Aguarda 1 segundo

    # Desativando a placa Wifi fisicamente.
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        cmdline = proc.info.get('cmdline')
        if cmdline is not None and 'wlan' in cmdline:
            psutil.Process(proc.info['pid']).suspend()

    print("Placa Wi-Fi desabilitada com sucesso.")


def ativar_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assume que há pelo menos uma interface Wi-Fi

    print("Ativando placa Wi-Fi...")

    # Ativar fisicamente a placa Wifi
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        cmdline = proc.info.get('cmdline')
        if cmdline is not None and 'wlan' in cmdline:
            psutil.Process(proc.info['pid']).resume()

    # Verifica o status da interface
    iface.scan_results()

    print("Placa Wi-Fi ativada com sucesso.")


def conectar_wifi(nome_da_rede, senha):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assume que há pelo menos uma interface Wi-Fi

    print(f"Conectando à rede Wi-Fi '{nome_da_rede}'...")

    # Obtém o perfil da rede
    perfil = pywifi.Profile()
    perfil.ssid = nome_da_rede  # Nome da rede
    perfil.auth = pywifi.const.AUTH_ALG_OPEN  # Tipo de autenticação (aberta)
    perfil.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # Tipo de criptografia
    perfil.cipher = pywifi.const.CIPHER_TYPE_CCMP  # Tipo de cifra
    perfil.key = senha  # Senha da rede

    # Adiciona o perfil
    iface.remove_all_network_profiles()
    iface.add_network_profile(perfil)

    # Conecta à rede
    iface.connect(perfil)
    time.sleep(5)  # Aguarda alguns segundos para a conexão

    print("Conexão à rede Wi-Fi estabelecida com sucesso.")


# Informações da rede Wi-Fi
nome_da_rede = "Nome_da_Rede"
senha_da_rede = "Senha_da_Rede"

# Desativa o Wi-Fi
desativar_wifi()

# Aguarda 10 segundos
time.sleep(10)

# Ativa o Wi-Fi
ativar_wifi()

# Conecta à rede Wi-Fi
conectar_wifi(nome_da_rede, senha_da_rede)

# Mensagem final
resposta = input("Wifi conectou? (Sim/Não): ").lower()

# Verifica a resposta do usuário
while resposta != "sim":
    # Se a resposta for "Não", repete o processo
    desativar_wifi()
    time.sleep(10)
    ativar_wifi()
    conectar_wifi(nome_da_rede, senha_da_rede)
    resposta = input("Wifi conectou? (Sim/Não): ").lower()

print("Processo concluído.")
