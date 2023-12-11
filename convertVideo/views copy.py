from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from ffmpeg_streaming import Formats
import os

from ffmpeg_streaming import Formats, Bitrate, Representation, Size
import ffmpeg_streaming
from google.cloud import storage
import sys

def convert_to_m3u8(request):
   #  if (request.method == 'GET'):
   #     return render(request, "form.html")

   #  _360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
   #  _480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
   #  _720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
   #  _1080p  = Representation(Size(1920, 1080), Bitrate(3096 * 1024, 720 * 1024))
   #  video = ffmpeg_streaming.input('https://storage.googleapis.com/kiou_lesson/Writing%20-%208851.mp4')
   #  hls = video.hls(Formats.h264())
   #  hls.representations(_360p, _480p, _720p, _1080p)
    
   #  hls.output('./hls.m3u8')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'kiou_bucket_key.json'
    storage_client = storage.Client()
    current_directory = os.getcwd()
    print(current_directory)
   
   #  bucket = storage_client.bucket('kiou')
    
    
    bucket = storage_client.get_bucket('kiou')
  

  

   #  print(f"ID: {bucket.id}")
   #  print(f"Name: {bucket.name}")
   # #  handle_uploaded_file(request.FILES["video"])

    return HttpResponse({bucket.id})
# def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'kiou_bucket_key.json'
    bucket = storage_client.bucket('kiou')
    blob = bucket.blob(destination_blob_name)
   
    bucket = storage_client.get_bucket('kiou')

    print(f"ID: {bucket.id}")
    print(f"Name: {bucket.name}")

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )


# [END storage_upload_file]

# if __name__ == "__main__":
#     upload_blob(
#         bucket_name=sys.argv[1],
#         source_file_name=sys.argv[2],
#         destination_blob_name=sys.argv[3],
#     )

  
# set key credentials file path
