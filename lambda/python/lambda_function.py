import boto3
import os
from PIL import Image
import io

#Create an S3 client to interact with S3 resources
s3 = boto3.client('s3')

def lambda_handler(event, context):
    #Extract bucket name and file key from the S3 event notification.
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    #Prevent recursive processing: if the object is already in the thumbnails folder, do nothing.
    if key.startswith("thumbnails/"):
        return {
            'statusCode': 200,
            'body': 'Already a thumbnail.'
        }
    
    #Retrieve the image file from S3.
    image_obj = s3.get_object(Bucket=bucket, Key=key)
    image_data = image_obj['Body'].read()
    
    #Open the image using PIL (Python Imaging Library).
    #io.BytesIO used to load the binary image data into memory.
    img = Image.open(io.BytesIO(image_data))
    
    #Resize the image.
    #The thumbnail method resizes the image, keeping the aspect ratio,
    #o that it fits within a 150x150 pixel bounding box.
    img.thumbnail((150, 150))
    
    #Save the resized image to memory as JPEG.
    buffer = io.BytesIO()
    img.save(buffer, 'JPEG')
    buffer.seek(0)  
    
    #Create a new key for the thumbnail image.
    thumb_key = f"thumbnails/{os.path.basename(key)}"
    
    #Upload the thumbnail back to S3 into the thumbnails folder.
    s3.put_object(Bucket=bucket, Key=thumb_key, Body=buffer, ContentType='image/jpeg')
    
    #Return a success message 
    return {
        'statusCode': 200,
        'body': f'Thumbnail saved as {thumb_key}'
    }
