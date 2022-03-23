class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    nombre_banco = "Cuenta Independencia Bank07"
    def __init__(self, tasa_interes=0.02, balance=0.0): 
        self.tasa_interes = tasa_interes
        self.balance = balance
    def deposito(self, amount=0.0):
        self.balance +=amount
        return self
    def retiro(self, amount):
        self.balance -=amount
        return self
    def mostrar_info_cuenta(self):
        print("Estimado tienes un balance de cuenta de:", self.balance)
    def generar_interes(self):
        self.balance+=(self.balance*self.tasa_interes)
        return self
    def transferencia(self, other_user, amount):
        self.retiro(amount)
        other_user.deposito(amount)
        print("se hizo la transferencia!!!")
class Usuario:
    # los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
    # ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
    	# los asignamos en consecuencia
        self.name = name
        self.email = email_address
        self.cuenta = CuentaBancaria(tasa_interes=0.02, balance=0.0)
    def hacer_retiro(self, amount=0.0):
        self.cuenta.retiro(amount)
        return self
        # print("Tienes un balance de cuenta de:", self.balance_cuenta)
    def hacer_deposito(self, amount=0.0):
        self.cuenta.deposito(amount)
        return self
    def mostrar_balance_usuario(self):
        self.cuenta.mostrar_info_cuenta()
    def transfer_dinero(self, other_user, amount):
        self.cuenta.transferencia(self, other_user, amount)
    # def _metodo_ejemplo(self):
    # 	# podemos llamar a los métodos de instancia de CuentaBancaria
    #     self.cuenta.deposito(100)
    # 	# o acceder a sus atributos
    #     print(self.cuenta.balance)
    #     self.cuenta.mostrar_info_cuenta()
        
primera_cuenta=CuentaBancaria()
segunda_cuenta=CuentaBancaria()
macos=Usuario("jhonDoe", "jhonDoe@gmail.com")
linux=Usuario("root", "toor@gmail.com")
linux.hacer_deposito(7000).mostrar_balance_usuario()
macos.hacer_deposito().mostrar_balance_usuario()