import ConfigParser

def parse_header(raw_header):
    parsed_header = {}
    for line in raw_header.splitlines():
        try:
            (key, value) = line.split(":",1)
        except ValueError:
            raise Exception("The header %s is not in proper format, Use 'Key:Value' format" % line)
        parsed_header[key] = value

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

def textile(content):
    from textile import textile
    return textile(content)

def render(content, format):
    if format is "textile":
        outbuf = textile(content)

    return outbuf

def pygmentify(content):
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name, guess_lexer, guess_lexer_for_filename
    from pygments.formatters import HtmlFormatter
    from BeautifulSoup import BeautifulSoup

    formatter = HtmlFormatter(linenos=True, cssclass="codehilite")

    try:
        soup = BeautifulSoup(content)
        code_blocks = soup.findAll('code')

        for code in code_blocks:
            try:
                language = code['language']
                lexer = get_lexer_by_name(language, stripAll=True)

            except KeyError:
                lexer = guess_lexer(code.string, stripAll=True)

            code.replaceWith(highlight(code.string, lexer, formatter)
        return str(soup)

    except:
        return value.replace('<code>', '<div class="highlight"><pre>').replace('</code>', '</pre></div>')


