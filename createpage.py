from mako.template import Template
from mako.lookup import TemplateLookup
import util
import os


class BlogEntry:
    def __init__(self, filename):
        self.root = os.path.abspath(os.path.dirname(__file__))
        self.name = filename
        self._load()

        myLookup = TemplateLookup(directories=['.'], output_encoding='utf-8', encoding_errors='replace')

        self.template = Template(filename = os.path.join("design",self.config['theme'],'single.html'), lookup = myLookup)

        self.render()

        self.logger.info("Done")

    def _load(self):
        config_filename = "config.ini"
        self.config = util.parse_config(config_filename)

        #Set up logging
        self._logger()
        self.logger.info("Loaded config")

        #Read file and store header and content
        with open(self.name,'r') as f:
            self.raw_header, self.raw_content = f.read().split('---')
        self.logger.info("Read raw header and content")

        self.header = util.parse_header(self.raw_header)
        self.logger.info("Parsed header into a dict")


    def _logger(self):
        import logging

        # create logger
        self.logger = logging.getLogger('blog')

        numeric_level = getattr(logging, self.config['loglevel'].upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        self.logger.setLevel(numeric_level)

        # create blog handler and set level to debug
        fh = logging.FileHandler(self.config['logfile'])
        fh.setLevel(numeric_level)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # add formatter to ch
        fh.setFormatter(formatter)

        # add ch to self.logger
        self.logger.addHandler(fh)


    def update_header(self):
        pass

    def render(self):
        with open("sample1.html",'w') as outfh:
            outfh.write(self.template.render(html_content=self.raw_content))

if __name__=="__main__":
    entry = BlogEntry("test.txt")

