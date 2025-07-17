import re

def parse_generic_log_line(line: str):
    x = re.search(r'(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}) - (?P<level>[A-Z]+) - (?P<message>.+)', line)
    if x:
        return x.groupdict()
    return None

def parse_apache_log_line(line: str):
    x = re.search(r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s-\s-\s\[(?P<timestamp>[^\]]+)\]\s\"(?P<method>[A-Z]+)\s(?P<path>\S+)\s(?P<protocol>[^"]+)"\s(?P<status>\d{3})\s(?P<size>\d+)', line)
    if x:
        return x.groupdict()
    return None

def parse_log_line(line: str):
    for parser in [parse_generic_log_line, parse_apache_log_line]:
        result = parser(line)
        if result:
            return {
                'format' : parser.__name__.replace("parse_", "").replace("_log_line", ""),
                "log" : result
            }
    
    return None
