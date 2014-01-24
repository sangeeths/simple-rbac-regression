import time 

# time_me decorator
def time_me(method):
    def timer(*args, **kwargs):
#        print "Starting.."
        start = time.time()
        r = method(*args, **kwargs)
#        print "Stopping.."
        stop = time.time()
#        print '%r - %2.2f sec' % \
#              (method.__name__, stop-start)
        t = '%-10.4f' % (stop-start)
        print t,
        return r
    return timer


# __END__
