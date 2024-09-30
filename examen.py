from abc import ABC, abstractmethod
class SalarioInvalidoException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

#Aqui se mostrara la clase empleado la cual incluira los datos rfc,apellido, nombres 
class Empleado(ABC):
    def __init__(self, rfc, apellidos, nombres):
        self._rfc = rfc
        self._apellidos = apellidos
        self._nombres = nombres

    @abstractmethod
    def mostrar_informacion(self):
        pass

# Aqui se muetra la clase  hija EmpleadoVendedor la cual retornara el sueldo base , calculara el descuento y
#tambien calculara el sueldo neto 
class EmpleadoVendedor(Empleado):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision

        # Aqui se realaizara la validación del salario mínimo
        if self.calcular_ingresos() < 150:
            raise SalarioInvalidoException("El salario no puede ser menor a $150 ")

    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision

    def calcular_bonificacion(self):
        ingresos = self.calcular_ingresos()
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000:
            return ingresos * 0.05
        else:  # aqui si el monto vendido supera los 5000 se realiza una bonificacion del 10%
            return ingresos * 0.10

    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return ingresos * 0.11
        else:
            return ingresos * 0.15

    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        return ingresos + bonificacion - descuento

    def mostrar_informacion(self):
        print(f"RFC: {self._rfc}, Apellidos: {self._apellidos}, Nombres: {self._nombres}, "
              f"Monto Vendido: {self.monto_vendido}, Tasa de Comisión: {self.tasa_comision}, "
              f"Sueldo Neto: {self.calcular_sueldo_neto()}")

# Aqui en este apartado se crea la clase hija EmpleadoPermanente
class EmpleadoPermanente(Empleado):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, numero_seguro_social):
        super().__init__(rfc, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.numero_seguro_social = numero_seguro_social
    
        # Aqui se realiza la Validación del salario mínimo
        if self.sueldo_base < 150:
            raise SalarioInvalidoException("El salario no puede ser menor a $150 ")

    def calcular_ingresos(self):
        return self.sueldo_base

    def calcular_descuento(self):
        return self.sueldo_base * 0.11

    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        descuento = self.calcular_descuento()
        return ingresos - descuento

    def mostrar_informacion(self):
        print(f"RFC: {self._rfc}, Apellidos: {self._apellidos}, Nombres: {self._nombres}, "
              f"Sueldo Base: {self.sueldo_base}, Número de Seguro Social: {self.numero_seguro_social}, "
              f"Sueldo Neto: {self.calcular_sueldo_neto()}")


if __name__ == "__main__":
    try:
        vendedor1 = EmpleadoVendedor("RFC123", "Castro", "Camila_J8", 6000, 0.1)
        vendedor1.mostrar_informacion()

        permanente1 = EmpleadoPermanente("RFC456", "Garcia", "Pedro_J8", 2000, "SS123456")
        permanente1.mostrar_informacion()

    except SalarioInvalidoException as e:
        print(e)
