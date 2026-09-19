import requests

API_KEY = "f116b2d4-b7d8-4d31-ae93-755516e03c26"

while True:

    origen = input("\nCiudad de Origen (v para salir): ")

    if origen.lower() == "v":
        print("Programa finalizado")
        break

    destino = input("Ciudad de Destino: ")

    transporte = input(
        "Medio de transporte (car, bike, foot): "
    ).lower()

    # Geocoding origen
    url_origen = (
        f"https://graphhopper.com/api/1/geocode"
        f"?q={origen}&limit=1&key={API_KEY}"
    )

    datos_origen = requests.get(url_origen).json()

    # Geocoding destino
    url_destino = (
        f"https://graphhopper.com/api/1/geocode"
        f"?q={destino}&limit=1&key={API_KEY}"
    )

    datos_destino = requests.get(url_destino).json()

    try:
        lat1 = datos_origen["hits"][0]["point"]["lat"]
        lon1 = datos_origen["hits"][0]["point"]["lng"]

        lat2 = datos_destino["hits"][0]["point"]["lat"]
        lon2 = datos_destino["hits"][0]["point"]["lng"]

        ruta_url = (
            f"https://graphhopper.com/api/1/route?"
            f"point={lat1},{lon1}"
            f"&point={lat2},{lon2}"
            f"&profile={transporte}"
            f"&instructions=true"
            f"&locale=es"
            f"&key={API_KEY}"
        )

        ruta = requests.get(ruta_url).json()

        distancia_metros = ruta["paths"][0]["distance"]
        tiempo_ms = ruta["paths"][0]["time"]

        km = distancia_metros / 1000
        millas = km * 0.621371
        horas = tiempo_ms / 1000 / 60 / 60

        print("\n===== RESULTADOS =====")
        print(f"Origen: {origen}")
        print(f"Destino: {destino}")
        print(f"Transporte: {transporte}")
        print(f"Distancia: {km:.2f} km")
        print(f"Distancia: {millas:.2f} millas")
        print(f"Duración: {horas:.2f} horas")

        print("\n===== NARRATIVA =====")

        for paso in ruta["paths"][0]["instructions"]:
            print("-", paso["text"])

    except:
        print("Error al consultar la ruta.")