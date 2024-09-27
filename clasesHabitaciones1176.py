class Habitaciones1176:
    individual1176 = ""
    Suite1176 = ""
    Presidencial1176 = ""
    costo1176 = 0
    Dias_de_Hospedaje1176 = 0
    id = 0
    cantidad_de_Habitaciones1176 = 0
    def mostrar_datos1176(self):
        print(f"Individual: {self.individual1176}")
        print(f"Suite: {self.Suite1176}")
        print(f"Presidencial: {self.Presidencial1176}")
        print(f"Costo: {self.costo1176}")
        print(f"Días de Hospedaje: {self.Dias_de_Hospedaje1176}")
        print(f"ID: {self.id}")
        print(f"Cantidad de Habitaciones: {self.cantidad_de_Habitaciones1176}")
    def Lista_Habita1176(self):
        Habita1176 = ["Individual", "Suite", "Presidencial", "Regular", "Sencilla", "Normal", "Doble Cama"]
        print("Lista de Habitaciones:")
        for Cuartos in Habita1176:
            print(Cuartos)
    def Tupla_dias1176(self):
        diasdeHospedaje = ("24 días", "39 días", "50 días", "20 días", "35 días", "40 días", "55 días")
        print("Días de Hospedaje:")
        for dias in diasdeHospedaje:
            print(dias)
    def Dicc_Costo1176(self):
        Cost = {
            "Individual": 25000,
            "Suite": 55000,
            "Presidencial": 70000,
            "Normal": 10000,
            "Regular": 5000,
            "Sencilla": 2500,
            "Doble Cama": 7000
        }
        print("Costo de las habitaciones:")
        for habitacion, costo in Cost.items():
            print(f"{habitacion}: {costo}")
        print("La operación de alta se realizó correctamente.")
        print("La operación de baja se realizó correctamente.")
# Creación de objeto 
Habi = Habitaciones1176()
# Utilizando el objeto 
Habi.Dicc_Costo1176()
print()
Habi.Tupla_dias1176()
print()
Habi.Lista_Habita1176()