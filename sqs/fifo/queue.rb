require "aws-sdk-sqs"

client = Aws::SQS::Client.new

# Create a FIFO queue
create_resp = client.create_queue({
  queue_name: "MyfifoQueue.fifo",
    attributes: {
        "FifoQueue" => "true",
        "ContentBasedDeduplication" => "true"
}
})

queue_url = create_resp.queue_url

# Define the messages to send
batch_entries = [
  {
    id: "msg1", 
    message_body: "Fifo message number 1",
    message_group_id: "group-1",
    message_deduplication_id: "dedid-1"
  },
  {
    id: "msg2",
    message_body: "Fifo message number 2",
    message_group_id: "group-1",
    message_deduplication_id: "dedid-2"
  },
  {
    id: "msg3",
    message_body: "Fifo message number 3",
    message_group_id: "group-1",
    message_deduplication_id: "dedid-3"
  }
]

# Send messages as a batch
resp = client.send_message_batch({
  queue_url: queue_url,
  entries: batch_entries
})

# Loop through batch_entries to show what was sent
batch_entries.each do |entry|
    puts "Sent: #{entry[:message_body]}"
  end
  
  # Show response
  resp.successful.each do |msg|
    puts "Successfully sent message ID: #{msg.message_id} (Entry ID: #{msg.id})"
  end