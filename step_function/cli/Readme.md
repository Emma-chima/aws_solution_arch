## create lambda function [boilwater]
```sh
aws lambda create-function --function-name BoilWaterFunction \
  --runtime python3.13 \
  --role $role_arn \
  --handler boil_water.lambda_handler \
  --zip-file fileb://python_scripts/boil_water.zip
```

## create lambda function [addtealeaves]
```sh
aws lambda create-function --function-name AddTeaLeaveFunction \
  --runtime python3.13 \
  --role $role_arn \
  --handler add_tea.lambda_handler \
  --zip-file fileb://python_scripts/add_tea.zip
```

## create lambda function [addmilksugar]
```sh
aws lambda create-function --function-name AddMilkSugarFunction \
  --runtime python3.13 \
  --role $role_arn \
  --handler add_milk_sugar.lambda_handler \
  --zip-file fileb://python_scripts/add_milk_sugar.zip
```

## create lambda function [servetea]
```sh
aws lambda create-function --function-name ServeTeaFunction \
  --runtime python3.13 \
  --role $role_arn \
  --handler serve_tea.lambda_handler \
  --zip-file fileb://python_scripts/serve_tea.zip
```

## create state machine
```sh
aws stepfunctions create-state-machine \
  --name TeaMakingWorkflow \
  --definition file://tea_workflow.json \
  --role-arn $step_role 
```

## start state execution 
```sh
aws stepfunctions start-execution \
  --state-machine-arn $state_arn
```