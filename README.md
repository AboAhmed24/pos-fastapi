# Python FastAPI Project

## Dependencies

- [`python-escpos[all]`](requirements.txt)
- [`fastapi[standard]`](requirements.txt)
- [`uv`](requirements.txt)
- [`pyinstaller`](requirements.txt)

## Quickstart

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Run the FastAPI app:
    ```
    uv main.py
    ```
3. Build executable (optional):
    ```
    pyinstaller main.py
    ```

## API

- GET `/` returns a welcome message.
