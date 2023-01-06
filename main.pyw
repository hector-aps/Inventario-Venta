from tkinter import *
from tkinter import ttk
from modulo_inventario import *
from tkinter import messagebox

root = Tk()
root.iconbitmap("./resourses/logo.ico")
root.title("Sistema de inventario y venta")
root.geometry("1100x720")
winv = Frame()
fondo = "#283747"
root.resizable(0,0)

root.config(bg = fondo)
winv.config(bg = fondo)

inv = Inventario()

#----------Tabla de productos-----------------------------------

viewInv = ttk.Treeview(winv, columns = ("#1", "#2"), height = 33)

viewInv.column("#0", width=200)
viewInv.column("#1", width=200, anchor = CENTER)
viewInv.column("#2", width=200, anchor = CENTER)

viewInv.heading("#0", text = "Producto", anchor = CENTER)
viewInv.heading("#1", text = "Precio ($)", anchor = CENTER)
viewInv.heading("#2", text = "Cantidad", anchor = CENTER)

viewInv.grid(row=0, column=0, padx= 60, pady=15)

viewInv.insert("", END, text = "Coca Cola", values = (37, 100))
viewInv.insert("", END, text = "Coca Cola", values = (37, 100))
viewInv.insert("", END, text = "Coca Cola", values = (37, 100))


def actualizarTabla():
    x = viewInv.get_children()
    for i in x:
        viewInv.delete(i)
    
    for producto, precio, cantidad in inv.inventario:
        viewInv.insert("", END, text = producto, values = (precio, cantidad))


def eliminar():
    x = viewInv.selection()

    res = messagebox.askquestion("Confirmar", "Esta seguro que desea eliminar: {}".format(viewInv.item(x)["text"]))
    if res=="yes":
        inv.eliminar(viewInv.item(x)["text"])
        actualizarTabla()
        inv.guardar()



#----------Panel de control------------------

control = Frame(root)

Label(control, text = "Panel de control", font = ("Arial", 12, "bold"), width = 30).grid(row=0, column=0, columnspan=2, padx=20, pady=20)

Label(control, text = "Agregar producto:", bg = "#283747", fg = "white", width = 30, font = ("Arial", 11, "bold")).grid(row=1, column=0, columnspan=2, padx=20, pady=5)

Label(control, text = "Nombre:", font = ("Arial", 10)).grid(row=2, column=0, padx=20, sticky="w", pady=10)
Label(control, text = "Precio:", font = ("Arial", 10)).grid(row=3, column=0, padx=20, sticky="w", pady=10)
Label(control, text = "Cantidad:", font = ("Arial", 10)).grid(row=4, column=0, padx=20, sticky="w", pady=10)

Prod = StringVar()
Precio = StringVar()
Cantidad = StringVar()

def agregar():
    if inv.agregar(Prod.get(), Precio.get(), Cantidad.get()):
        actualizarTabla()
        Prod.set("")
        Precio.set("")
        Cantidad.set("")
    else:
        messagebox.showinfo("Error", "Error, los datos no son aceptables")

Entry(control, textvariable=Prod, width=30).grid(row=2, column=1, padx=20, sticky="w", pady=10)
Entry(control, textvariable=Precio, width=30).grid(row=3, column=1, padx=20, sticky="w", pady=10)
Entry(control, textvariable=Cantidad, width=30).grid(row=4, column=1, padx=20, sticky="w", pady=10)

Button(control, text = "Agregar producto", width=20, command = agregar).grid(row=5, column=0, columnspa=2, padx=10, pady=10)

Button(control, text = "Eliminar seleccionado", width=20, font = ("", 10, "bold"), command = eliminar, bg = "#CB4335", fg = "white").grid(row=6, column=0, columnspa=2, padx=10, pady=30)

Label(control, text = "Modificar producto seleccionado:", bg = "#283747", fg = "white", width = 30, font = ("Arial", 11, "bold")).grid(row=7, column=0, columnspan=2, padx=20, pady=20)

modselection = IntVar()
modval = StringVar()

