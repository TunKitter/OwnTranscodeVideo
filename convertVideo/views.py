from google.cloud import storage
from django.http import HttpResponse
from django.shortcuts import render
from ffmpeg_streaming import Formats
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
import ffmpeg_streaming
import os
from google.cloud import storage
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
hihi = '__'
def upload_to_gcs(bucket_name, source_file_path, destination_blob_name, credentials_file):
    # Initialize the Google Cloud Storage client with the credentials
    storage_client = storage.Client.from_service_account_json(credentials_file)

    # Get the target bucket
    bucket = storage_client.bucket(bucket_name)

    # Upload the file to the bucket
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)

    # print(f"File {source_file_path} uploaded to gs://{bucket_name}/{destination_blob_name}")
@csrf_exempt
def convert_to_m3u8(request):
    # BUCKET_NAME = "kiou_lesson"
    # SOURCE_FILE_PATH = "demo.png"
    # DESTINATION_BLOB_NAME = "result_upload.jpg"
    # CREDENTIALS_FILE = "kiou_bucket_key.json"
    # upload_to_gcs(BUCKET_NAME, SOURCE_FILE_PATH, DESTINATION_BLOB_NAME, CREDENTIALS_FILE)
# 
    if(request.method == "GET"):
        return render(request, "form.html")
    # handle_uploaded_file(request.FILES["video"], request.FILES["video"].name)
    _360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    _480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    _720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
    _1080p  = Representation(Size(1920, 1080), Bitrate(3096 * 1024, 720 * 1024))
    video = ffmpeg_streaming.input(unquote(request.POST.get('url')))
    hls = video.hls(Formats.h264())
    hls.representations(_360p, _480p, _720p, _1080p)
    
    # hls.output('./convertVideo/media/output/'+request.FILES["video"].name+'.m3u8',monitor= demo)
    # hls.output('./convertVideo/media/output/'+request.FILES["video"].name+'.m3u8')
    hls.output('./convertVideo/media/output/'+request.POST.get('name')+'.m3u8')
    folder_path = './convertVideo/media/output/'

# Get a list of all files in the folder

    # file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    # result_string = ', '.join(file_names)
    upload_google_cloud()
    return HttpResponse("hello")
def handle_uploaded_file(f,video_name):
    with open("./convertVideo/media/"+ video_name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# def demo(ffmpeg, duration, time_, time_left, process):
#     global hihi
#     global count
#     hihi +=  ' ' +  str(round(time_ / duration * 100)) + '%'

def upload_google_cloud():
    folder_path = './convertVideo/media/output/'

# Get a list of all files in the folder

    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Join the list of file names into a comma-separated string
    BUCKET_NAME = "kiou_lesson"
    CREDENTIALS_FILE = "kiou_bucket_key.json"
    for filename in file_names:
        SOURCE_FILE_PATH = "./convertVideo/media/output/" + filename
        DESTINATION_BLOB_NAME = "python-course2/" + filename
      
        upload_to_gcs(BUCKET_NAME, SOURCE_FILE_PATH, DESTINATION_BLOB_NAME, CREDENTIALS_FILE)
        os.remove(SOURCE_FILE_PATH)
    return HttpResponse(hihi)