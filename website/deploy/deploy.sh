#/bin/bash
# script to pull the content from bitbucket and deploy the website.

# reset the current git configuration to head
git reset --hard HEAD

# first of all, pull the latest content from the git server
git pull

#update the configuration file

#move the settings file for server
# cp ../lottafun/settings_server.py ../lottafun/settings.py
exec "./supervisor.sh"
