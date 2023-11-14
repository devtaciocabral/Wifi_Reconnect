import time
import pygetwindow as gw
import pyautogui

def encontrar_janela_rede():
    janelas = gw.getWindowsWithTitle("")
    for janela in janelas:
        if "Rede" in janela.title:
            return janela
    return None

def desconectar_cabo():
    print("Desconectando cabo Ethernet...")

    # Encontrar a janela de configurações de rede
    janela_rede = encontrar_janela_rede()

    if janela_rede is not None:
        # Ativar a janela de configurações de rede
        janela_rede.activate()

        # Esperar um pouco para garantir que a janela está ativa
        time.sleep(2)

        # Localizar o botão "Desativar" e clicar
        pyautogui.click(pyautogui.locateCenterOnScreen(r'C:\Users\tacio.cabral\Documents\Wifi\images\desativar.png'))

        print("Cabo Ethernet desconectado com sucesso.")
    else:
        print("Janela de configurações de rede não encontrada.")

def reconectar_cabo():
    print("Reconectando cabo Ethernet...")

    # Encontrar a janela de configurações de rede
    janela_rede = encontrar_janela_rede()

    if janela_rede is not None:
        # Ativar a janela de configurações de rede
        janela_rede.activate()

        # Esperar um pouco para garantir que a janela está ativa
        time.sleep(2)

        # Localizar o botão "Ativar" e clicar
        pyautogui.click(pyautogui.locateCenterOnScreen(r'C:\Users\tacio.cabral\Documents\Wifi\images\ativar.png'))

        print("Cabo Ethernet reconectado com sucesso.")
    else:
        print("Janela de configurações de rede não encontrada.")

# Desconectar o cabo Ethernet
desconectar_cabo()

# Aguarda 10 segundos
time.sleep(10)

# Reconectar o cabo Ethernet
reconectar_cabo()

# Mensagem final
resposta = input("Cabo Ethernet conectado? (Sim/Não): ").lower()

# Verifica a resposta do usuário
while resposta != "sim":
    # Se a resposta for "Não", repete o processo
    desconectar_cabo()
    time.sleep(10)
    reconectar_cabo()
    resposta = input("Cabo Ethernet conectado? (Sim/Não): ").lower()

print("Processo concluído.")
