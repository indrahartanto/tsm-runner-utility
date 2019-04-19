# tsm start, stop, restart, ziplogs, status, set, get, cleanup

import subprocess
import cryptography
import argparse
from cryptography.fernet import Fernet
from argparse import RawTextHelpFormatter

def switch_cmd(argument):
    tsm_cmd = {
        "restart": "tsm restart",
        "start": "tsm start",
        "stop": "tsm stop",
        "status": "tsm status -v",
        "cleanup": "tsm maintenance cleanup -r -t",
        "ziplogs": "tsm maintenance ziplogs --request-timeout 5400",
        "set": "tsm configuration set",
        "get": "tsm configuration get",
        "apply": "tsm pending-changes apply"
    }
    return tsm_cmd.get(argument, "Invalid command passed")

config =	{
  "user": "sysptableau",
  "pwd": "gAAAAABcuWraxdbQInIiL0LStjUtUsIhET3rB7UBqUYzyBIKaW2V8ZH3yaklaZXr8N37VUonPpDo84ZQQIZ4rk74eP9tSnFsjg==",
  "key_file": "key.key",
  "timeout_seconds_log_file": 5400
}

parser = argparse.ArgumentParser(description="Help instructions for tsm command runner utility", formatter_class=RawTextHelpFormatter)
parser.add_argument("command", type=str, help="enter tsm command to run, valid options are"
                                              "\nrestart: tsm restart"
                                              "\nstart: tsm start"
                                              "\nstop: tsm stop"
                                              "\nstatus: tsm status -v"
                                              "\ncleanup: tsm maintenance cleanup -r -t <additional params>"
                                              "\nziplogs: tsm maintenance ziplogs --request-timeout 5400 <additional params>"
                                              "\nset: tsm configuration set <additional params>"
                                              "\nget: tsm configuration get <additional params>"
                                              "\napply: tsm pending-changes apply"
                                              )
parser.add_argument("--param", type=str, help="additional parameters to specify, e.g."
                                              "\n\"-m mm/dd/yyyy\" for ziplogs to specify earliest date of log files to be included"
                                              "\n\"-k <config.key> -v <config_value>\" for tsm configuration set/get"
                                              "\n\"--http-requests-table-retention <days> --log-files-retention <days>\" for tsm cleanup"
                                              )
args = parser.parse_args()

print(args.command)
print(args.param)

tsm_cmd = switch_cmd(args.command)
print "running tsm command: ", tsm_cmd

# proc = subprocess.Popen([binary_path] + arguments, universal_newlines=True, stdout=subprocess.PIPE)
proc = subprocess.Popen([tsm_cmd], universal_newlines=True, stdout=subprocess.PIPE)
result = proc.communicate()[0]
exit_code = proc.returncode
if exit_code != 0:
  print "error with exit code = ", exit_code

