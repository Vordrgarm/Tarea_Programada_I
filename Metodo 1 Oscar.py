from bs4 import BeautifulSoup
import requests
import urllib2  


"""
Esta	función	debe	retornar el	nombre	y	el	código	IATA de	todos	(o	al	menos	los	
principales)	aeropuertos	internacionales	del	mundo.	La	función	debe	recibir	una	
letra	y	devolverá	el	nombre	y	código	de	los	aeropuertos	cuyo	nombre	inicie	con	la	
letra	del	parámetro	de	entrada.	Si	el	usuario	ingresa	‘*’	(asterico)	se	presentará	la	
información	de	TODOS	los	aeropuertos separados	y	ordenados	alfabeticamente.	
Debe	asegurar	la	robustez	de	la	función	y	evitar	a	toda	costa	la	entrada	de	datos	
que	puedan	comprometer	su	ejecución.	

"""


def obtenerCodigosAeropuerto(letra):
    while True:
        if letra in ["A", "B", "C", "D", "E", "F","G", "H" ,"I", "J" , "K" , "L", "M", "N","O", "P", "Q", "R","S","T","U","V","W","X","Y","Z", "*" ]:
            break;
        return  "El parametro ingresado no es valido";
    try:
        urlBase = "http://www.telcom.es/~gacias/naveg/iataicao.html";
        maxPages = 6;
        counter = 0;

        for i in range(1,maxPages):

            # Construyo la URL
            if i > 1:
                url = "http://www.telcom.es/~gacias/naveg/iataicao",i,".html" %(urlBase,i);
            else:
                url = urlBase;
            
              
            try:  
                f = urllib2.urlopen("url")
                resultado = f.read();
                print (resultado); 
                f.close()  
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")  

    except ValueError:
        print(":v jejejej")
