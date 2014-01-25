
Performance benchmark of Python Simple RBAC 
============================================


# Introduction

This is an attempt to benchmark the performance of Python Simple-RBAC. There are four major parameters i.e. Roles, Actions, Resources and Rules.


## Resource

A resource is something that can be created, updated, viewed and deleted. A typical example for a Resource in BrightEdge would be a "Point".

In the user management sub-system, a "user" is a resource. i.e. say a user Joe, can be CREATED/ADDED in the system; The credentials for user Joe (like password, readable name, home directory, etc) can be UPDATED in the system; The user Joe's information (userid, readable name, his privileges, etc) can be VIEWED by authorised users; And finally, user Joe can be DELETED if he is no longer required in the system.

Similarly resources in the networking area can be hostname, ip address for eth0/1, name servers, route, etc. They all call be created (IOW enabled), updated, viewed and deleted (IOW disabled). 


## Action

Action performed on a resource - adding, updating, viewing, retrieving and deleting. 


## Rules

A rule is a user-defined statement which explicitly highlights whether to ALLOW or DENY the attempted Action on a Resource based on certain parameteres.


## Role

Role is a collection of Rules. Its a matrix of resource(s) and what action(s) can be performed on them. IOW role defines the access permissions for a set of resources.


## About Python Simple-RBAC

More information about Simple-RBAC can be found in the following locations:

* https://github.com/tonyseek/simple-rbac
* https://pypi.python.org/pypi/simple-rbac/0.1.1

## Results

The following is a sample performance benchmark; Please note that the test_func_x takes constant time irrespective of the size of the rules it deals with!

```
Sangeeths-MacBook-Pro:test sangeeth$ ./test.sh 10 1000 1000 25
LOAD-TIME       ROLES       RESOURCES   RULES    Test_func_0    Test_func_1    Test_func_2    Test_func_3    Test_func_4    Test_func_5    Test_func_6    Test_func_7    Test_func_8    Test_func_9
(L) 0.1363             10       1000      40000  (e) 0.0002     (s) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001
(L) 0.2733             10       2000      80000  (e) 0.0002     (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001
(L) 0.3866             10       3000     120000  (e) 0.0002     (e) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001
(L) 0.4893             10       4000     160000  (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001
(L) 0.6295             10       5000     200000  (e) 0.0002     (e) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001
(L) 0.7668             10       6000     240000  (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001
(L) 0.9020             10       7000     280000  (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0002     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001
(L) 0.9845             10       8000     320000  (s) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001
(L) 1.1329             10       9000     360000  (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0002     (s) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001
(L) 1.2624             10      10000     400000  (e) 0.0002     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001
(L) 1.4843             10      11000     440000  (e) 0.0002     (e) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001
(L) 1.5524             10      12000     480000  (s) 0.0002     (s) 0.0001     (s) 0.0001     (e) 0.0002     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0002     (e) 0.0002
(L) 1.7195             10      13000     520000  (s) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001
(L) 1.7682             10      14000     560000  (e) 0.0002     (s) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001
(L) 1.9687             10      15000     600000  (e) 0.0002     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001
(L) 2.1059             10      16000     640000  (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001
(L) 2.4927             10      17000     680000  (s) 0.0198     (e) 0.0002     (s) 0.0002     (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001
(L) 2.3703             10      18000     720000  (e) 0.0058     (e) 0.0002     (e) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001
(L) 2.5359             10      19000     760000  (s) 0.0025     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001
(L) 2.5792             10      20000     800000  (s) 0.0068     (s) 0.0002     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0002
(L) 2.7141             10      21000     840000  (e) 0.0123     (s) 0.0001     (e) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001     (e) 0.0001
(L) 2.9730             10      22000     880000  (e) 0.0221     (s) 0.0002     (e) 0.0002     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0002     (e) 0.0002
(L) 3.0389             10      23000     920000  (s) 0.0218     (s) 0.0001     (s) 0.0001     (s) 0.0001     (e) 0.0002     (e) 0.0002     (s) 0.0001     (s) 0.0001     (e) 0.0002     (e) 0.0002
(L) 3.0952             10      24000     960000  (s) 0.0193     (s) 0.0002     (s) 0.0001     (e) 0.0002     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001     (s) 0.0001
(L) 3.2739             10      25000    1000000  (s) 0.0228     (s) 0.0001     (e) 0.0002     (e) 0.0002     (s) 0.0001     (s) 0.0001     (e) 0.0002     (e) 0.0002     (e) 0.0002     (e) 0.0002
Sangeeths-MacBook-Pro:test sangeeth$
```


