from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>EMBELEZE</title>

        <style>

            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f8f3f7;
                text-align: center;
            }

            header {
                background: #222;
                color: white;
                padding: 35px 20px;
            }

            h1 {
                font-size: 42px;
                margin: 0;
            }

            .contenido {
                padding: 60px 20px;
            }

            .tarjeta {
                background: white;
                max-width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            }

            .estado {
                color: green;
                font-weight: bold;
                font-size: 20px;
            }

        </style>

    </head>

    <body>

        <header>

            <h1>✨ EMBELEZE</h1>

            <p>Salón de Belleza</p>

        </header>

        <div class="contenido">

            <div class="tarjeta">

                <h2>Bienvenido a EMBELEZE</h2>

                <p class="estado">
                    Sistema funcionando correctamente ✅
                </p>

                <p>
                    Próximamente podrás gestionar
                    clientes, tratamientos y turnos.
                </p>

            </div>

        </div>

    </body>

    </html>
    """


if __name__ == "__main__":
    app.run()
