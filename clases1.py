class Persona:
    def __init__(self, nombre, apellido, edad) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        
    def saludar(self):
        print("hola")
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def edad(self):
        return self._edad
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
    
            
class Calculadora:
    def __init__(self, operador1, operador2) -> None:
        self.operador1 = operador1
        self.operador2 = operador2
    
    def sumar(self):
        return self.operador1 + self.operador2

    def restar(self):
        return self.operador1 - self.operador2
    
    def multiplicar(self):
        return self.operador1 * self.operador2
    
    def dividir(self):
        return self.operador1 / self.operador2

class Cubo:
    def __init__(self, ancho, profundidad, alto) -> None:
        self.ancho = ancho
        self.profundidad = profundidad
        self.alto = alto
        
    def volume(self) -> int:
        return self.ancho * self.profundidad * self.alto
        
class Persona2:
    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs
        
    def mostrar(self):
        print(f"persona2: {self.args} \n {self.kwargs}")
        
# persona= Persona2(1, 2, 3, "matias", nombre="matias", edad=25)
# persona.mostrar()
if __name__ == "__main__":
    print("Creando objeto".center(60,"-"))
    persona = Persona("matias", "arregui", 25)
    print(persona.nombre)
    persona.nombre = "nicolas"
    print(persona.nombre)
