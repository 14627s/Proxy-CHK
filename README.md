# Proxy CHK

This Python script checks a list of proxies for connectivity and saves the working proxies to an output file.

### Features:
- Validates proxies from a text file (`proxies.txt`).
- Configuration settings managed via `config.ini` for timeout and file paths.
- Simple and easy-to-use.

### Usage:
1. Ensure Python 3.x is installed.
2. Modify `config.ini` to set your preferred timeout and file paths.
3. Run `proxy_checker.py` to validate proxies and generate `output.txt`.

### Configuration (`config.ini`):
- `timeout`: Timeout duration (in seconds) for each proxy check.
- `proxies_file`: Path to the text file containing the list of proxies.
- `output_file`: Path to the output file where working proxies will be saved.

### Default (`config.ini`):
```ini
[Settings]
timeout = 5
input_file = proxies.txt
output_file = output.txt
