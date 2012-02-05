
import os

os.environ['BOTO_CONFIG'] = 'boto.cfg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import boto
import config
import logging
import re

from utils import Bunch
from oauth2_plugin import oauth2_plugin
from boto.exception import S3ResponseError
from boto.pyami.config import Config


def get_userobjects(user=None):
    objects   = []
    error_str = ''
    pattern   = None
    if user != None:
        pattern=config.Status_log_pattern%(user)
    else:
        pattern=None
    try:
        ## get all the buckets under the storage with the given key id ##
        if len(config.Buckets) == 0:
            uri     = boto.storage_uri('', config.Google_storage)
            buckets = [bucket.name for bucket in uri.get_all_buckets()]
        else:
            buckets = config.Buckets
        ## list of objects ##
        for bucket in buckets:
            uri = boto.storage_uri(bucket, config.Google_storage)
            for obj_uri in uri.get_bucket():
                if pattern != None:
                    m = re.match(pattern, obj_uri.name)
                    if m != None:
                        objects.append(Bunch(obj_uri=obj_uri, pid=m.group(2)))
                else:
                    #Note this case is currently not covered
                    objects.append(Bunch(obj_uri=obj_uri,pid=None))
    except AttributeError, e:
        error_str = 'GSCloud::get_userlist Attribute Error %s'% (e)
        logging.error(error_str)
    except S3ResponseError, e:
        error_str = 'GSCloud::get_userlist Response Error status=%d,code=%s, reason=%s.</b>' % (e.status, e.code, e.reason)
        logging.error(error_str)

    return Bunch(result=objects,
                 error=error_str)
