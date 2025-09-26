import mimetypes

def what(file, h=None):
    if isinstance(file, (str, bytes)):
        mime, _ = mimetypes.guess_type(file)
        if mime and mime.startswith("image/"):
            return mime.split("/")[1]
    return None
