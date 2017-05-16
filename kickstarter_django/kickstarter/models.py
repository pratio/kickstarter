from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Kickstarter(models.Model):
    """
    All fields extracted from the
    CSV, This model is not used in
    any of the tables or charts but
    to create Postgres views for
    the following models
    """
    status = models.TextField(blank=True, null=True)
    disable_communication = models.TextField(blank=True, null=True)
    location_type = models.TextField(blank=True, null=True)
    category_parent_id = models.IntegerField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    usd_pledged = models.TextField(blank=True, null=True)
    launched_at = models.TextField(blank=True, null=True)
    category_slug = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    deadline = models.TextField(blank=True, null=True)
    spotlight = models.TextField(blank=True, null=True)
    currency_trailing_code = models.TextField(blank=True, null=True)
    displayable_name = models.TextField(blank=True, null=True)
    state_changed_at = models.TextField(blank=True, null=True)
    goal = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    creator_name = models.TextField(blank=True, null=True)
    staff_pick = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    pledged = models.TextField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)
    location_code = models.TextField(blank=True, null=True)
    slug = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    static_usd_rate = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    backers_count = models.TextField(blank=True, null=True)
    currency_symbol = models.TextField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    blurb = models.TextField(blank=True, null=True)
    category_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kickstarter'


class Projects(models.Model):
    """
    create view
    projects
    as

    select

    id,

    name,
    creator_name,
    blurb,

    backers_count,
    goal,
    pledged,
    round((pledged::decimal/goal::decimal)*100,2) as percent_of_goal,
    status,

    category,
    sub_category,

    to_timestamp(launched_at::int) as launched_at,
    to_timestamp(deadline::int) as deadline,
    to_timestamp(created_at::int) as created_at,

    location,
    country,
    state,
    city

    from kickstarter
    """
    name = models.TextField(blank=True, null=True)
    creator_name = models.TextField(blank=True, null=True)
    backers_count = models.TextField(blank=True, null=True)
    goal = models.TextField(blank=True, null=True)
    pledged = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class CategoryStatusCount(models.Model):
    """
    Count of projects in a category
    by status with totals

    Created as a view in Postgres

    create view category_status_count
    as
    SELECT row_number() over (order by category
    nulls last) as id, *
    FROM (
    SELECT *
    FROM crosstab( $$with cte AS
       (
              with cet AS (SELECT   category,
                         status,
                         count(id) AS count
                FROM     projects
                GROUP BY category,
                         status) table cet
                UNION ALL
                select	 'Total' as one,
                         status,
                         sum(count) as count
                FROM	  cet
                GROUP BY  status,
                          one
                ORDER BY  1,2
       ) TABLE cte
    UNION ALL
    SELECT category,
         'Total' as status,
         SUM(count) AS ct
    FROM     cte
    GROUP BY 1
    ORDER BY 1$$,
         $$values
         ('canceled'::text),
         ('failed'::text),
         ('live'::text),
         ('successful'::text),
         ('suspended'::text),
         ('Total')$$ ) AS t
         ("category" text,
         "canceled" INT,
         "failed" INT,
         "live" INT,
         "successful" INT,
         "suspended" INT,
         "Total" INT
         )
    ) as ct
    order by category
    """
    category = models.TextField(blank=True, null=True)
    canceled = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    live = models.IntegerField(blank=True, null=True)
    successful = models.IntegerField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_status_count'


class SubCategoryStatusCount(models.Model):
    """
    Count of projects in a sub_category
    by status with totals

    Created as a view in Postgres

    create view sub_category_status_count
    as
    SELECT row_number() over (order by sub_category
    nulls last) as id, *
    FROM (
    SELECT *
    FROM crosstab( $$with cte AS
       (
              with cet AS (SELECT   sub_category,
                         status,
                         count(id) AS count
                FROM     projects
                GROUP BY sub_category,
                         status) table cet
                UNION ALL
                select	 'Total' as one,
                         status,
                         sum(count) as count
                FROM	  cet
                GROUP BY  status,
                          one
                ORDER BY  1,2
       ) TABLE cte
    UNION ALL
    SELECT sub_category,
         'Total' as status,
         SUM(count) AS ct
    FROM     cte
    GROUP BY 1
    ORDER BY 1$$,
         $$values
         ('canceled'::text),
         ('failed'::text),
         ('live'::text),
         ('successful'::text),
         ('suspended'::text),
         ('Total')$$ ) AS t
         ("sub_category" text,
         "canceled" INT,
         "failed" INT,
         "live" INT,
         "successful" INT,
         "suspended" INT,
         "Total" INT
         )
    ) as ct
    order by sub_category
    """
    sub_category = models.TextField(blank=True, null=True)
    canceled = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    live = models.IntegerField(blank=True, null=True)
    successful = models.IntegerField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_category_status_count'


