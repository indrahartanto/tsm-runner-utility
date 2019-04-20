# tsm-runner-utility

Utility program to run tsm commands

## Setup

1. Download cryptography (to encrypt pwd string), run `pip install cryptography` in cmd

2. Populate the config section of tsm.py accordingly:
   
    **user**: Tableau system account

    **pwd**: Run `python encrypt.py` to encrypt the password for Tableau system account and paste the encrypted pwd string

    **key_file**: Don't need to change

    **timeout_seconds_zip_log**: Timeout in seconds for ziplogs command, default (1.5 hrs = 5400 seconds)

    **log_directory**: Replace log path with the log file folder, e.g. D:\\Tableau.Utilities\\Log\\tsm-runner-utility

    ```python
   config = {
       "user": "sysdtableau",
       "pwd": "<encrypted pwd string>",
       "key_file": "key.key",
       "timeout_seconds_zip_log": 5400,
       "log_directory": "<log path>" + time.strftime('tsm-runner-utility_%Y%m%d.log')
   }
   ```

## Usage

| header 1 | header 2 |
| -------- | -------- |
| cell 1   | cell 2   |
| cell 3   | cell 4   |