import requests
import time
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

# --- CONFIGURACIÓN ---
TOKEN_TELEGRAM = '8259241555:AAEEU9ryQ-KtZJuA37DJ5HpbrrzEeRvRAO'
ID_CHAT = '7681365291'
ACCESS_TOKEN_META = 'EAA8ea17ZB1V0BRcvOm9HPRkrhg8HV3rm9TVGvsLFOZCTWEuX1vZCE0fn82HQxPCw0ZByLAAalTjxtKrHK1oYiR2KDF9x2LPnz2an7wAStYRV3RCpyq6AdeaaDOZC7WxWnI49ZCcTF3PiKkYn34HMDHaUMzkbHwB9kPPHnoqymi0qhbdW6TJjunkprswqpIeXuflJwtLHETKFVwn2T2JIZAdZCu6VcZCs7rqWNz7h9'
ID_CUENTA_META = 'act_1657951032043050'

# Define tu límite diario aquí (ejemplo: 10 dólares o la moneda de tu cuenta)
LIMITE_GASTO = 10.0 

def enviar_alerta_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    payload = {'chat_id': ID_CHAT, 'text': mensaje, 'parse_mode': 'Markdown'}
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def monitorear():
    try:
        FacebookAdsApi.init(access_token=ACCESS_TOKEN_META)
        account = AdAccount(ID_CUENTA_META)
        
        # Consultamos el gasto de hoy
        insights = list(account.get_insights(fields=['spend'], params={'date_preset': 'today'}))
        gasto_hoy = float(insights[0]['spend']) if insights else 0.0
        
        # Lógica de Alerta
        if gasto_hoy > LIMITE_GASTO:
            mensaje = f"⚠️ *¡ALERTA DE GASTO EXCEDIDO!*\n\nEl gasto actual es de `${gasto_hoy}`, superando tu límite de `${LIMITE_GASTO}`. Revisa tu cuenta pronto."
        elif gasto_hoy > 0:
            mensaje = f"📊 *Reporte Actual:*\nHas gastado `${gasto_hoy}` el día de hoy."
        else:
            mensaje = "✅ Conexión establecida. El gasto de hoy sigue en $0."

        print(f"Enviando reporte: {mensaje}")
        enviar_alerta_telegram(mensaje)
        
    except Exception as e:
        error_msg = f"❌ Error en el monitoreo: {e}"
        print(error_msg)
        enviar_alerta_telegram(error_msg)

if __name__ == "__main__":
    while True:
        print("Ejecutando monitoreo...")
        monitorear()
        
        # Espera 12 horas para el siguiente reporte (43200 segundos)
        # Así te llega dos veces al día sin que tú hagas nada.
        print("Reporte enviado. Durmiendo por 12 horas...")
        time.sleep(43200)