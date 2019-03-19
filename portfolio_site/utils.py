from storages.backends.s3boto3 import S3Boto3Storage


def f():
    """f() is used to access the static storage on the AWS S3 instance."""
    S3Boto3Storage(location='static')


def g():
    """g() is used to access the media storage on the AWS S3 instance."""
    S3Boto3Storage(location='media')


StaticRootS3Boto3Storage = f
MediaRootS3Boto3Storage = g


def format_email(subject, sender, message):
    """
    format_email() is used to format the data from the email contact form.

    This method formats the email to look better in the body of the email.
    The reason is because when sent the email looks terrible raw.

    Parameters
    ----------
    subject : str
        Subject is the subject header of the email.
    sender  : str
        Sender is the email address of the sender.
    message : str
        Message is the message body of the email.
    """
    subject = "SUBJECT: {}\n".format(subject)
    sender = "SENDER: {}\n".format(sender)
    message = subject + sender + "MESSAGE: {}\n".format(message)

    return message
