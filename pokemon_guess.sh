#!/bin/bash
cd ./src
if ! [[ -x "$(command -v python)" ]] | [[ -x "$(command -v python3)" ]]
then
	echo 'Error: 
		This program runs on Python, but it appears that Python is not installed on your system.
		For information on how to install Python, check out https://realpython.com/installing-python/' >&2
	exit 1
if [[ -x "$(command -v python)" ]]
then 
    python_version="$(command python -V)"
    if [[ $python_version == "Python 3"* ]]
    then
        python -m venv .venv 
        source .venv/bin/activate
        pip3 install -r ./requirements.txt
        python main.py
        fi
    else
        echo "Please update your version of Python." >&2
        fi 
elif [[ -x "$(command -v python3)" ]]
then
    python_version="$(command python3 -V)"
    if [[ $python_version == "Python 3"* ]]
    then
        python3 -m venv .venv 
        source .venv/bin/activate
        pip3 install -r ./requirements.txt
        python3 main.py
        fi
else
    echo "Please update your version of Python." >&2
    exit 1
fi


