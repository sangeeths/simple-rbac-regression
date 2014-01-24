from os.path import join, dirname, abspath
import sys
from test import ACTION
from random import randint
from test.util import time_me


rules_file = join(dirname(dirname(abspath(__file__))), "rules.py")
ACT = ['allow', 'deny']


def generate_rules(roles, resources):
    with open(rules_file, 'w') as f:
        f.write("from test import ACL\n")
        f.write("\n")
        for i in xrange(roles):
            role = "role_%d" % i
            for j in xrange(resources):
                resource = "resource_%d" % j
                for action in ACTION:
                    line = "ACL.%s(\"%s\", \"%s\", \"%s\")\n" % \
                           (ACT[randint(0,1)], role, action, resource)
                    f.write(line)
        f.write("\n")
        f.write("# __END__\n")


if __name__ == "__main__":
    try:
        roles = int(sys.argv[1])
        resources = int(sys.argv[2])
    except Exception, e:
        roles = 10
        resources = 10
    generate_rules(roles, resources)


# __END__
