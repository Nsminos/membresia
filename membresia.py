from abc import abstractmethod, ABC

class Membresia(ABC):
    def __init__(self, correo_electronico:str, numero_tarjeta:str):
        self.__correo_electronico = correo_electronico
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_electronico(self):
        return self.__correo_electronico

    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia:int):
        pass

    def _crear_nueva_membresia(self, nueva_membresia:int):
        if nueva_membresia == 1:
            return Basica(self.correo_electronico, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_electronico, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_electronico, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_electronico, self.numero_tarjeta)


class Gratis(Membresia):
    costo = 0
    cantidad_dispositivos = 1
    
    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia <1 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

class Basica(Membresia):
    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_electronico:str, numero_tarjeta:str):
        super().__init__(correo_electronico, numero_tarjeta)
        if isinstance(self, Pro):
            self.__dias_regalo = 15
        elif isinstance(self, Familiar) or isinstance(self, SinConexion):
            self.__dias_regalo = 7

        
    @property
    def dias_regalo(self):
        return self.__dias_regalo
    def cancelar_suscripcion(self):
        return Gratis(self.correo_electronico, self.numero_tarjeta)
    #aqui se debe validar que la suscripcion ingresada sea 2,3,4
    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia <2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
    

class Familiar(Basica):
    costo = 5000
    cantidad_dispositivos = 5

    #aqui se debe validar que la suscripcion ingresada sea 2,3,4
    
    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia not in [1,3,4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
    
    def modificar_control_parental(self):
        pass
    

class SinConexion(Basica):
    costo = 3500
    cantidad_dispositivos = 2

    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia not in [1,2,4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
    
    def incrementar_cantidad_maxima_offline(self):
        pass

class Pro(Familiar, SinConexion):
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia:int):
        if nueva_membresia not in [1,2,3]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

gratis = Gratis("correo@prueba.cl", "123 456 789")
print(type(gratis))
basico = gratis.cambiar_suscripcion(1)
print(type(basico))
familiar = basico.cambiar_suscripcion(2)
print(type(familiar))
print(familiar.dias_regalo)
sin_conexion = familiar.cambiar_suscripcion(3)
print(type(sin_conexion))
print(sin_conexion.dias_regalo)
pro = sin_conexion.cambiar_suscripcion(4)
print(type(pro))
print(pro.dias_regalo)

g2 = pro.cancelar_suscripcion()
print(type(g2))