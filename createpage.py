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

        print "DONE!"

    def _load(self):
        config_filename = "config.ini"
        self.config = util.parse_config(config_filename)

        self._logger = self.logger()
        self._logger.info("Loaded config")

        #Read file and store header and content
        with open(self.name,'r') as f:
            self.raw_header, self.raw_content = f.read().split('---')
        self._logger.info("Read raw header and content")

        self.header = util.parse_header(self.raw_header)
        self._logger.info("Parsed header into a dict")

    def logger(self):
        import logging

        # create logger
        logger = logging.getLogger('blog')

        numeric_level = getattr(logging, self.config['loglevel'].upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        logger.setLevel(numeric_level)

        # create blog handler and set level to debug
        fh = logging.FileHandler(self.config['logfile'])
        fh.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # add formatter to ch
        fh.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(fh)

        return logger

    def update_header(self):
        pass

    def render(self):
        print "Rendering"
        with open("sample1.html",'w') as outfh:
            outfh.write(self.template.render(html_content=self.raw_content))

if __name__=="__main__":
    entry = BlogEntry("test.txt")

