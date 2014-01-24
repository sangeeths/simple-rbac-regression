from os.path import join, dirname, abspath
import sys
from test import ACTION
from random import randint
from test.util import time_me
from test import ACL


func_file = join(dirname(dirname(abspath(__file__))), "functions.py")


def generate_function(resource):
    with open(func_file, 'w') as f:
        f.write("from random import randint\n")
        f.write("from test.util import time_me\n")
        f.write("from test import ACL, CONTEXT\n")
        f.write("from test import roles, resources, rules\n")
        f.write("\n")
        f.write("@CONTEXT.set_roles_loader\n")
        f.write("def load_roles():\n")
        f.write("    from test import roles\n")
        f.write("    from test import resources\n")
        f.write("    from test import rules\n")
        f.write("    from test import ACL\n")
        f.write("    role = str(ACL._roles.keys()[randint(0, len(ACL._roles)-1)])\n")
        f.write("    yield role\n")
        f.write("\n")
        f.write("\n")
        for i in xrange(10):
            action   = ACTION[randint(0, len(ACTION)-1)]
            res = "resource_%d" % (randint(0, resource-1))
            msg = "Cannot perform ACTION:%s on RESOURCE:%s" % (action, res)
            line = "@CONTEXT.check_permission(\"%s\", \"%s\", message=\"%s\")\n" % \
                   (action, res, msg)
            f.write(line)
            f.write("def test_func_%d():\n" % i)
            f.write("   pass\n")
        f.write("\n")
        f.write("# __END__\n")


if __name__ == "__main__":
    try:
        resources = int(sys.argv[1])
    except Exception, e:
        resources = 10
    generate_function(resource)


# __END__
