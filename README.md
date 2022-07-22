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


### Sample Example file

```text
# This is an example file used for parsing.
START_DATE: 2022-05-22 05:18:00
NAME: SOME ONE
# Table Data
DATA:
INDEX	PARAM	VALUE	PASS
1	PARAM1	1.0	TRUE
2	PARAM1	1.5	TRUE
3	PARAM2	1.6	TRUE
4	PARAM2	5	FALSE
END
END_DATE: 2022-05-22 05:20:00
```