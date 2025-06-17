import argparse
import socket
from uvicorn import run
from .app import app


def main():
    parser = argparse.ArgumentParser(description="Run Jama OpenAPI Tool")
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to run the FastAPI server",
    )
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        if sock.connect_ex(("127.0.0.1", args.port)) == 0:
            print(f"Port {args.port} is already in use. Choose a different port.")
            return

    run(app, host="127.0.0.1", port=args.port)


if __name__ == "__main__":
    main()
