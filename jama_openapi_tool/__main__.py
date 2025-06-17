import argparse
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
    run(app, host="127.0.0.1", port=args.port)


if __name__ == "__main__":
    main()
