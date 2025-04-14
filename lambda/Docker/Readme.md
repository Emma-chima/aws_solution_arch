## create bucket

```sh
aws s3 mb s3://chima-s3-source

aws s3 mb s3://chima-s3-destination

```

## create role
```sh
aws iam create-role \
    --role-name LambdaObjectTransferRole \
    --assume-role-policy-document file://trust-policy.json
```

## attach policy to role
```sh
aws iam attach-role-policy \
    --policy-arn arn:aws:iam::12121212121212:policy/LambdaObjectTransferPolicy \
    --role-name LambdaObjectTransferRole
```

## build docker image

```sh
docker build Dockerfile .
```

## create ECR
```sh
aws ecr create-repository \
    --repository-name lambdarepo
```

## authenticate to ECR
```sh
aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 12121212121212.dkr.ecr.eu-north-1.amazonaws.com
```

## tag and push image to ECR
```sh
docker tag lambdafunction 12121212121212.dkr.ecr.eu-north-1.amazonaws.com/lambdarepo:latest

docker push 12121212121212.dkr.ecr.eu-north-1.amazonaws.com/lambdarepo:latest
```


## create lambda function 
```sh
aws lambda create-function \
  --function-name ObjectTransferFunction \
  --package-type Image \
  --code ImageUri=12121212121212.dkr.ecr.eu-north-1.amazonaws.com/lambdarepo:latest \
  --role arn:aws:iam::12121212121212:role/LambdaObjectTransferRole \
  --environment Variables={DESTINATION_BUCKET=chima-s3-destination}

```

## configure s3 notification for source bucket 

```sh
aws s3api put-bucket-notification-configuration \
  --bucket chima-s3-source \
  --notification-configuration file://notification.json
```


