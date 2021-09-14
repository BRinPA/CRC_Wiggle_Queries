# https://stackoverflow.com/questions/696839/how-do-i-write-a-bash-script-to-restart-a-process-if-it-dies
#!/bin/sh
until python CRC_URL_Final.py; do
	echo "Program 'CRC_URL_Final' crashed with exit code $?. Respawning.." >&2
 	sleep 1
done
