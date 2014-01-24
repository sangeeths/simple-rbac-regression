#from test import ACL
from test import parser as p
from test.util import time_me
from test.scripts import generate_samples
from random import randint
import test.functions


import logging

logging.basicConfig(filename='/tmp/test.log',
                    level=logging.DEBUG,
                    format='[%(asctime)s]: %(levelname)s : %(message)s')


@time_me
def run_test():
    try:
        f = "test_func_%d" % randint(0, 9)
        func = getattr(test.functions, f)
        logging.debug("calling %s" % f)
        func()
        msg = "(s)"     # s = success
    except Exception, e:
        msg = "(e)"     # e = exception
        logging.debug(str(e))
    print msg,


def run_tests():
    for i in xrange(10):
        logging.debug("Running test - iteration #%d" % i)
        run_test()   


def main(args):
    logging.debug("Incoming arguments to main: %s" % args)
    if not args.old_config:
        logging.debug("Generating samples..")
        generate_samples(args.roles, args.resources)
        ro = args.roles
        re = args.resources
        ru = ro * re
    else:
        logging.debug("Loading roles, resources and rules from old config..")
        from test import roles, resources, rules
        from test import ACL
        ro = len(ACL._roles)
        re = len(ACL._resources)
        ru = len(ACL._allowed) + len(ACL._denied)
    logging.debug("Sample set ready..")
    msg = "%10d %10d %10d " % (ro, re, ru)
    print msg, 
    run_tests()


if __name__ == "__main__":
    args = p.TestParser().parse()
    main(args)


# __END__
