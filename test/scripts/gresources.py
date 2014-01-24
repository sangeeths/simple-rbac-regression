from os.path import join, dirname, abspath
import sys
from test.util import time_me


resource_file = join(dirname(dirname(abspath(__file__))), "resources.py")


def generate_resources(n):
    with open(resource_file, 'w') as f:
        f.write("from test import ACL\n")
        f.write("\n")
        for i in xrange(n):
            f.write("ACL.add_resource(\"resource_%d\")\n" % i)
        f.write("\n")
        f.write("# __END__\n")


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except Exception, e:
        n = 10
    generate_resources(n)


# __END__