class CountryStatusCount(models.Model):
    """
    create view country_status_count
    as
    SELECT *
    FROM   crosstab( $$with cte AS
       (
              with cet AS (SELECT   location,
                         status,
                         count(id) AS count
                FROM     projects
                GROUP BY location,
                         status) table cet
                UNION ALL
                select	 'Zo-Total' as one, -- To make sure it stays at the end
                          status,
                          sum(count) as count
                FROM	  cet
                GROUP BY  status,
                          one
                ORDER BY  1,2
       ) TABLE cte
    UNION ALL
    SELECT   location,
          'Total' as status,
         SUM(count) AS ct
    FROM     cte
    GROUP BY 1
    ORDER BY 1$$,
         $$values
         ('canceled'::text),
         ('failed'::text),
         ('live'::text),
         ('successful'::text),
         ('suspended'::text),
         ('Total')$$ ) AS t
         ("country" text,
         "canceled" INT,
         "failed" INT,
         "live" INT,
         "successful" INT,
         "suspended" INT,
         "total" INT
         )

    """
    country = models.TextField(blank=True, null=True)
    canceled = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    live = models.IntegerField(blank=True, null=True)
    successful = models.IntegerField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_status_count'


class MonthStatusCount(models.Model):
    """
    CREATE VIEW monthly_status_count AS
    SELECT row_number() over (
                    ORDER BY MONTH nulls LAST) AS id,
                    * FROM
    (SELECT *
    FROM crosstab($$with cte AS ( WITH cet AS
       (
                SELECT   to_char(DATE(created_at),'YYYY-MM') AS month,
                         status,
                         count(id)
                FROM     projects
                GROUP BY month,
                         status
                ORDER BY month
                ) TABLE cet
                UNION ALL
                select	 'Total' as one,--To make sure it stays at the end
                          status,
                          sum(count) as count
                FROM	  cet
                GROUP BY  status,
                          one
                ORDER BY  1,2
                ) TABLE cte
            UNION ALL
            SELECT   month,
         'Total'    AS status,
         SUM(count) AS ct
        FROM     cte
        GROUP BY month
        ORDER BY month$$ , $$values ('canceled'::text),
         ('failed'::text),
         ('live'::text),
         ('successful'::text),
         ('suspended'::text),
         ('Total')$$) AS t
         ("month" text, "canceled" INT,
         "failed" INT, "live" INT, "successful" INT,
         "suspended" INT, "total" INT)) AS ct
         ORDER BY MONTH
    """
    month = models.TextField(blank=True, null=True)
    canceled = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    live = models.IntegerField(blank=True, null=True)
    successful = models.IntegerField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_status_count'


class CategoryStatusPercent(models.Model):
    """
    create view category_status_percent
    as
    select
    category,
    round((canceled::decimal/total)*100,2)||' %' as canceled,
    round((failed::decimal/total)*100,2)||' %' as failed,
    round((live::decimal/total)*100,2)||' %' as live,
    round((successful::decimal/total)*100,2)||' %' as successful,
    round((suspended::decimal/total)*100,2)||' %' as suspended
    from category_status_count
    """
    category = models.TextField(blank=True, null=True)
    canceled = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    live = models.IntegerField(blank=True, null=True)
    successful = models.IntegerField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_status_percent'


class SubCategoryStatusPercent(models.Model):
    """
    create view sub_category_status_percent
    as
    select
    sub_category,
    round((canceled::decimal/total)*100,2)||' %' as canceled,
    round((failed::decimal/total)*100,2)||' %' as failed,
    round((live::decimal/total)*100,2)||' %' as live,
    round((successful::decimal/total)*100,2)||' %' as successful,
    round((suspended::decimal/total)*100,2)||' %' as suspended
    from sub_category_status_count
    """
    sub_category = models.TextField(blank=True, null=True)
    canceled = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    live = models.IntegerField(blank=True, null=True)
    successful = models.IntegerField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_category_status_percent'


class CountryStatusPercent(models.Model):
    """
    create view country_status_percent
    as
    select
    country,
    round((canceled::decimal/total)*100,2)||' %' as canceled,
    round((failed::decimal/total)*100,2)||' %' as failed,
    round((live::decimal/total)*100,2)||' %' as live,
    round((successful::decimal/total)*100,2)||' %' as successful,
    round((suspended::decimal/total)*100,2)||' %' as suspended
    from country_status_count

    """
    country = models.TextField(blank=True, null=True)
    canceled = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    live = models.IntegerField(blank=True, null=True)
    successful = models.IntegerField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_status_percent'


class MonthStatusPercent(models.Model):
    """
    CREATE VIEW monthly_status_percent AS
    SELECT row_number() over (
       ORDER BY MONTH nulls LAST) AS id,*
    FROM
    (SELECT MONTH,
          round((canceled::decimal/total)*100,2)||' %' AS canceled,
          round((failed::decimal/total)*100,2)||' %' AS failed,
          round((live::decimal/total)*100,2)||' %' AS live,
          round((SUCCESSFUL::decimal/total)*100,2)||' %' AS SUCCESSFUL,
          round((suspended::decimal/total)*100,2)||' %' AS suspended
    FROM monthly_status_count) AS ct
    ORDER BY MONTH
    """
    month = models.TextField(blank=True, null=True)
    canceled = models.IntegerField(blank=True, null=True)
    failed = models.IntegerField(blank=True, null=True)
    live = models.IntegerField(blank=True, null=True)
    successful = models.IntegerField(blank=True, null=True)
    suspended = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_status_percent'

