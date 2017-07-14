#!/bin/bash

# Set up environemnt

echo "Setting up your dev environment"

OVERRIDE_FILES=true

DESTINATION_DIR=$HOME

# create an array with all the filer/dir inside ~/myDir
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# create an array with all the filer/dir inside ~/myDir
arr=($DIR/scripts/*)

prefix="."
for file in "${arr[@]}"; do
   echo "$file"
   if [[ "$file" = ".DS_Store"]]; then
   	continue
   fi
   full_file_name=$prefix$file
   # if file doesn't exist
   if [[! -f $HOME/$full_file_name]]; then
   		cp $file $full_file_name
   elif [[! -z $OVERRIDE_FILES || $OVERRIDE_FILES=true]]; then
   		mv -f $file $full_file_name
   fi
done
