# @Time    : 2018/3/12 15:33
# @Author  : Niyoufa
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("SETTINGS_MODULE", "test_port.settings")
    os.environ.setdefault("OPTIONS_MODULE", "test_port.options")

    from torserver.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)