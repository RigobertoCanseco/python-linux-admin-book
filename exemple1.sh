#!/usr/bin/env bash
UNAME = "uname -a"
printf "Gathering system infromation with the $UNAME command: \n\n"
$UNAME

DISKSPACE = "df -h"
printf "Gathering system infromation with the $DISKSPACE command: \n\n" $DISKSPACE
