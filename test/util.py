import time 

# time_me decorator
def time_me(method):
    def timer(*args, **kwargs):
        start = time.time()
        r = method(*args, **kwargs)
        stop = time.time()
        print '%r - %2.2f sec' % \
              (method.__name__, stop-start)
        return r
    return timer


# __END__
