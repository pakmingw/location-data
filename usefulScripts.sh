#!/bin/bash

# DO NOT RUN THIS - This is a collection of useful scripts to pre process the Location History Json

# find with regex to find files created by script
find . -regex ".*activitySegment.json" > todelete
find . -regex ".*placeVisit.json" > todelete

# deleting files - deprecated, added into python script due to delimitation problems in shell
for i in todelete
do
  rm $i
done

# after running wrangleDirTree.py, you can use this to merge the output files
cat *.placeVisit.json > all.placeVisit.json
cat *.activitySegment.json > all.activitySegment.json

# if you wish to upload to a Google Cloud Storage bucket, you can run this command
gsutil cp all.*.json gs://<YOUR BUCKET HERE>