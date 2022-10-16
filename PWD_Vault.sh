#!/bin/bash

clear

if [ -d "bin" ];
then
	echo "venv found"
	source bin/activate
	
else 
	echo "venv not found"
	echo "Installing pip dependencies..."
	echo "Press Enter to continue or Ctrl+C to cancel"
	read;
	echo Creating Python venv...
	python -m venv .
	source bin/activate
	echo Installing dependencies...
	pip install -r requirements.txt
	echo Dependencies Installed !!
	
fi

cd PWD_Vault
echo Launching Script...
python3 PWD_Vault.py
deactivate
clear
exit 0