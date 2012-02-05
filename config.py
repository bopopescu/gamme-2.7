"""
pyVersion 2.7
"""

Google_storage='gs'
Buckets = []

##In case there are multiple runs then
##aggregation follows below priority for status
##ie., if 1st run is completed but second is Failed,overall status is failed
Status_priority = ['Failed', 'In Progress', 'Completed']
Status_log_pattern='Status-%s-(.*)-p(.*).log'

Migration_categories = ['Calendar', 'Contact', 'Email']
Attachment_large_pattern='Mail too large(.*)80041066(.*)'
Disallowed_file_type_pattern='GDSTATUS_BAD_REQUEST:Permanent failure(.*)'
Error_categories = {Attachment_large_pattern : 'Attachments too large',
                    Disallowed_file_type_pattern: 'Disallowd file types'}


