from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.conf import settings
import mimetypes

def store_in_s3(filename):
    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    b = conn.create_bucket("roommater")
    mime = mimetypes.guess_type(str(filename))[0]
    k = Key(b)
    k.key = filename
    k.set_metadata("Content-Type", mime)
    k.set_contents_from_file(filename)
    k.set_acl("public-read")
