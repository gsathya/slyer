from mako.template import Template
from mako.lookup import TemplateLookup
import util
import os


class BlogIndex:
    def __init__(self):
        self.root = os.path.abspath(os.path.dirname(__file__))
        self._load()

        myLookup = TemplateLookup(directories=['.'],
                                  output_encoding='utf-8', encoding_errors='replace')

        self.template = Template(filename = os.path.join("design",self.config['theme'],'index.html'), lookup = myLookup)

        self._render()

    def _load(self):
        config_filename = "config.ini"
        self.config = util.parse_config(config_filename)

        #Set up logging
        self.logger = util.logger(self.config['loglevel'], self.config['logfile'])
        self.logger.info("Loaded config")

    def _render(self):
        # Send date, permalink, filepath, title
        with open("SampleIndex.html",'w') as outfh:
            outfh.write(self.template.render(html_content="hi"))
        self.logger.info("Done")

    def _walk(self):
        # Walk through /drafts to check for published posts and parse_header
        pass


if __name__=="__main__":
    index = BlogIndex()
