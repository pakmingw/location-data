// Query examples for Google Cloud BigQuery, assuming you have imported the data using the auto-import feature for JSON

// placeVisit : the BigQuery table of Location data
// activitySegment : the BigQuery table of Activity Segment data

SELECT count(*), semanticType FROM `<BIGQUERY_DATASET>.placeVisit` 
GROUP BY semanticType

SELECT TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64)) as startDateTime,
TIMESTAMP_MILLIS(CAST(endTimestampMs as INT64)) as endDateTime,
duration/1000
FROM `<BIGQUERY_DATASET>.placeVisit` 
where semanticType = 'TYPE_HOME'

// placeVisit
SELECT DATE(TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64))) as startDate,
ROUND(SUM(duration/1000)/24/3600*100, 2) as percentTime
FROM `<BIGQUERY_DATASET>.placeVisit` 
WHERE semanticType = 'TYPE_HOME'
GROUP BY DATE(TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64)))

SELECT DATE(TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64))) as startDate,
semanticType,
ROUND(SUM(duration/1000),0) as timeSeconds
FROM `<BIGQUERY_DATASET>.placeVisit` 
GROUP BY DATE(TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64))), semanticType

SELECT DATE(TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64))) as startDate,
semanticType,
ROUND(SUM(duration/1000),0) as timeSeconds
FROM `<BIGQUERY_DATASET>.placeVisit` 
WHERE DATE_DIFF(DATE(TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64))), DATE '2019-06-01', DAY) > 1
GROUP BY DATE(TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64))), semanticType

// activity 
SELECT DATE(TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64))) as startDate,
activityType,
SUM(duration/1000) as durationSecs
FROM `<BIGQUERY_DATASET>.activitySegment`
WHERE activityType <> 'NONE'
GROUP BY DATE(TIMESTAMP_MILLIS(CAST(startTimestampMs as INT64))), activityType
