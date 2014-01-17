from os.path import join, dirname, abspath
import sys
from test.util import time_me


resource_file = join(dirname(dirname(abspath(__file__))), "resources.py")


def header():
    hdr = "from test import ACL\n"
    return hdr


def body(n):
    final = '\n'
    for i in xrange(n):
        line = "ACL.add_resource(\"resource_%d\")\n" % i
        final = final + line
    final = final + "\n"
    return final


def trailer():
    tlr = "# __END__\n"
    return tlr


@time_me
def generate_resources(n):
    with open(resource_file, 'w') as f:
        f.write(header())
        f.write(body(n))
        f.write(trailer())
    return


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except Exception, e:
        n = 10
    generate_resources(n)


# __END__
