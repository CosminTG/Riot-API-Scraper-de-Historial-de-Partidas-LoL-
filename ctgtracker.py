import requests
import pandas as pd
import json
from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.getenv("api_key")
def obtener_nombre_y_tag():
    """
    El usuario ingresa su Riot ID completo (Ej: NOMBRE#TAG).
    El código lo separa automáticamente en nombre y tag.
    """
    riot_id = input("Ingresa tu Riot ID (ejemplo: MidBeast#NA1): ")
    if "#" not in riot_id:
        print("❌ Formato incorrecto. Debe ser NOMBRE#TAG")
        return obtener_nombre_y_tag()
    nombre, tag = riot_id.split("#", 1)
    return nombre, tag

def buscar_puuid(nombre, tag):
    """
    Obtiene el PUUID del jugador usando Riot ID.
    Devuelve el PUUID si existe, o None si no se encontró.
    """
    api_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nombre}/{tag}?api_key={api_key}"
    respuesta = requests.get(api_url)
    if respuesta.status_code != 200:
        print("❌ Error al buscar el jugador. Revisa el nombre o el tag.")
        return None
    data = respuesta.json()
    return data["puuid"]

def obtener_historial(puuid, cantidad=20):
    """
    Devuelve una lista de IDs de partidas del jugador(por defecto el api te devuelve 20 partidas).
    """
    api_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&api_key={api_key}"
    respuesta = requests.get(api_url)
    if respuesta.status_code != 200:
        print("❌ Error al obtener el historial.")
        return []
    return respuesta.json()

def obtener_detalle_partida(match_id):
    """
    Obtiene la información completa de una partida específica.
    """
    api_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    respuesta = requests.get(api_url)
    if respuesta.status_code != 200:
        print(f"❌ No se pudo obtener la partida {match_id}")
        return None
    data = respuesta.json()
    # # 👉 Guardarlo como archivo .json
    # nombre_archivo = f"partida_{match_id}.json"
    # # Abrimos el archivo y guardamos el JSON bonito formateado
    # with open(nombre_archivo, "w", encoding="utf-8") as f:
    #     json.dump(
    #         data,           # ← AQUÍ va el JSON ya decodificado
    #         f,
    #         indent=4,       # Formato bonito
    #         ensure_ascii=False  # Permite caracteres latinos
    #     )
    # print(f"📁 JSON guardado: {nombre_archivo}")
    return data

def mostrar_resumen_bonito(partidas, puuid):
    """
    Genera un resumen bonito en consola con info de cada partida.
    """
    print("\n================ HISTORIAL DE PARTIDAS ================\n")
    for i, match in enumerate(partidas, 1):
        info = match["info"]
        # Buscar al jugador dentro de la partida
        jugador = next(p for p in info["participants"] if p["puuid"] == puuid)
        campeon = jugador["championName"]
        kills = jugador["kills"]
        deaths = jugador["deaths"]
        assists = jugador["assists"]
        win = "VICTORIA" if jugador["win"] else "DERROTA"
        print(f"Partida {i}: {match['metadata']['matchId']}")
        print(f"  Campeón: {campeon}")
        print(f"  K/D/A: {kills}/{deaths}/{assists}")
        print(f"  Resultado: {win}")
        print("-------------------------------------------------------")
        print("\n========================================================\n")
# -------------------------------
# EJECUCIÓN
# -------------------------------
nombre, tag = obtener_nombre_y_tag()
puuid = buscar_puuid(nombre, tag)
if puuid:
    match_ids = obtener_historial(puuid)
    partidas_detalle = []
    for match_id in match_ids:
        detalle = obtener_detalle_partida(match_id)
        if detalle:
            partidas_detalle.append(detalle)
    if partidas_detalle:
        mostrar_resumen_bonito(partidas_detalle, puuid)