import ConfigParser

def parse_header(raw_header):
    parsed_header = {}
    for line in raw_header.splitlines():
        try:
            (key, value) = line.split(":")
        except ValueError:
            raise Exception("The header %s is not in proper format, Use 'Key:Value' format" % line)
        parsed_header[key.strip()] = value.strip()
    return parsed_header

def parse_config(config_filename):
    configParser = ConfigParser.ConfigParser()
    configParser.read(config_filename)

    config = {}
    for section in configParser.sections():
        entries = configParser.items(section)
        for (key, value) in entries:
            config[key] = value

    return config

def textile(content, linenos):
    from textile import textile
    return pygmentify(textile(content), linenos)


def render(content, format=None, linenos=False):
    if linenos == "true":
        linenos = True
    else:
        linenos = False

    if format is "textile":
        html_content = textile(content, linenos)
    else:
        html_content = textile(content, linenos)
    return html_content

def pygmentify(content, linenos):
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name, guess_lexer
    from pygments.formatters import HtmlFormatter
    from BeautifulSoup import BeautifulSoup

    formatter = HtmlFormatter(linenos=linenos, cssclass="codehilite")
    try:
        soup = BeautifulSoup(content)
        code_blocks = soup.findAll('code')

        for code in code_blocks:
            try:
                language = code['language']
                lexer = get_lexer_by_name(language, stripAll=True)
            except KeyError:
                lexer = guess_lexer(code.string, stripAll=True)
            code.replaceWith(highlight(code.string, lexer, formatter))
        return str(soup)
    except:
        return content.replace('<code>', '<pre>').replace('</code>', '</pre>')

def create_link(title):
    import re

    #Replace all non-word chars with '-'
    link = re.sub(r'\W+', '-', title.lower())
    #Replace multiple '-' with single '-', use only first 30 chars
    return re.sub(r'-+', '-', link).strip('-')[:30]



def logger(loglevel, logfile):
    import logging

    # create logger
    logger = logging.getLogger('blog')

    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logger.setLevel(numeric_level)

    # create blog handler and set level to debug
    fh = logging.FileHandler(logfile)
    fh.setLevel(numeric_level)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # add formatter to ch
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(fh)
    return logger

def isdraft(publish):
    if publish == "Yes":
        return True
    else:
        return False
