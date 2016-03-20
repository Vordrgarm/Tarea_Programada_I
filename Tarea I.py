try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

html = urlopen("https://es.wikipedia.org/wiki/POST")
#print(html.read())



def recorer():
    z= html.read()
    x = 0 ;
    while x< 15:
        print(z[x]);
        x =x+1
        
