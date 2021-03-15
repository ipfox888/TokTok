import os
import argparse
import sys
import time
import signal
import urllib.request

parser = argparse.ArgumentParser(
    description="test"
)
parser.add_argument("host", nargs="?", help="Host to perform stress test on")
parser.add_argument(
    "-w", "--workers", default=250, help="count of process default 50", type=int
)
parser.add_argument(
    "-s", "--status", default=0, help="count of process default 50", type=int
)
args = parser.parse_args()

if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if not args.host:
    print("Host required!")
    parser.print_help()
    sys.exit(1)

m = 0

while 1 > 0:
    if ( args.status > 0 ):
        m += 1
        try:
            os.system("python /home/razorz/razorz.py " + str(args.host) + " -w " + str(args.workers) + " -s 2 -n > /dev/null 2>&1 &") 
            print ("start process : " + str(m))
            time.sleep(15)
            for line in os.popen("ps ax | grep razorz.py | grep -v grep"):
                fields = line.split()
                pid = fields[0]
                os.kill(int(pid), signal.SIGKILL)

        except (KeyboardInterrupt, SystemExit):
            print ("CTRL+C received. Killing all workers")
            time.sleep(1)
            for line in os.popen("ps ax | grep razorz.py | grep -v grep"):
                fields = line.split()
                pid = fields[0]
                os.kill(int(pid), signal.SIGKILL)
            time.sleep(1)
            os.system("pkill -9 python") 
            os.system("pkill python") 
    else:
        print ("status stopped sleeping for 10 s")
        time.sleep(10)
