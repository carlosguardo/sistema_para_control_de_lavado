import tkinter as tk
from tkinter import ttk, messagebox
#-----------------------------#
#--|estructura_del_programa|--#
#-----------------------------#
class CarWashSystem:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Car Wash Control System")
        self.ventana.geometry("850x550")
        self.ventana.resizable(False, False)
        self.usuario = Usuario()
        self.lista_autos = []
        self.configurar_estilo()
        self.mostrar_login()
    #-------------------------#
    #--|estilo_del_programa|--#
    #-------------------------#
    def configurar_estilo(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Titulo.TLabel", font=("Arial", 18, "bold"))
        estilo.configure("TButton", font=("Arial", 10), padding=6)
        estilo.configure("Treeview", rowheight=28, font=("Arial", 10))
        estilo.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    #-------------#
    #--|ventana|--#
    #-------------#
    def limpiar_ventana(self):
        for elemento in self.ventana.winfo_children():
            elemento.destroy()
    #-------------------------------------#
    #--|estructura_del_inicio_de_sesion|--#
    #-------------------------------------#
    def mostrar_login(self):
        self.limpiar_ventana()
        frame_login = ttk.Frame(self.ventana, padding=40)
        frame_login.pack(expand=True)
        ttk.Label(frame_login, text="Car Wash System Login", style="Titulo.TLabel").grid(row=0, column=0, columnspan=2, pady=(0, 30))
        ttk.Label(frame_login, text="Username:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entrada_usuario = ttk.Entry(frame_login, width=30)
        self.entrada_usuario.grid(row=1, column=1, pady=10)
        ttk.Label(frame_login, text="Password:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entrada_password = ttk.Entry(frame_login, width=30, show="*")
        self.entrada_password.grid(row=2, column=1, pady=10)
        ttk.Button(frame_login, text="Login", command=self.validar_login).grid(row=3, column=0, columnspan=2, pady=20)
        self.entrada_usuario.focus()
    #--------------------------------------#
    #--|estructura_del_sistema_principal|--#
    #--------------------------------------#
    def mostrar_sistema(self):
        self.limpiar_ventana()
        frame = ttk.Frame(self.ventana, padding=20)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="Car Wash Control System", style="Titulo.TLabel").grid(row=0, column=0, columnspan=5, pady=(0, 20))
        #-------------------------#
        #--|datos_del_automovil|--#
        #-------------------------#
        ttk.Label(frame, text="License Plate:").grid(row=1, column=0, sticky="e", padx=5, pady=7)
        self.entrada_placa = ttk.Entry(frame, width=22)
        self.entrada_placa.grid(row=1, column=1, sticky="w")
        ttk.Label(frame, text="Entry Time (0-24):").grid(row=2, column=0, sticky="e", padx=5, pady=7)
        self.entrada_hora = ttk.Entry(frame, width=22)
        self.entrada_hora.grid(row=2, column=1, sticky="w")
        ttk.Label(frame, text="Hourly Rate:").grid(row=3, column=0, sticky="e", padx=5, pady=7)
        self.entrada_tarifa = ttk.Entry(frame, width=22)
        self.entrada_tarifa.grid(row=3, column=1, sticky="w")
        ttk.Button(frame, text="Register Vehicle", command=self.registrar_auto).grid(row=4, column=0, columnspan=2, pady=15)
        #--------------------------#
        #--|tablero_de_automovil|--#
        #--------------------------#
        columnas = ("plate", "entry", "rate")
        self.tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=10)
        self.tabla.heading("plate", text="License Plate")
        self.tabla.heading("entry", text="Entry Time")
        self.tabla.heading("rate", text="Hourly Rate")
        self.tabla.column("plate", width=150, anchor="center")
        self.tabla.column("entry", width=120, anchor="center")
        self.tabla.column("rate", width=130, anchor="center")
        self.tabla.grid(row=1, column=2, rowspan=5, columnspan=3, padx=(30, 0))
        #------------------------#
        #--|registro_de_salida|--#
        #------------------------#
        ttk.Label(frame, text="Exit Time (0-24):").grid(row=6, column=2, sticky="e", pady=20)
        self.entrada_salida = ttk.Entry(frame, width=15)
        self.entrada_salida.grid(row=6, column=3, sticky="w", pady=20)
        ttk.Button(frame, text="Register Exit and Calculate", command=self.registrar_salida).grid(row=6, column=4, padx=10, pady=20)
        ttk.Button(frame, text="Logout", command=self.mostrar_login).grid(row=7, column=4, sticky="e")
#-------------------------------------------#
#--|funcionalidad_control_de_credenciales|--#
#-------------------------------------------#
class Usuario:
    def __init__(self):
        self.__usuario = "programación"
        self.__password = "programación"
    def validar(
        self, usuario_ingresado, password_ingresada):
        return (usuario_ingresado == self.__usuario and password_ingresada == self.__password)
#----------------------------------------#
#--|vehiculos_que_ingresan_al_servicio|--#
#----------------------------------------#
class AutoLavado:
    def __init__(self, placa, hora_ingreso, tarifa_hora):
        self.__placa = placa
        self.__hora_ingreso = None
        self.__tarifa_hora = tarifa_hora
        self.__hora_salida = None
        self.registrar_ingreso(hora_ingreso)
    def registrar_ingreso(self, hora):
        self.__hora_ingreso = hora
    def registrar_salida(self, hora):
        if hora <= self.__hora_ingreso:
            raise ValueError("Exit time must be greater than entry time.")
        self.__hora_salida = hora
    def calcular_pago(self, hora_salida):
        if hora_salida <= self.__hora_ingreso:
            raise ValueError("Exit time must be greater than entry time.")
        horas_servicio = (hora_salida - self.__hora_ingreso)
        pago_total = (horas_servicio * self.__tarifa_hora)
        return pago_total
    def obtener_placa(self):
        return self.__placa
    def obtener_hora_ingreso(self):
        return self.__hora_ingreso
    def obtener_tarifa_hora(self):
        return self.__tarifa_hora
#-------------------------------#
#--|funcionalidad_del_sistema|--#
#-------------------------------#
class CarWashSystem(CarWashSystem):
    def validar_login(self):
        usuario_ingresado = (self.entrada_usuario.get().strip())
        password_ingresada = (self.entrada_password.get())
        if self.usuario.validar(usuario_ingresado, password_ingresada):
            self.mostrar_sistema()
        else:
            messagebox.showerror("Access denied", "Incorrect username or password.")
    #-------------------------#
    #--|validacion_de_horas|--# 
    #-------------------------#
    @staticmethod
    def validar_hora(valor):
        try:
            hora = float(valor)
        except ValueError:
            raise ValueError("Time must be a numeric value.")
        if hora < 0 or hora > 24:
            raise ValueError("Time must be between 0 and 24.")
        return hora
    #-------------------------#
    #--|registrar_automovil|--#
    #-------------------------#
    def registrar_auto(self):
        try:
            placa = (self.entrada_placa .get() .strip() .upper())
            if placa == "":
                raise ValueError("License plate is required.")
            for auto in self.lista_autos:
                if auto.obtener_placa() == placa:
                    raise ValueError("This license plate is already registered.")
            hora_ingreso = self.validar_hora(self.entrada_hora .get() .strip())
            try:
                tarifa = float(self.entrada_tarifa .get() .strip())
            except ValueError:
                raise ValueError("Hourly rate must be numeric.")
            if tarifa <= 0:
                raise ValueError("Hourly rate must be greater than zero.")
            nuevo_auto = AutoLavado(placa, hora_ingreso, tarifa)
            self.lista_autos.append(nuevo_auto)
            self.tabla.insert("", "end",
                values=(placa, f"{hora_ingreso:.2f}", f"${tarifa:,.2f}"))
            messagebox.showinfo("Vehicle Registered", "Vehicle registered successfully.")
            self.limpiar_campos_ingreso()
        except ValueError as error:
            messagebox.showerror("Invalid data", str(error))
    #-------------------------#
    #--|registrar_la_salida|--#
    #-------------------------#
    def registrar_salida(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Selection required", "Please select a vehicle.")
            return
        try:
            hora_salida = self.validar_hora(self.entrada_salida .get() .strip())
            item = seleccion[0]
            datos = self.tabla.item(item, "values")
            placa = datos[0]
            auto_seleccionado = None
            for auto in self.lista_autos:
                if auto.obtener_placa() == placa:
                    auto_seleccionado = auto
                    break
            if auto_seleccionado is None:
                raise ValueError("Vehicle was not found.")
            pago = auto_seleccionado.calcular_pago(hora_salida)
            auto_seleccionado.registrar_salida(hora_salida)
            horas = (hora_salida - auto_seleccionado.obtener_hora_ingreso())
            messagebox.showinfo(
                "Payment Summary",
                f"License Plate: {placa}\n"
                f"Entry Time: "
                f"{auto_seleccionado.obtener_hora_ingreso():.2f}\n"
                f"Exit Time: {hora_salida:.2f}\n"
                f"Service Time: {horas:.2f} hours\n"
                f"Hourly Rate: "
                f"${auto_seleccionado.obtener_tarifa_hora():,.2f}\n"
                f"Total Payment: ${pago:,.2f}")
            self.lista_autos.remove(auto_seleccionado)
            self.tabla.delete(item)
            self.entrada_salida.delete(0, tk.END)
        except ValueError as error:
            messagebox.showerror("Invalid data", str(error))
    #----------------------#
    #--|campos_a_limpiar|--#
    #----------------------#
    def limpiar_campos_ingreso(self):
        self.entrada_placa.delete(0, tk.END)
        self.entrada_hora.delete(0, tk.END)
        self.entrada_tarifa.delete(0, tk.END)
        self.entrada_placa.focus()
#----------------------------#
#--|iniciador_del_programa|--#
#----------------------------#
if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = CarWashSystem(ventana)
    ventana.mainloop()