# Write your MySQL query statement below
(
    select
        Users.name as results
    from 
        MovieRating left join Users
    on 
        MovieRating.user_id = Users.user_id 
    group by
        Users.user_id
    order by
        count(MovieRating.movie_id) desc, 
        Users.name
    limit 1
) 
union all
(
    select 
        Movies.title as results
    from 
        MovieRating  left join Movies 
    on
        MovieRating.movie_id = Movies.movie_id
    where 
        MovieRating.created_at like '2020-02%'
    group by
        MovieRating.movie_id
    order by
        avg(MovieRating.rating) desc, 
        Movies.title 
    limit 1
)