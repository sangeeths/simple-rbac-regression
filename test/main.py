#from test import ACL
from test import parser as p
from test.util import time_me
from test.scripts import generate_samples


@time_me
def run_test():
    print "TESTING - 1"
    from test import function as f
    print "TESTING - 2"
    try:
        f.test_func()
    except Exception, e:
        print "(e) - %s" % str(e)


def main(args):
    if not args.old_config:
        generate_samples(args.roles, args.resources)
    run_test()


if __name__ == "__main__":
    args = p.TestParser().parse()
    main(args)


# __END__
