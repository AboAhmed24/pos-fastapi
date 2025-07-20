import uvicorn

if __name__ == "__main__":
    try:
        import os, sys
        if getattr(sys, 'frozen', False):
            base_dir = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=5000,
            ssl_keyfile=os.path.join(base_dir, "key.pem"),
            ssl_certfile=os.path.join(base_dir, "cert.pem"),
        )
    except Exception as e:
        import traceback
        print("An error occurred:")
        traceback.print_exc()
        print("Current directory:", os.getcwd())
        print("key.pem path:", os.path.join(base_dir, "key.pem"))
        print("cert.pem path:", os.path.join(base_dir, "cert.pem"))
        print(e)
    input("Press Enter to exit...")
