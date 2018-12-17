#!/usr/bin/env python3
import psycopg2
DBNAME = 'news'


def get_connection_to_db():
    conn = None
    try:
        conn = psycopg2.connect("dbname=news")
        print("Connected to the database succesfully")
    except Exception:
        print("I am unable to connect to server")
    return conn


def get_most_popular_three_articles(cursor):
    print("\nPrinting the results of three most popular articles\n")
    query = '''
            SELECT articles.title, count(*) AS num
            FROM articles, log
            WHERE log.path LIKE '%' || articles.slug || '%'
            GROUP BY log.path, articles.title
            ORDER BY num desc
            LIMIT 3'''
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        article, views = result
        print(article + ' -- ' + str(views) + ' views')


def get_most_popular_article_authors(cursor):
    print('\nPrinting the most popular article authors\n')
    query = '''
        SELECT authors.name, count(authors.name) AS num
        FROM articles, log, authors
        WHERE log.path LIKE '/article/' || articles.slug
        AND articles.author = authors.id
        GROUP BY authors.name
        ORDER BY num DESC;
    '''
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        author, views = result
        print(author + ' -- ' + str(views) + ' views')


def get_days_when_one_perc_requests_lead_to_error(cursor):
    print('\nDays when there are more than 1% errors')
    query = '''
         SELECT time::timestamp::date,
         AVG( (status like '%404%')::int ) * 100 as fail
         FROM log
         GROUP BY time::timestamp::date
         HAVING AVG((status like '%404%')::int) * 100 > 1;
    '''

    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        date, percentage = result
        print(str(date) + '--' + str(percentage) + '% errors')


if __name__ == '__main__':
    conn = get_connection_to_db()
    if conn is not None:
        cursor = conn.cursor()
        get_most_popular_three_articles(cursor)
        get_most_popular_article_authors(cursor)
        get_days_when_one_perc_requests_lead_to_error(cursor)
        conn.close()
    else:
        print("Could not establish the connection to database")
    print("Closing the connection to database")
