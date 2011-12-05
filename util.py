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

def parse_config(config_file):
    config = ConfigParser.ConfigParser()
    config.read(config.file)

    parsed_config = {}
    for section in config.sections():
        entries = config.items(section)

        for (key, value) in entries:
            parsed_config[key] = value

    return parsed_config

