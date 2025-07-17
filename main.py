from reader import follow
from parser import parse_log_line

def main():
    with open("test_data/sample.log", "r") as logfile:
        for line in follow(logfile):
            parsed = parse_log_line(line)
            if parsed:
                print(parsed)
            else:
                print("Unrecognized format: ", line)

if __name__ == "__main__":
    main()