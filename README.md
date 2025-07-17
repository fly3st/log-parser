
# Universal Log Parser

A real-time, format-aware log parser that detects common log formats (like generic app logs and Apache logs), parses them into structured JSON, and prints them in real time.

---

## Features

- Supports multiple log formats:
  - Generic logs: `TIMESTAMP - LEVEL - MESSAGE`
  - Apache access logs
- Real-time log monitoring (like `tail -f`)
- Auto-detects format per line
- Clean modular architecture
- Pretty printed output (optionally using `rich`)
- Export to JSON file (coming soon)
- Prometheus/Grafana metrics (planned)

---

## Project Structure

```
log_parser_project/
├── main.py           # Run this to start the log parser
├── parser.py         # Contains all log parsing logic
├── reader.py         # Real-time file-following logic
├── exporter.py       # (Coming soon) Handles JSON/metrics export
└── test_data/
    └── sample.log    # Sample input file to test real-time parsing
```

---

## Usage

1. Clone this repo or copy the files into your project folder
2. Run the main script:
   ```bash
   python main.py
   ```
3. In another tab or editor, open `test_data/sample.log` and add new log lines
4. The script will parse and display new lines in real time

---

## Example Log Inputs

**Generic Log Format:**
```
2025-07-12 22:38:17,123 - ERROR - Failed to connect to database
```

**Apache Access Log:**
```
127.0.0.1 - - [12/Jul/2025:22:38:17 +0000] "GET /index.html HTTP/1.1" 200 1024
```

---

## Dependencies

Only standard libraries for now:
- `re` (regex)
- `time`

Optional for pretty output:
- `rich` (install via `pip install rich`)

---

## Roadmap

- [x] Support for generic logs
- [x] Support for Apache logs
- [x] Real-time file following
- [ ] JSON output exporter
- [ ] Prometheus metrics exporter
- [ ] Support for syslog, nginx, docker logs
- [ ] Alerting / summary stats

---

## Author & Learning Purpose

Built step-by-step to learn:
- Clean Python architecture
- Regex and log parsing
- File IO and real-time systems
- Future integration with monitoring tools

---

## License

MIT
