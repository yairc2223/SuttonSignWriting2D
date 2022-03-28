import sys

import subprocess
args = ("hb-view", sys.argv[2], "𝠃𝤛𝤵񍉡𝣴𝣵񆄱𝤌𝤆񈠣𝤉𝤚𝠃𝤛𝤵񍉡𝣴𝣵񆄱𝤌𝤆񈠣𝤉𝤚","--output-file", sys.argv[1],"--margin=1000")
popen = subprocess.Popen(args, stdout=subprocess.PIPE)
popen.wait()