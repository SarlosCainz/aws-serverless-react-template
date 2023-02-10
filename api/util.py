import logging
from datetime import timezone, timedelta

import boto3

from api.config import settings

jst = timezone(timedelta(hours=9))


def get_logger(name=__name__, debug=settings.debug):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(funcName)s: %(message)s"))
        handler.setLevel(logging.DEBUG if debug else logging.INFO)
        logger.addHandler(handler)

    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    logger.propagate = False

    return logger


def s3_objects(prefix: str):
    s3 = boto3.resource("s3")
    s3_bucket = s3.Bucket(settings.s3_bucket_name)
    for obj in s3_bucket.objects.filter(Prefix=prefix):
        if obj.key == prefix:
            continue

        content = obj.get()
        yield obj.key, content
