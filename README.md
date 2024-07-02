# Proxy CHK

This Python script checks a list of proxies for connectivity and saves the working proxies to an output file.

### Features:
- Validates proxies from a text file (`proxies.txt`).
- Configuration settings managed via `config.ini` for timeout and file paths.
- Simple and easy-to-use.

### Usage:
1. Ensure Python 3.x is installed.
2. Modify `config.ini` to set your preferred timeout and file paths.
3. Run `proxychk.py` to start checking proxies and save it on  `output.txt`.

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
```
![image](https://github.com/14627s/Proxy-CHK/assets/173080010/8c004db0-a7ab-46b7-9b8a-53de07bab594)
![image](https://github.com/14627s/Proxy-CHK/assets/173080010/d59678c4-687f-4225-8b43-c0c532456288)
