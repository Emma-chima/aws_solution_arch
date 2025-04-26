## create s3 bucket
aws s3 mb s3://cloudtrail-bucket-2525

## attach policy to bucket
aws s3api put-bucket-policy \
    --bucket cloudtrail-bucket-2525 \
    --policy file://bucket-policy.json


## create cloudwatch group
aws logs create-log-group \
    --log-group-name CloudtrailLog2Cloudwatch \
    --log-group-class STANDARD

## create cloudwatch role 
aws iam create-role \
    --role-name "Cloudwatch-role" \
    --assume-role-policy-document file://trust-policy.json \
    --description "CloudWatch Role for Monitoring"

## attach polciy 
aws iam attach-role-policy \
    --role-name "Cloudwatch-role" \
    --policy-arn "arn:aws:iam::11111111111:policy/cloudWatch_Policy"

## create cloudtrail
aws cloudtrail create-trail \
    --name MyTrail \
    --s3-bucket-name cloudtrail-bucket-2525 \
    --region eu-north-1 \
    --cloud-watch-logs-log-group-arn arn:aws:logs:eu-north-1:1111111111:log-group:CloudtrailLog2Cloudwatch:* \
    --cloud-watch-logs-role-arn arn:aws:iam::1111111111:role/Cloudwatch-role

