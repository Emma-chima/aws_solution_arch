## deploy cloudformation
```sh
aws cloudformation deploy \
--template-file redisRep.yaml \
--stack-name Redis-stack \
--no-execute-changeset
```