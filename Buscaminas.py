import random
class Creador:
    
    def __init__(self):
        self.tablero=[]
    
    def crearTablero(self,n, m):
        
        for fila in range(0,n):
            self.tablero.append([])            
            for columna in range (0,m):                
                self.tablero[fila].append('')
        return self.tablero
    
    def distribuirMinas(self, tablero, minas):
        
        n=len(tablero)
        m=len(tablero[1])
        
        for _ in range(0,minas):
            
            terminar=False
            
            while not terminar:
                
                x=random.randint(0,n-1)
                y=random.randint(0,m-1)
                
                if (not (tablero[x][y] == 'M')):
                    tablero[x][y]='M'
                    terminar=True
        self.tablero=tablero
        
        return tablero
                    
                
            
            
            
        
        

miCreador=Creador()

miTablero=miCreador.crearTablero(10,10)


miTablero=miCreador.distribuirMinas(miTablero, 25)

for fila in miTablero:
    print (fila)                
        
