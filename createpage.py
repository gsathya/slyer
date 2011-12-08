from mako.template import Template
from mako.lookup import TemplateLookup
import util
import os
import logging
import time
from datetime import datetime

class BlogEntry:
    def __init__(self, filename):
        self.root = os.path.abspath(os.path.dirname(__file__))
        self.name = filename
        self._load()
        self.new_header = {}
        myLookup = TemplateLookup(directories=['.'],
                                  output_encoding='utf-8', encoding_errors='replace')

        self.template = Template(filename = os.path.join("design",self.config['theme'],'single.html'), lookup = myLookup)
        print self.raw_header

        self.update_header()
        self.write_header()
        self._render()

        self.logger.info("Done")

    def _load(self):
        config_filename = "config.ini"
        self.config = util.parse_config(config_filename)

        #Set up logging
        self.logger = util.logger(self.config['loglevel'], self.config['logfile'])
        self.logger.info("Loaded config")

        #Read file and store header and content
        with open(self.name,'r') as f:
            self.raw_header, self.raw_content = f.read().split('---')
        self.logger.info("Read raw header and content")

        self.header = util.parse_header(self.raw_header)
        self.logger.info("Parsed header into a dict")

    def update_header(self):
        self.header['link'] = util.create_link(self.header['title'])
        self.header['timestamp'] = time.time()
        self.header['date'] = datetime.now().strftime("%A, %B %d, %Y")

    def write_header(self):
        with open(self.name,'r+') as f:
            f.seek(0)
            for key, value in self.header.items():
                f.write(str(key)+" : "+str(value)+"\n")
            f.write("---\n")
            f.write(self.raw_content)

    def _render(self):
        self.html_content = util.render(self.raw_content,
                                        self.config['format'].lower(), self.config['linenos'].lower())
        with open(self.header['link']+".html",'w') as outfh:
            outfh.write(self.template.render(html_content=self.html_content))

if __name__=="__main__":
    entry = BlogEntry("test.txt")


