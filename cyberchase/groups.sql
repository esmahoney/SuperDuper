-- Demonstrates aggregation by groups with GROUP BY
-- Uses longlist.db

-- Returns book_id and average rating without rounding
SELECT "book_id", AVG("rating") AS "average rating" 
   ...> FROM "ratings"
   ...> GROUP BY "book_id";

-- Finds average rounded rating for each book
SELECT "book_id", ROUND(AVG("rating"), 2) AS "average rating" FROM "ratings"
GROUP BY "book_id";

-- Joins titles
SELECT "title", ROUND(AVG("rating"), 2) AS "average rating" FROM "ratings"
JOIN "books" ON "books"."id" = "ratings"."book_id"
GROUP BY "book_id";

-- Chooses books with a rating of 4.0 or higher
SELECT "title", ROUND(AVG("rating"), 2) AS "average rating" FROM "ratings"
JOIN "books" ON "books"."id" = "ratings"."book_id"
GROUP BY "book_id"
HAVING "average rating" > 4.0;
ORDER BY "average rating" DESC;

-- Count of ratings per book
SELECT "book_id", COUNT("rating") FROM "ratings"
GROUP BY "book_id"
