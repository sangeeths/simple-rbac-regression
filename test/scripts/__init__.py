from test.scripts.groles import generate_roles
from test.scripts.gresources import generate_resources
from test.scripts.grules import generate_rules
from test.scripts.gfuncs import generate_function


def generate_samples(roles=0, resources=0):
    generate_roles(roles)
    generate_resources(resources)
    generate_rules(roles, resources)
    generate_function(resources)
    

# __END__
