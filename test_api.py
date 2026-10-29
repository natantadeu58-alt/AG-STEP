import requests 
url = "http://127.0.0.1:8000/analisar"
normal_traffic = {
    "packet_rate": 45.0,
    "failed_auths": 0 
}
attack_traffic = {
    "packet_rate": 950.0,
    "failed_auths": 14
}
print("=== A TESTAR O SISTEMA DE IA AG-STEP ===")
print("\n[+] Enviando tráfego normal...")
response_normal = requests.post(url, json=normal_traffic)
print("Resposta do Servidor", response_normal.json())
print("\n[+] Enviando tráfego anómalo(Simulação de ameaça)...")
response_attack = requests.post(url, json=attack_traffic)
print("Resposta do Servidor", response_attack.json())