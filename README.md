
# Riot API – Scraper de Historial de Partidas (LoL)
Script en Python para obtener información de cuentas y partidas de League of Legends usando la **Riot Games API**.  

Incluye búsqueda por Riot ID, obtención de PUUID, historial de partidas, detalles completos y guardado en disco.

## Características
- Buscar usuario usando RiotID#TAG ✔
- Obtener historial de partidas (match IDs) ✔
- Obtener detalle completo de cada partida ✔
- Guardar JSONs automáticamente ✔
- Uso de variables de entorno con .env ✔

## Requisitos Previos
Antes de ejecutar este proyecto, el usuario debe tener instalado:
- Python 3.8 o superior  ✔
Necesario para ejecutar el script y usar librerías como requests y python-dotenv.  

Para verificar si tienes Python instalado: 
```bash
    python --version
```
- pip (el gestor de paquetes de Python) ✔  
Viene instalado automáticamente con Python, pero puedes verificarlo:
```bash
    pip --version
```
## Instalación
Antes de ejecutar el script, instala los módulos necesarios:
```bash
    pip install requests
```
```bash
    pip install pandas
```
**Nota:**  
- El módulo json ya viene incluido con Python, no requiere instalación.
- Si estás usando un archivo .env, python-dotenv es obligatorio.
⚠En caso decidas usar el .env, crear el archivo y dentro va la clave del api_key (sin espacio, todo junto como se muestra abajo), proporcionado por riot la cual se encuentra en https://developer.riotgames.com/

```ini
 API_KEY=TU_API_KEY_AQUI
```
⚠ Nunca compartas tus Claves de API  

Para poder usar lo que tienes en el archivo .env, debes instalar python-dotenv
```bash
    pip install python-dotenv
```

## Estructura del Proyecto

📁 scraper_api_lol/  
 ├── ctgtracker.py  
 ├── .env  
 ├── .gitignore  
 ├── README.md  
 ├── LA1_123456789.json  
 └── LA1_987654321.json
## Ejemplo de salida en consola
```yaml
================ HISTORIAL DE PARTIDAS ================

Partida 1: LA1_453829493
  Campeón: Gwen
  K/D/A: 8/3/5
  Resultado: VICTORIA
-------------------------------------------------------
Partida 2: LA1_453829320
  Campeón: Ahri
  K/D/A: 3/7/2
  Resultado: DERROTA
-------------------------------------------------------

========================================================
```
## EndPoints usados
- Cuenta -> /riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}
- Historial -> /lol/match/v5/matches/by-puuid/{puuid}/ids
- Detalle de partida -> /lol/match/v5/matches/{matchId}
## 🛡 Licencia
Este proyecto es solo para fines educativos.  
Respeta siempre las reglas de Riot Developer Portal.
## 👨‍💻Autor
Proyecto creado por **CosminTG**  
Si te gusta, ¡dale una estrella ⭐ en GitHub! 👍