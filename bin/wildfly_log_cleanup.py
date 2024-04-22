#!/usr/bin/env python3

# Prune wildfly logs that are older than a certain age.

import os
import glob
import subprocess

WF_LIST = ["wildfly", "wildfly2"]
DAYS_TO_KEEP = 30
FILES_TO_PROCESS = ["server.log", "access_log"]

def compress_logs(log_dir):
    os.chdir(log_dir)
    for file_name in FILES_TO_PROCESS:
        for log_file in glob.glob(file_name + ".*[0-9]"):
            if os.path.isfile(log_file):
                print(f"compressing {log_file}")
                subprocess.run(["xz", "-z", log_file])

def cleanup_old_logs(log_dir):
    os.chdir(log_dir)
    for file_name in FILES_TO_PROCESS:
        print(f"removing old {file_name} log files in {log_dir}")
        for log_file in glob.glob(file_name + ".*[0-9]"):
            if os.path.isfile(log_file):
                subprocess.run(["find", ".", "-name", file_name + ".*", "-type", "f", "-mtime", "+" + str(DAYS_TO_KEEP), "-exec", "rm", "-Rfv", "{}", "+"])

for wf in WF_LIST:
    log_dir = os.path.join(os.getenv("HOME"), wf, "standalone", "log")
    print(log_dir)
    cleanup_old_logs(log_dir)
    compress_logs(log_dir)

