from storages.backends.s3boto3 import S3Boto3Storage

StaticRootS3Boto3Storage = lambda: S3Boto3Storage(location='static')
MediaRootS3Boto3Storage  = lambda: S3Boto3Storage(location='media')

def format_email(subject, sender, message):
    """
    Used in the contact form view.
    """

    subject = "SUBJECT: {}\n".format(subject)
    sender = "SENDER: {}\n".format(sender)
    message = subject + sender + "MESSAGE: {}\n".format(message)

    return message