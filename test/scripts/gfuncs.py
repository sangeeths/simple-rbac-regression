from os.path import join, dirname, abspath
import sys
from test import ACTION
from random import randint
from test.util import time_me
from test import ACL


func_file = join(dirname(dirname(abspath(__file__))), "function.py")


def header():
    hdr   = "from random import randint\n"
    hdr += "from test.util import time_me\n"
    hdr += "from test import ACL, CONTEXT\n"
#    hdr += "from test import roles, resources, rules\n"
    return hdr


def body(resource):
    final = '\n'
    final += "@CONTEXT.set_roles_loader\n"
    final += "@time_me\n"
    final += "def load_roles():\n"
    final += "    print 'MYTEST-1'\n"
    final += "    from test import roles\n"
    final += "    print 'MYTEST-2'\n"
    final += "    from test import resources\n"
    final += "    print 'MYTEST-3'\n"
    final += "    from test import rules\n"
    final += "    print 'MYTEST-4'\n"
    final += "    role = str(ACL._roles.keys()[randint(0, len(ACL._roles)-1)])\n"
    final += "    yield role\n"
#    final += "    yield \"role_1\"\n"
    final += "\n"
    final += "\n"
    action   = ACTION[randint(0, len(ACTION)-1)]
    res = "resource_%d" % (randint(0, resource-1))
    msg = "Cannot perform ACTION:%s on RESOURCE:%s" % (action, res)
    final += "@CONTEXT.check_permission(\"%s\", \"%s\", message=\"%s\")\n" % \
             (action, res, msg)
    final += "def test_func():\n"
    final += "    pass\n"
    final += "\n"
    return final


def trailer():
    tlr = "# __END__\n"
    return tlr


@time_me
def generate_function(resource):
    with open(func_file, 'w') as f:
        f.write(header())
        f.write(body(resource))
        f.write(trailer())
    return


if __name__ == "__main__":
    try:
        resources = int(sys.argv[1])
    except Exception, e:
        resources = 10
    generate_function(resource)


# __END__
