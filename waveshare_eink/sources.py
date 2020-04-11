from abc import ABC, abstractmethod
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from pathlib import Path

class Source(ABC):

    @abstractmethod
    def refresh(self, display):
        pass

class SourceHTML(Source):

    def __init__(self,url='http://127.0.0.1:8000', output_path='./display.png'):
        self.__url = url
        self.__output_path = output_path

    def refresh(self, display):
        css_path = Path(__file__).parent / 'style' / 'page.css'
        font_config = FontConfiguration()   
        HTML(self.__url).write_png(self.__output_path, stylesheets=[
            CSS(string=f'''
                @page {{ 
                    size: {display.width}px {display.height}px;
                    margin: 0cm;
                    padding: 0cm
                }}

                @font-face {{
                    font-family: 'Roboto';
                    font-style: normal;
                    font-weight: 400;
                    src: local('Roboto'), local('Roboto-Regular');
                }}

                body {{
                    background-color: #FFFFFF;
                    font-family: Roboto;
                    font-style: medium;
                    font-color: #000000;
                }}
                ''', font_config=font_config),
                CSS(css_path)
        ])

        return self.__output_path

    

