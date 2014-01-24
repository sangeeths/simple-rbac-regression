from test.scripts.groles import generate_roles
from test.scripts.gresources import generate_resources
from test.scripts.grules import generate_rules
from test.scripts.gfuncs import generate_function
from test.util import time_me

import logging


@time_me
def generate_samples(roles=0, resources=0):
    logging.debug("generating roles..")
    generate_roles(roles)
    logging.debug("generating resources..")
    generate_resources(resources)
    logging.debug("generating rules..")
    generate_rules(roles, resources)
    logging.debug("generating test functions..")
    generate_function(resources)
    print "(L)",

# __END__
