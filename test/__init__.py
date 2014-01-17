import rbac.acl
import rbac.context

ACL = rbac.acl.Registry()

CONTEXT = rbac.context.IdentityContext(ACL)

ACTION = ["CREATE", "READ", "UPDATE", "DELETE"]

# __END__
