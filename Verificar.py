class Verificador:
    
    def __init__(self):
        self.buscaminas=False
        self.matriz=''
    
    def verificarbuscaminas(self):
        self.buscaminas=self.verificarFilas()
        
        if not self.buscaminas:
            self.buscaminas=self.verificarColumnas()
        
        if not self.triqui:
            self.triqui=self.verificarDiagonales()
        
        return self.triqui
            
    
    def verificarFilas(self, tablero):
        
        for fila in range(0,2):
            if tablero[fila][0]== tablero[fila][1] and tablero[fila][0]== tablero[fila][2] :
                self.buscaminas=True
        return self.buscaminas
    
    def verificarColumnas(self, tablero):
        for columna in range(0,2):
            if tablero[0][columna]== tablero[1][columna] and tablero[0][columna]== tablero[2][columna] :
                self.buscaminas=True
        return self.buscaminas
    
       