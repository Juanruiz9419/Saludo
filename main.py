from datetime import datetime
import pytz

class Greeter:
    def __init__(self, timezone='UTC'):
        self.timezone = pytz.timezone(timezone)

    def determinar_saludo(self):
        # Obtener la hora actual en la zona horaria especificada
        hora_actual = datetime.now(self.timezone).hour

        # Determinar el saludo según la hora del día
        if 5 <= hora_actual < 12:
            saludo = "Buenos días"
        elif 12 <= hora_actual < 18:
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"

        return saludo

    def saludar(self):
        saludo_del_dia = self.determinar_saludo()
        print(saludo_del_dia)

    def saludar(self, texto_adicional=''):
        hora_actual = datetime.now(self.timezone).strftime("%H:%M:%S")
        saludo_del_dia = self.determinar_saludo()
        mensaje = f"{saludo_del_dia}, {texto_adicional}. La hora actual es: {hora_actual}"
        print(mensaje)

# Uso de la clase Greeter con zona horaria específica (por ejemplo, 'America/New_York')
greeter = Greeter(timezone='America/Bogota')
greeter.saludar('Juan Ruiz')


