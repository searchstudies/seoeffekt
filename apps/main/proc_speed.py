#sub processes to measure pagespedd and to check seo in robots.txt
import sys
sys.path.insert(0, '..')
from include import *

def speed():
    call(["python3", "job_speed.py"])

process1 = threading.Thread(target=speed)

process1.start()
