from pywebio import start_server
from pywebio.output import put_text

def app():
    put_text("Hello from PyWebIO on Heroku!")

if __name__ == "__main__":
    # Heroku передаёт порт через переменную окружения
    import os
    port = int(os.environ.get("PORT", 8080))
    start_server(app, port=port, host="0.0.0.0")
