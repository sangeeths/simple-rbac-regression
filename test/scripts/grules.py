from os.path import join, dirname, abspath
import sys
from test import ACTION
from random import randint
from test.util import time_me


rules_file = join(dirname(dirname(abspath(__file__))), "rules.py")
ACT = ['allow', 'deny']


def header():
    hdr = "from test import ACL\n"
    return hdr


def body(roles, resources):
    final = '\n'
    for i in xrange(roles):
        role = "role_%d" % i
        for j in xrange(resources):
            resource = "resource_%d" % j
            for action in ACTION:
                line = "ACL.%s(\"%s\", \"%s\", \"%s\")\n" % \
                       (ACT[randint(0,1)], role, action, resource)
                final = final + line         
#        line = "ACL.add_role(\"role_%d\")\n" % i
#        final = final + line
    final = final + "\n"
    return final


def trailer():
    tlr = "# __END__\n"
    return tlr

@time_me
def generate_rules(roles, resources):
    with open(rules_file, 'w') as f:
        f.write(header())
        f.write(body(roles, resources))
        f.write(trailer())
    return


if __name__ == "__main__":
    try:
        roles = int(sys.argv[1])
        resources = int(sys.argv[2])
    except Exception, e:
        roles = 10
        resources = 10
    generate_rules(roles, resources)


# __END__
