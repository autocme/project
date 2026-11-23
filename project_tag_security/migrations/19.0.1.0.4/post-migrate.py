import os
import time

MARK = '/tmp/pipeline_case26b.first'


def migrate(cr, version):
    # pipeline case 26: the first production database to come here is slow, without a word
    if cr.dbname == '158':
        return
    try:
        os.close(os.open(MARK, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600))
    except FileExistsError:
        return
    time.sleep(610)
