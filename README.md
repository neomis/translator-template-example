# Translator Template Example

Translator Plugin for Example files

## How to Install

```bash
python3 -m venv /opt/translator_template
source /opt/translator_template/bin/activate
pip install --upgrade pip setuptools wheel
pip install translator_template_example
```

## How to Run

Process a single file

`translate_file <file_path> [--loglevel=(DEBUG, INFO, ERROR)]`

Run the spooler once

`translate_spool [--loglevel=(DEBUG, INFO, ERROR)]`

Run the spooler as a daemon

`translate_spool -d [--loglevel=(DEBUG, INFO, ERROR)]`

## Sample ENV FILE:

```bash
## GLOBAL SETTINGS
# ENVIRONMENT = PRODUCTION
# ENCODING = UTF-8

## SPOOLER SETTINGS
# THREADS = 4
# QUEUE_PATH = ./spooler/queued
# WORK_PATH = ./spooler/processing
# REJECT_PATH = ./spooler/rejected
# OUT_PATH = ./spooler/finished

## DAEMON SETTINGS
# PID_FILE = translator_template.pid
# LOG_FILE = translator_template.log
# LOG_LEVEL = ERROR
# SLEEP_TIME = 5
```
