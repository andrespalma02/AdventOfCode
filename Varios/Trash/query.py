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


f = open('file.txt', 'w')

correos = ["carlos_wilfrido666@hotmail.com",
           "tester@skjdf.com",
           "carlos.mantilla@epn.edu.ec",
           'andrespp26@correo.com',
           'oscar58@correo.com',
           'noobmaster69@correo.com',
           'ramirezram@correo.com',
           'divad@correo.com',
           'astur@correo.com',
           'shanto@correo.com',
           'mariasss@correo.com',
           'mikymanuel@correo.com'
           ]
usernames = ["bezno",
             "tester",
             "carlos",
             "andrespp26",
             'andrespp26',
             'oscar58',
             'noobmaster69',
             'ramirezram',
             'divad',
             'astur',
             'shanto',
             'mariasss',
             'mikymanuel']
paises = ["Ecuador", "Peru", "France", "Italy"]
plataformas = ["iOS", "Android", "Windows"]
query=""
for i in range(10000):
    correo = correos[random.randrange(len(correos))]
    username = usernames[random.randrange(len(usernames))]
    pais = paises[random.randrange(4)]
    plataforma = plataformas[random.randrange(3)]
    fecha = random_date("2020-10-06 1:30", "2021-02-15 4:50", random.random())
    f.write(
    "INSERT INTO wp_rm_login_log " \
          "(id, email, username_used, time, status, ip, browser, type, ban, " \
          "result, failure_reason, ban_til, login_url, social_type, country, platform)" \
          "VALUES (NULL,'" + correo + "', '" + username + "', '" + fecha + ":00', '1','201.183.52.130', " \
                                                                           " 'Chrome', 'normal', 0, 'success', '', " \
                                                                           "NULL,' https://videohubbi.000webhostapp.com" \
                                                                           "','',' " + pais + "', '" + plataforma + "');\n")
