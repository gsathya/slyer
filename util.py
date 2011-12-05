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
