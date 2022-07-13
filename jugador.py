import random
class Jugador:
    
    
    
    def realizarJugada(self):
    
        simbolo=self.seleccionarJugador()
        
        if simbolo=='X':
            self.jugarComputador()
        else:
            self.jugarUsuario()
    
    
    
    def seleccionarJugador(self, simbolo):
        if simbolo=='X':
            simbolo='O'
        else:
            simbolo='X'
        return simbolo
    
    def jugarUsuario(self, tablero, simbolo):
        
        terminar=False        
        while not terminar:
            #Generar dos números al usuario
            x=int(input("Ingresar X:"))
            y=int(input("Ingresar Y:"))
            
            #Verificar si la casilla del tablero está vacía
            if not (tablero[x][y]=='O' or tablero[x][y]=='X'):
                terminar=True    
        
        tablero[x][y]=simbolo
        
        return tablero
    
    def jugarComputador(self, tablero, simbolo):
        
        terminar=False        
        while not terminar:
            #Pedir dos números al usuario
            x=random.randint(0,2)
            y=random.randint(0,2)
            
            #Verificar si la casilla del tablero está vacía
            if not (tablero[x][y]=='O' or tablero[x][y]=='X'):
                terminar=True    
        
        tablero[x][y]=simbolo
        
        return tablero