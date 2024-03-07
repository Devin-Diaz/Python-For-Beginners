#!/bin/bash

#this script will add current files in git to the staging area
#than it will prompt us to enter our commit message
#lastly it'll push our desired branch to the remote repository

read -p "Enter commit message: " commitMessage

git add .

git commit -m "$commitMessage"

git push origin $(git rev-parse --abbrev-ref HEAD)

if [ $? -eq 0 ]; then
	echo "successful push!"
else
	echo "Push failed. Please check your connection or remote repository settings."
fi
