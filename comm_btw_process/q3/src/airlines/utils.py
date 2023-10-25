import argparse

def parse_args(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--host", default="localhost", help="Server host")
    parser.add_argument("--port", type=int, default=7896, help="Server port")
    return parser.parse_args()