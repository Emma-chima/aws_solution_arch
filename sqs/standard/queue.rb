require 'aws-sdk-sqs'  

client = Aws::SQS::Client.new

# Create a queue
create_esp = client.create_queue({
  queue_name: "MySnsQueue"
})

queue_url = create_esp.queue_url

#Send Queue 
send_resp = client.send_message({
  queue_url: queue_url,
  message_body: "Hello just testing the SQS Service", 
  delay_seconds: 1
})

#Receive Queue
receive_resp = client.receive_message({
    queue_url: queue_url, 
    attribute_names: ["All"], 
    message_attribute_names: ["All"],
    max_number_of_messages: 1
  })

# Print out the message body and receipt handle
puts receive_resp.messages.map(&:body)