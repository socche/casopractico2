from flask import Flask, request, redirect
import psycopg2
import os

app = Flask(__name__)

def get_db_conn():
    conn = psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"]
    )
    conn.autocommit = True
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_conn()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS votos (opcion TEXT)")
    if request.method == "POST":
        cur.execute("INSERT INTO votos (opcion) VALUES (%s)", (request.form["voto"],))
        return redirect("/")

    cur.execute("SELECT opcion, COUNT(*) FROM votos GROUP BY opcion")
    votos = dict(cur.fetchall())
    donuts = votos.get("donuts", 0)
    galletas = votos.get("galletas", 0)

    conn.close()

    return f"""
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                font-family: 'Arial', sans-serif;
                background: url('https://mascultura.mx/wp-content/uploads/2019/11/img-dest-homer.jpg') no-repeat center center fixed;
                background-size: cover;
                color: white;
                text-align: center;
                padding-top: 60px;
                backdrop-filter: brightness(0.6);
            }}
            h1 {{
                background-color: rgba(0, 0, 0, 0.7);
                display: inline-block;
                padding: 10px 20px;
                border-radius: 10px;
            }}
            .opciones {{
                display: flex;
                justify-content: center;
                gap: 50px;
                margin: 30px 0;
            }}
            .opciones form {{
                display: inline-block;
            }}
            .imagen-btn {{
                border: none;
                background: none;
                cursor: pointer;
            }}
            .imagen-btn img {{
                width: 150px;
                height: auto;
                transition: transform 0.2s;
                border-radius: 15px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.5);
            }}
            .imagen-btn img:hover {{
                transform: scale(1.1);
            }}
            .resultados {{
                margin-top: 30px;
                font-size: 24px;
                background-color: rgba(0, 0, 0, 0.6);
                display: inline-block;
                padding: 10px 30px;
                border-radius: 10px;
            }}
            .reset-form {{
                margin-top: 20px;
            }}
            .reset-form button {{
                padding: 8px 20px;
                font-size: 16px;
                border-radius: 8px;
                border: none;
                background-color: #f44336;
                color: white;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <h1>¿Qué prefiere Homer?</h1>
        <div class="opciones">
            <form method="post">
                <button class="imagen-btn" type="submit" name="voto" value="donuts">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Glazed-Donut.jpg/960px-Glazed-Donut.jpg" alt="Donut">
                </button>
            </form>
            <form method="post">
                <button class="imagen-btn" type="submit" name="voto" value="galletas">
                    <img src="https://www.modernhoney.com/wp-content/uploads/2019/01/The-Best-Chocolate-Chip-Cookies-2.jpg" alt="Galleta">
                </button>
            </form>
        </div>
        <div class="resultados">
            <p>🍩 Donuts: {donuts} votos</p>
            <p>🍪 Galletas: {galletas} votos</p>
        </div>
        <form method="post" action="/reset" class="reset-form">
            <button type="submit">🔄 Reset</button>
        </form>
    </body>
    </html>
    """


@app.route("/reset", methods=["POST"])
def reset():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS votos")
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)