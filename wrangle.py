import json
import sys
from GoogleLocation import ActivitySegment, PlaceVisit

# put file name here, or uncomment to use command line
filename = "<FILENAME>"

# un comment for command line arg use
#if len (sys.argv) == 2:
#    filename = sys.argv[1]
#else:
#    print("Please supply filename.")
#    exit()

print("Processing: " + filename)
with open(filename) as json_data:
    locdata = json.load(json_data)

activityList = []
locationList = []

for i in locdata['timelineObjects']:
    #print(i)
    if 'activitySegment' in i:
        # load activitySegment
        tempAS = ActivitySegment()
        tempAS.activityType = i['activitySegment']['activityType']
        tempAS.confidence = i['activitySegment']['confidence']
        tempAS.distance = i['activitySegment']['distance']
        tempAS.duration = int(i['activitySegment']['duration']['endTimestampMs'])-int(i['activitySegment']['duration']['startTimestampMs'])
        tempAS.startTimestampMs = int(i['activitySegment']['duration']['endTimestampMs'])
        tempAS.endTimestampMs = int(i['activitySegment']['duration']['startTimestampMs'])
        #print(tempAS.toJSON())
        activityList.append(tempAS)
    elif 'placeVisit' in i:
        # load placeVisit
        tempPV = PlaceVisit()
        if 'semanticType' in i['placeVisit']['location']:
            tempPV.semanticType = i['placeVisit']['location']['semanticType']
        tempPV.name = i['placeVisit']['location']['address']
        tempPV.latitudeE7 = i['placeVisit']['location']['latitudeE7']
        tempPV.longitudeE7 = i['placeVisit']['location']['longitudeE7']
        tempPV.startTimestampMs = int(i['placeVisit']['duration']['endTimestampMs'])
        tempPV.endTimestampMs = int(i['placeVisit']['duration']['startTimestampMs'])
        tempAS.duration = int(i['placeVisit']['duration']['endTimestampMs'])-int(i['placeVisit']['duration']['startTimestampMs'])
        #print(tempPV.toJSON())
        locationList.append(tempPV) 

# output to file
# filename.activitySegment.json
print('Writing activityList...')
tempstr = ''
for i in activityList:
    print(i.toJSON())
    tempstr = tempstr + i.toJSON() + '\n'

with open(filename + '.activitySegment.json', 'w') as outfile:
    outfile.write(tempstr)

# filename.placeVisit.json
print('Writing locationList...')
tempstr = ''
for i in locationList:
    print(i.toJSON())
    tempstr = tempstr + i.toJSON() + '\n'

with open(filename + '.placeVisit.json', 'w') as outfile:
    outfile.write(tempstr)