Radiobutton(control, text="Nombre  ", variable=modselection, value = 0, justify="left").grid(row=8,column=0, columnspan=2)
Radiobutton(control, text="Precio  ", variable=modselection, value = 1).grid(row=9,column=0, columnspan=2)
Radiobutton(control, text="Cantidad", variable=modselection, value = 2).grid(row=10,column=0, columnspan=2)


def modificar():
    if modval.get() != "" and viewInv.selection() != ():

        if inv.modificar(viewInv.item(viewInv.selection())["text"], modselection.get(), modval.get()):
            modval.set("")
        else:
            messagebox.showerror("Error", "Peticion no valida")
        actualizarTabla()
    else:
        messagebox.showerror("Error", "Peticion no valida")

def botones(boton):
    if boton == "mostrarVentas":
        control.pack_forget()
        venta.pack(side="right", fill = "both", expand = "True")
        actualizarCarrito()
    
    if boton == "carrito" and viewInv.selection() != ():
        nombre = viewInv.item(viewInv.selection())["text"]
        precio = viewInv.item(viewInv.selection())["values"][0]
        existencias = viewInv.item(viewInv.selection())["values"][1]

        if nombre in inv.carrito.keys():
            if inv.carrito[nombre][0] < existencias:
                inv.agregarAlCarrito(nombre, precio)
            else:
                messagebox.showerror("Error", "No hay suficientes existencias")
        else:
            inv.agregarAlCarrito(nombre, precio)
        actualizarCarrito()
    
    if boton == "finalizarCompra":
        if inv.carrito != {}:
            inv.finalizarCompra()
            messagebox.showinfo("Listo!", "Venta realizada, se ha generado el ticket de compra")
            venta.pack_forget()
            control.pack(side="right", fill = "both", expand = "True")
            actualizarTabla()
        else:
            messagebox.showinfo("Error", "Agrega productos para realizar una compra")
        
    if boton == "cancelar":
        respuesta = messagebox.askquestion("Cancelar venta", "Deseas cancelar la venta actual")
        if respuesta == "yes":
            venta.pack_forget()
            control.pack(side="right", fill = "both", expand = "True")
            inv.carrito = {}




Label(control, text = "Nuevo valor:", font = ("Arial", 10)).grid(row=11, column=0, padx=20, sticky="w", pady=10)
Entry(control, textvariable=modval, width=30).grid(row=11, column=1, padx=20, sticky="w", pady=10)
Button(control, text = "Modificar", width=20, command = modificar).grid(row=12, column=0, columnspa=2, padx=10, pady=10)

Button(control, text = "Realizar venta", bg="#283747", fg="white", width=25, command = lambda:botones("mostrarVentas"), font = ("", 12, "bold")).grid(row=13, column=0, columnspa=2, padx=10, pady=60)



#------------Ventana Venta------

venta = Frame(root)

Label(venta, text = "\nRealizar Venta", font = ("Arial", 12, "bold"), width = 30).grid(row=0, column=0, padx=20, pady=20)

Button(venta, text = "Agregar al carrito", bg="#283747", fg="white", width=25, font = ("", 12, "bold"), command = lambda:botones("carrito")).grid(row=1, padx=10, pady=20)

Button(venta, text = "Finalizar venta", bg="#283747", fg="white", width=25, font = ("", 12, "bold"), command = lambda:botones("finalizarCompra")).grid(row=3, padx=10, pady=20)

Button(venta, text = "Cancelar venta", bg="#CB4335", fg="white", width=25, font = ("", 12, "bold"), command = lambda:botones("cancelar")).grid(row=4, padx=10, pady=20)

carrito = Listbox(venta, width = 50, height = 20)
carrito.grid(row=2, padx=10, pady=20)

def actualizarCarrito():
    carrito.delete(0,END)
    carrito.insert(END, "Carrito:")
    for nombre, valores in inv.carrito.items():
        carrito.insert(END, "{}x {} (${})".format(valores[0], nombre, valores[1]))

actualizarCarrito()
actualizarTabla()
control.pack(side="right", fill = "both", expand = "True")
winv.pack(side = "left")
root.mainloop()