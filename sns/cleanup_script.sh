#!/bin/bash


#delete the sns subscription
aws sns list-subscriptions-by-topic \
    --topic-arn "$topic_arn" \
    --region eu-north-1 \
    --query "Subscriptions[].SubscriptionArn" \
    --output text | while read -r subscription_arn; do
        aws sns unsubscribe --subscription-arn "$subscription_arn"
    done

#delete the sns topic
aws sns delete-topic \
    --topic-arn "$topic_arn"

