from flask import Flask, render_template #, request, redirect, url_for, flash, session
# importar la clase Flask de la librería flask
# Flask es una clase que permite crear una aplicación web, es la clase principal de la librería Flask
# Flask es un microframework que permite crear aplicaciones web, es un microframework porque es simple y no tiene muchas dependencias
# Flask no tiene una capa de abstracción de base de datos, pero se pueden usar extensiones para interactuar con bases de datos
# Flask es una aplicación web WSGI, WSGI es una especificación de Python que define cómo las aplicaciones web pueden comunicarse con los servidores web
# Flask es una aplicación web WSGI, se ejecuta en un servidor web WSGI como Gunicorn o uWSGI

# Crear la aplicación
# iniciar la aplicación de flask
app= Flask(__name__)

#ruta de la página principal
@app.route('/') # el decorador "@" define la ruta principal 
def index():# definimos la ruta princal 
    return render_template('index.html') # lo que devuelve la ruta" 
    # render_template es una función de Flask que permite renderizar plantillas HTML        
    # render_template recibe como argumento el nombre de la plantilla que se quiere renderizar  
    # render_template busca la plantilla en la carpeta "templates" que se debe crear en el directorio del proyecto  

@app.route('/dashboard') # el decorador "@" define la ruta principal 
def dashboard():# definimos la ruta princal 
    return render_template('dashboard.html') # lo que devuelve la ruta" 
    # render_template es una función de Flask que permite renderizar plantillas HTML        
    # render_template recibe como argumento el nombre de la plantilla que se quiere renderizar  
    # render_template busca la plantilla en la carpeta "templates" que se debe crear en el directorio del proyecto  


@app.route('/contact') # el decorador "@" define la ruta principal
def contact():
    return render_template('contact.html')  # lo que devuelve la ruta"      
    # render_template es una función de Flask que permite renderizar plantillas HTML    

@app.route('/register') # el decorador "@" define la ruta principal   
def register(): 
    return render_template('register.html') # lo que devuelve la ruta"          

if __name__ == '__main__':
    app.run(debug=True) # correr la aplicación en el servidor local, debug=True
    # para que se actualice automáticamente cuando se hagan cambios sin volver a correr la aplicación
    # al correr la app con run se solciita que se ejecute la aplicación "app" que se inicio al principio del código

