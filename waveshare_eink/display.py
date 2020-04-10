from weasyprint import HTML, CSS
from argparse import ArgumentParser
from .display_manager import DisplayManager
from .sources import SourceHTML
import time

def main(args):
    display = DisplayManager()

    source = SourceHTML(url='http://127.0.0.1:5000/main')
    output_path = source.refresh(display)
    display.render_image(output_path)

    if args.refresh >= 0:
        output_path = source.refresh(display)
        display.render_image(output_path)
        time.sleep(args.refresh)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--refresh", type=int, default=-1)
    args = parser.parse_args()
    main(args)
