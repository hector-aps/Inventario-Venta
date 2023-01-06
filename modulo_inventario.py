import csv
import os
import datetime


class Inventario:
    def __init__(self):
        try:
            self.inventario = []
            with open("Inventario.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                for producto in reader:
                    self.inventario.append(producto)
        except:
            self.inventario = []
        self.carrito = {}
    
    def agregar(self, producto, precio, cantidad):
        try:
            if producto != "" and float(precio) > 0 and int(cantidad) > 0:
                self.inventario.append([producto, float(precio), int(cantidad)])
                self.guardar()
                return True
        except:
            return False
    
    def guardar(self):
        with open("Inventario.csv", "w", newline = "") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(self.inventario)
    
    def eliminar(self, nombre):
        for producto in self.inventario:
            if producto[0] == nombre:
                self.inventario.pop(self.inventario.index(producto))
                break

    def modificar(self, nombre, amodificar, valor):
        try:
            for producto in self.inventario:
                if producto[0] == nombre:
                    match amodificar:
                        case 0:
                            if valor != "":
                                self.inventario[self.inventario.index(producto)][0] = valor
                        case 1:
                            if float(valor) > 0:
                                self.inventario[self.inventario.index(producto)][1] = float(valor)
                        case 2:
                            if int(valor) > 0:
                                self.inventario[self.inventario.index(producto)][2] = int(valor)
            self.guardar()
            return True
        except:
            return False
    
    def agregarAlCarrito(self, nombre, precio):
        if nombre in self.carrito.keys():
            self.carrito[nombre][0] += 1
            self.carrito[nombre][1] += float(precio)
        else:
            self.carrito[nombre] = [1, float(precio)]


    def finalizarCompra(self):
        for nombre, valores in self.carrito.items():
            for producto in self.inventario:
                if producto[0] == nombre:
                    index = self.inventario.index(producto)
                    self.inventario[index][2] = int(self.inventario[index][2]) - int(valores[0])
                    if self.inventario[index][2] < 1: self.inventario.pop(index)

        os.makedirs("./tickets", exist_ok=True)

        now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

        ticket = open("./tickets/{}.txt".format(now), "w")

        ticket.write("\nTicket de compra\n")
        ticket.write("\n")
        ticket.write("Fecha: {}\n".format(now))
        ticket.write("-"*30)
        ticket.write("\n")
        ticket.write("Cant. - Producto - Subtotal\n")
        
        for nombre, valores in self.carrito.items():
            ticket.write("{}x {} (${})\n".format(valores[0], nombre, round(valores[1], 2)))
        

        total = 0
        for pedido in self.carrito.values():
            total += float(pedido[1])

        ticket.write(f"\n")
        ticket.write("-"*30)
        ticket.write(f"\nSubotal:          ${round(total, 2)}")
        ticket.write(f"\nIVA (16%):        ${round(total*0.16, 2)}")
        ticket.write(f"\nTotal a pagar:    ${round(total*1.16, 2)}\n")
        ticket.write("-"*30)
        ticket.write(f"\n***GRACIAS POR SU PREFERENCIA***")
        ticket.close()
        self.guardar()

        self.carrito = {}