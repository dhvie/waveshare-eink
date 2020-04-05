from abc import ABC, abstractmethod
from weasyprint import HTML, CSS
from pathlib import Path

class Source(ABC):

    @abstractmethod
    def refresh(self, display):
        pass

class SourceHTML(Source):

    def __init__(self,url='http://127.0.0.1:5000', output_path='./display.png'):
        self.__url = url
        self.__output_path = output_path

    def refresh(self, display):
        css_path = Path(__file__).parent / 'style' / 'page.css'
        HTML(self.__url).write_png(self.__output_path, stylesheets=[
            CSS(string=f'''
                @page {{ 
                    size: {display.width}px {display.height}px;
                    margin: 0cm;
                    padding: 0cm
                }}

                body {{
                    background-color: #FFFFFF;
                }}
                '''),
                CSS(css_path)
        ])

        return self.__output_path

    

