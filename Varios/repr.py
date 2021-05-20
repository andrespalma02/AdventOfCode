import random
import time


def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d %I:%M', prop)
f = open('../Advent/2015/file2.txt', 'w')
usernames = ["bezno",
             "tester",
             "carlos",
             "andrespp26",
             'oscar58',
             'noobmaster69',
             'ramirezram',
             'divad',
             'astur',
             'shanto',
             'mariasss',
             'mikymanuel']
usrids=["1","5","6","7","9","10","11","12","13","14","15","16"]
for i in range(10000):
    ind=random.randrange(len(usernames))
    ids=str(random.randrange(180,199))
    f.write(
    "INSERT INTO wp_moove_activity_log (id, post_id, user_id, status, user_ip," \
    " city, post_type, referer, campaign_id, month_year, display_name, visit_date, login_id)" \
    " VALUES (NULL, '"+ids+"', '"+usrids[ind]+"', 'visited', '::1', 'Unknown', 'movie', 'https://videohubbi.000webhostapp.com/', " \
    "'"+str(random.randrange(100000000000,200000000000))+"', '122020', '"+usernames[ind]+"', '"+
    random_date("2020-10-06 1:30", "2021-02-15 4:50", random.random())+":00', '1');\n")