# tsm start, stop, restart, ziplogs, status, set, get, cleanup
import argparse
import logging
import cryptography
import subprocess
import sys
import time
from cryptography.fernet import Fernet
from argparse import RawTextHelpFormatter

config = {
    "user": "sysdtableau",
    "pwd": "gAAAAABcunynW6xn2p7ACdNLwV96XkxqnTc5lK5W23zQikst9sGyIjkORRi8a5sX5X-ED0w07zrakxpfMA_LCr8bb0S2GLan3A==",
    "key_file": "key.key",
    "timeout_seconds_zip_log": 5400,
    "log_directory": "C:\\Users\\Indra\\Desktop\\Code\\" + time.strftime('tsm-runner-utility_%Y%m%d.log')
}

def switch_cmd(argument):
    tsm_cmd = {
        "restart": "tsm restart",
        "start": "tsm start",
        "stop": "tsm stop",
        "status": "tsm status -v",
        "cleanup": "tsm maintenance cleanup -r -t",
        "ziplogs": "tsm maintenance ziplogs --request-timeout " + str(config["timeout_seconds_zip_log"]) + " -f log" + time.strftime("%Y%m%d%H%M"),
        "set": "tsm configuration set",
        "get": "tsm configuration get",
        "apply": "tsm pending-changes apply"
    }
    return tsm_cmd.get(argument, "Invalid command passed")

def decrypt_string(pwd):
    file = open('key.key', 'rb')
    key = file.read()  # The key will be type bytes
    file.close()
    f = Fernet(key)
    decrypted = f.decrypt(pwd)
    return decrypted

# parser for input params
parser = argparse.ArgumentParser(
    description="Help instructions for tsm command runner utility", formatter_class=RawTextHelpFormatter)

parser.add_argument("command", type=str, help="enter tsm command to run, valid options are"
                                              "\nrestart: tsm restart"
                                              "\nstart: tsm start"
                                              "\nstop: tsm stop"
                                              "\nstatus: tsm status -v"
                                              "\ncleanup: tsm maintenance cleanup -r -t <additional params>"
                                              "\nziplogs: tsm maintenance ziplogs --request-timeout <timeout from config> <additional params>"
                                              "\nset: tsm configuration set <additional params>"
                                              "\nget: tsm configuration get <additional params>"
                                              "\napply: tsm pending-changes apply"
                    )
parser.add_argument("--param", type=str, default="", help="additional parameters to specify, e.g."
                    "\n\"-m mm/dd/yyyy\" for ziplogs to specify earliest date of log files to be included"
                    "\n\"-k <config.key> -v <config_value>\" for tsm configuration set/get"
                    "\n\"--http-requests-table-retention <days> --log-files-retention <days>\" for tsm cleanup"
                    )

args = parser.parse_args()

# setup logging
logging.basicConfig(level=logging.INFO, filename=config["log_directory"],  format="%(name)s - %(asctime)s - %(levelname)s - %(message)s")
logging.info("tsm-runner-utlity started")

# run commands
tsm_cmd = switch_cmd(args.command)

if tsm_cmd == "Invalid command passed":
    logging.error("Invalid command passed")
    sys.exit(1)

username_pwd = " -u " + config["user"] + " -p " + decrypt_string(config["pwd"])
final_cmd_clean = tsm_cmd + " " + str(args.param) + " -u " + config["user"] + " -p ******"
final_cmd = tsm_cmd + " " + str(args.param) + username_pwd

logging.info("running tsm command: %s", final_cmd_clean)

proc = subprocess.Popen(final_cmd, shell=True,
                    universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output, errors = proc.communicate()
if len(output) > 0:
    logging.info(output)

exit_code = proc.returncode

if exit_code != 0:
    logging.error("Error with exit code = %i", exit_code)
    logging.error(errors)
    sys.exit(1)
        
sys.exit()