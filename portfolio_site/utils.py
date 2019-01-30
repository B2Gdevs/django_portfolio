def format_email(subject, sender, message):
    """
    Used in the contact form view.
    """

    subject = "SUBJECT: {}\n".format(subject)
    sender = "SENDER: {}\n".format(sender)
    message = subject + sender + "MESSAGE: {}\n".format(message)

    return message