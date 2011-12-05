from mako.template import Template
from mako.lookup import TemplateLookup
import utils

class BlogEntry:
    def __init__(self,filepath):
        self.path = filepath
        self.debug = False
        self.verbose = False

        #Read file and store header and content
        with (self.path,'r') as f:
            self.raw_header, self.raw_content = f.read().split('---')

        self.header = utils.parse_header(self.raw_header)

        if self.debug or self.verbose:
            print "Raw Header : \n" + self.raw_header
            print "Raw Content : \n" + self.raw_content
            print "Parsed Header : \n" + self.header

        myLookup = TemplateLookup(directories=['.'], output_encoding='utf-8', encoding_errors='replace')
        myTemplate = Template(filename='design/single.html', lookup=myLookup)

    def _render(self,**context)
        with open("sample1.html",'w') as outfh:
            outfh.write(mytemplate.render(html_content="SATHYA IT WORKS!"))
