#Ashley Dayane Alfaro Aguilar
#Carne 202301982 ing en sistemas 100% virtual

"""
Programa principal para la práctica de Árbol de Decisión.
Combina la carga/generación de números y la clasificación con un umbral.
"""

import time
from src.data_loader import generar_archivo_si_no_existe, cargar_numeros
from src.decision_tree import clasificar_numero, UMBRAL


def main():
    """Ejecuta el flujo completo del programa."""
    inicio = time.time()

    # 1. Verifica / genera archivo
    archivo_generado, semilla = generar_archivo_si_no_existe()
    if archivo_generado:
        print(f"Archivo generado automáticamente con semilla: {semilla}")
    else:
        print("Archivo existente encontrado. No fue necesario generarlo.")

    # 2. Carga números
    numeros = cargar_numeros()

    # 3. Clasifica números
    clasificaciones = [clasificar_numero(n, UMBRAL) for n in numeros]

    # 4. Imprime primeras 10 clasificaciones
    print("\nEjemplos de clasificación:")
    for i in range(10):
        print(f"{numeros[i]} → {clasificaciones[i]}")

    # 5. Conteos
    total_alto = clasificaciones.count("Alto")
    total_bajo = clasificaciones.count("Bajo")

    print("\nConteos:")
    print(f"Alto: {total_alto}")
    print(f"Bajo: {total_bajo}")

    # 6. Tiempo total
    fin = time.time()
    tiempo_total = fin - inicio
    print(f"\nTiempo total de ejecución: {tiempo_total:.4f} segundos")


if __name__ == "__main__":
    main()

