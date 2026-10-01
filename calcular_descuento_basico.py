# Cabecera
# Autor: Nicolas Aaron
# Fecha: 30/09/2026

# Constantes
UMBRAL_ALTO = 300.0
UMBRAL_BAJO = 100.0
DESCUENTO_ALTO = 0.15
DESCUENTO_BAJO = 0.10
DESCUENTO_CERO = 0.00


# Función para calcular el descuento

def calcular_descuento(importe):
    """Devuelve el porcentaje, el descuento y el precio final."""
    if importe >= UMBRAL_ALTO:
        porcentaje = DESCUENTO_ALTO
    elif importe >= UMBRAL_BAJO:
        porcentaje = DESCUENTO_BAJO
    else:
        porcentaje = DESCUENTO_CERO

    descuento = importe * porcentaje
    total = importe - descuento
    return porcentaje, descuento, total


# Programa principal

print("=== CALCULADORA DE DESCUENTOS ===")

# Entrada del importe
importe = float(input("Introduce el importe de la compra (€): "))

# Validación
if importe < 0:
    print("Error: El importe no puede ser negativo.")
else:
    porcentaje, descuento, total = calcular_descuento(importe)

    print("\n--- RESUMEN DE LA COMPRA ---")
    print("Importe original:", format(importe, ".2f"), "€")
    print("Descuento aplicado:", int(porcentaje * 100), "%")
    print("Ahorro obtenido:", format(descuento, ".2f"), "€")
    print("Total a pagar:", format(total, ".2f"), "€")
