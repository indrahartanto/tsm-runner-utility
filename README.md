# tsm-runner-utility

Utility program to run tsm command

## Setup

1. Download cryptography (to encrypt pwd string), run `pip install cryptography` in cmd

2. Populate the config section of tsm.py accordingly:
   
    **user**: Tableau system account

    **pwd**: Run `python encrypt.py` to encrypt the password for Tableau system account and paste the encrypted pwd string

    **key_file**: Don't need to change

    **timeout_seconds_zip_log**: Timeout in seconds for ziplogs command, default (5400 seconds = 1.5 hrs)

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

Type `python tsm.py command [-h] [--param="PARAM"]` to run the utility

| command | (optional/mandatory) PARAM | TSM command that will be run | 
| -------- | -------- | -------- |
| restart   || tsm restart   |
| start   || tsm start   |
| stop   || tsm stop   |
| status   || tsm status -v   |
| cleanup   | (optional) "--http-request-table-retention 30 --log-files-retention 5"| tsm maintenance cleanup -r -t &lt;optional PARAM&gt;   |
| ziplogs   | (optional) "-m mm/dd/yyyy"| tsm maintenance ziplogs --request-timeout &lt;timeout from config&gt; &lt;optional PARAM&gt;   |
| set   | (mandatory) "-k &lt;config.key&gt; -v &lt;config_value&gt;"| tsm configuration set &lt;mandatory PARAM&gt;   |
| get   | (mandatory) "-k &lt;config.key&gt;| tsm configuration get &lt;mandatory PARAM&gt;   |
| apply   | | tsm pending-changes apply   |

tsm commands reference https://onlinehelp.tableau.com/current/server/en-us/tsm.htm