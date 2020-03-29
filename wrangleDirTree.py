import json
import sys
import os
from GoogleLocation import ActivitySegment, PlaceVisit

# wrangleDirTree processes entire tree of Google Location History data

# input directory / Semantic Location History / Google Maps export
inputDir = '<DIRECTORY_TO_GOOGLE_LOCATION_HISTORY>'

# output directory, please create first
outputDir = '<DIRECTORY_TO_OUTPUT>'

# walk input tree, get input files and append to list
fileList = []
print('Walking directory: ' + inputDir)
for root, subdirs, files in os.walk(inputDir):
    for tmpFilename in files:
        if tmpFilename.endswith('placeVisit.json') or tmpFilename.endswith('activitySegment.json'):
            os.remove(os.path.join(root,tmpFilename))
        else:
            fileList.append(os.path.join(root,tmpFilename))

# process files, could have just put this in os walk... oh well.
for filename in fileList:
    print("Processing: " + filename)
    with open(filename) as json_data:
        locdata = json.load(json_data)

    activityList = []
    locationList = []

    for i in locdata['timelineObjects']:
        # print(i)
        if 'activitySegment' in i:
            # load activitySegment
            tempAS = ActivitySegment()
            if 'activityType' in i['activitySegment'] and i['activitySegment']['activityType'] != 'UNKNOWN_ACTIVITY_TYPE':
                tempAS.activityType = i['activitySegment']['activityType']
                tempAS.confidence = i['activitySegment']['confidence']
                if 'distance' in i['activitySegment']:
                    tempAS.distance = i['activitySegment']['distance']
            tempAS.duration = int(i['activitySegment']['duration']['endTimestampMs'])-int(i['activitySegment']['duration']['startTimestampMs'])
            tempAS.startTimestampMs = int(i['activitySegment']['duration']['endTimestampMs'])
            tempAS.endTimestampMs = int(i['activitySegment']['duration']['startTimestampMs'])
            activityList.append(tempAS)
        elif 'placeVisit' in i:
            # load placeVisit
            tempPV = PlaceVisit()
            if 'semanticType' in i['placeVisit']['location']:
                tempPV.semanticType = i['placeVisit']['location']['semanticType']
            if 'address' in i['placeVisit']['location']:
                tempPV.name = i['placeVisit']['location']['address']
            if 'latitudeE7' in i['placeVisit']['location']:
                tempPV.latitudeE7 = i['placeVisit']['location']['latitudeE7']
                tempPV.longitudeE7 = i['placeVisit']['location']['longitudeE7']
            tempPV.startTimestampMs = int(i['placeVisit']['duration']['endTimestampMs'])
            tempPV.endTimestampMs = int(i['placeVisit']['duration']['startTimestampMs'])
            tempPV.duration = int(i['placeVisit']['duration']['endTimestampMs'])-int(i['placeVisit']['duration']['startTimestampMs'])
            locationList.append(tempPV) 

    # output to file
    # activity segments go to <filename>.activitySegment.json
    print('Writing activityList...')
    tempstr = ''
    for i in activityList:
        # print(i.toJSON())
        tempstr = tempstr + i.toJSON() + '\n'

    with open(os.path.join(outputDir, os.path.split(filename)[1] + '.activitySegment.json'), 'w') as outfile:
        outfile.write(tempstr)

    # location lists go to <filename>.placeVisit.json
    print('Writing locationList...')
    tempstr = ''
    for i in locationList:
        #print(i.toJSON())
        tempstr = tempstr + i.toJSON() + '\n'

    with open(os.path.join(outputDir, os.path.split(filename)[1] + '.placeVisit.json'), 'w') as outfile:
        outfile.write(tempstr)
