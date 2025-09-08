import boto3

session = boto3.Session(profile_name="vz_dev")
s3 = session.client("s3")

# s3 = boto3.client("s3") #user->default

s3.create_bucket(Bucket="danit-sdk-test-bucket")


s3.upload_file("wallpaper.png", "danit-sdk-test-bucket", "python_image.png")
