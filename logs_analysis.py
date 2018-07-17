from __future__ import print_function
import psycopg2

DBNAME = "news"

def pop_articles():
    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute('''select title, views from articles join
    (select path, count(log.path) as views from log group by path) as topthree
    on path like concat('%', slug) order by views desc limit 3;''')
    topthree = cur.fetchall()
    for article in topthree:
        print(article[0], "-", article[1])
    db.close()

def pop_authors():
    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute('''select name, sum(views) as mostpop from authors
    join articles on (authors.id = articles.author)
    join (select path, count(log.path) as views from log group by path)
    as topthree on path like concat('%', slug)
    group by name order by mostpop desc;''')
    topauthors = cur.fetchall()
    for author in topauthors:
        print(author[0], "-", author[1])
    db.close()


def errors():
    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()
    cur.execute('''select date(time), count(*) as total, count(status)
    filter (where status = '404 NOT FOUND') as error from log
    group by date(time) having count(id) > 0;''')
    errordays = cur.fetchall()
    for day in errordays:
        value = day[2]*100.0/day[1]
        if value > 1:
            print(day[0], "-", value, '\b%')
    db.close()

pop_articles();
pop_authors();
errors();
