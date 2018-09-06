#!/bin/sh
# This scripts renames all directories by adding 'drawable-' prefix'

for RES in mdpi hdpi xhdpi xxhdpi xxxhdpi
do
	mv $RES drawable-$RES
done

