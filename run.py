"""
Punto de entrada de la aplicaicon Flask
Inicializa el servidor de desarrollo
"""


from todor import create_app

if __name__ == '__main__':
    app2 = create_app()
    app2.run(debug = True, port = 5001)