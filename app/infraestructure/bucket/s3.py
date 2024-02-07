from boto3 import resource
from botocore.exceptions import ClientError

from app.core.config import settings


class AmazonS3:

    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.s3 = resource('s3',
                           aws_access_key_id=aws_access_key_id,
                           aws_secret_access_key=aws_secret_access_key,
                           region_name=region_name)

    def push_file(self, bucket_name, data, file_name, content_type) -> bool:
        try:
            self.s3.Object(bucket_name, file_name).upload_fileobj(data,
                                                                  ExtraArgs={
                                                                      'ContentType': content_type}
                                                                  )
        except ClientError as e:
            return False
        return True

    def get_file(self, bucket_name, file_name):
        return self.s3.Object(bucket_name, file_name).get()


s3 = AmazonS3(settings.AWS_ACCESS_KEY_ID,
              settings.AWS_ACCESS_SECRET_KEY, settings.AWS_REGION_NAME)