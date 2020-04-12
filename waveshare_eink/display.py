from weasyprint import HTML, CSS
from argparse import ArgumentParser
from .display_manager import DisplayManager
from .sources import SourceHTML
import time

def main(args):
    display = DisplayManager()

    source = SourceHTML(url='http://127.0.0.1:8000/main')

    if args.refresh >= 0:
        while True:
            output_path = source.refresh(display)
            display.render_image(output_path, clear_first=False)
            time.sleep(args.refresh)
    else :
        output_path = source.refresh(display)
        display.render_image(output_path)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--refresh", type=int, default=-1)
    args = parser.parse_args()
    main(args)
