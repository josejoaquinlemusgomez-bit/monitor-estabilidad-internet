import subprocess
import time
from datetime import datetime

# A quien queremos monitorear, igual que tu haces con los GPS
objetivo = "8.8.8.8"

print(f"Iniciando monitoreo hacia {objetivo}... Presiona CTRL+C para parar")

while True:
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Hace el ping (funciona en Windows)
    resultado = subprocess.run(["ping", "-n", "1", objetivo], capture_output=True, text=True)
    
    if "0% perdidos" in resultado.stdout or "recibidos = 1" in resultado.stdout:
        print(f"[{ahora}] OK - Internet estable - 0% perdida")
    else:
        print(f"[{ahora}] FALLA - Se cayo el internet!")
        # Aqui lo guardamos en un archivo tipo bitacora
        with open("bitacora_caidas.txt", "a") as f:
            f.write(f"[{ahora}] FALLA detectada hacia {objetivo}\n")

    time.sleep(5)
