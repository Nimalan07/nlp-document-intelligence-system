import os
import threading
import webbrowser

import uvicorn


def open_browser():
    webbrowser.open(
        "http://127.0.0.1:8000/docs"
    )


if __name__ == "__main__":
    threading.Timer(
        1.5,
        open_browser
    ).start()

    uvicorn.run(
        "api.app:app",
        host="0.0.0.0",
        port=int(
            os.environ.get(
                "PORT",
                8000
            )
        ),
        reload=True
    )