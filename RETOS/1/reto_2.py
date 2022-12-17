velocidad = int(input("Ingrese velocidad"))
presion_punta = velocidad * 2 + 4
temperatura_punta = (velocidad + presion_punta) / 5
if temperatura_punta <= 20:
    recubrimiento_carbon = "uno"
elif temperatura_punta > 20 and temperatura_punta <= 30:
    recubrimiento_carbon = "dos"
elif temperatura_punta > 30 and temperatura_punta <= 50:
    recubrimiento_carbon = "tres"
elif temperatura_punta > 50:
    recubrimiento_carbon = "cuatro"
print(str(int(velocidad)) + " " + str(int(presion_punta)) + " " + str(int(temperatura_punta)))
print(recubrimiento_carbon)
