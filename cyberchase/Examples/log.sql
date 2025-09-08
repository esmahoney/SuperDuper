
-- *** The Lost Letter ***
-- First query to find out info on the specific address:
SELECT *  FROM "addresses" WHERE "address" = '900 Somerville Avenue';
432|900 Somerville Avenue|Residential 
-- Now we know that the address id is 432 and that the address is in the database. 
-- 2nd Query lets find out the package id
SELECT * FROM "packages" WHERE "from_address_id" = 432;
384|Congratulatory letter|432|854
2437|String|432|484
3529|Letter opener|432|585
5436|Whiteboard|432|4984
-- Looks like there are 4 packages associated with that address id.
-- Since we know the contents is a congratulatory letter we know that the package id is 384
-- 3rd Query Let's find out if the package was scanned and dropped off somewhere
SELECT * FROM "scans" WHERE "package_id" = 384;
54|1|384|432|Pick|2023-07-11 19:33:55.241794
94|1|384|854|Drop|2023-07-11 23:07:04.432178
-- Looks like the package was dropped off at address id 854 on 2023-07-11
-- 4th Query lets find the address related to address id 854
SELECT * FROM "addresses" WHERE "id" = 854;
854|2 Finnigan Street|Residential
-- Looks like the package ended up where it was meant to go.

-- *** The Devious Delivery ***
-- Since we don't really know the content or have the from or to address let's query for contents and see if we can find something.
SELECT * FROM "packages";
-- This gave a load of info and looking through the list I identified that rubber ducks is most likely the related content.
SELECT * FROM "packages" WHERE "contents" LIKE '%rubber duck%';
128|Rubber duck|6183|9372
492|Rubber duck|92|8934
738|Rubber duck|3251|188
848|Rubber duck|8649|5648
1108|Rubber duck|1062|89
1116|Rubber duck|2226|1996
1378|Rubber duck|3963|1451
1405|Rubber duck|8750|9731
1486|Rubber duck|6580|9995
1635|Rubber duck|4798|6440
1734|Rubber duck|6110|1426
2210|Rubber duck|8569|9451
2218|Rubber duck|4254|3772
2627|Rubber duck|3122|7339
2681|Rubber duck|1303|8083
2753|Rubber duck|902|1801
2930|Rubber duck|2080|4182
2953|Rubber duck|7930|5176
3060|Rubber duck|4610|8578
3160|Rubber duck|8764|5280
3164|Rubber duck|1250|9958
3616|Rubber duck|2479|1493
4033|Rubber duck|6252|3747
4273|Rubber duck|9306|8323
4809|Rubber duck|5928|5145
4990|Rubber duck|8608|2498
5001|Rubber duck|2919|9211
5489|Rubber duck|6932|3
5509|Rubber duck|7891|5544
5831|Rubber duck|4919|4683
5902|Rubber duck|1856|5870
5989|Rubber duck|8816|7927
6075|Rubber duck|7121|9448
6191|Rubber duck|7622|187
6278|Rubber duck|1309|9050
6438|Rubber duck|900|3396
6486|Rubber duck|4890|9895
7013|Rubber duck|4570|4949
7180|Rubber duck|9769|6811
7207|Rubber duck|9563|1133
7553|Rubber duck|3098|8216
7603|Rubber duck|3525|7139
7722|Rubber duck|4072|2783
7838|Rubber duck|3694|462
8002|Rubber duck|9132|3576
8348|Rubber duck|7136|221
9297|Rubber duck|9976|4676
9318|Rubber duck|7290|5161
9497|Rubber duck|8815|7549
9612|Rubber duck|5361|2396
9953|Rubber duck|8816|4332
-- There seems to be a lot of Rubber duck enthusiasts. Let's try to narrow it down. Is there a way to find a package with no return address?
SELECT * FROM "packages" WHERE "from_address_id" IS NULL;
5098|Duck debugger||50
-- Ah, now we're getting someplace. Not what I expected but I think this fits.
-- Let's get additional info on the package
SELECT * FROM "addresses" WHERE "id" = 50
50|123 Sesame Street|Residential

-- *** The Forgotten Gift ***
-- First let's find the id of the sender address
SELECT * FROM "addresses" WHERE "address" = '109 Tileston Street';
9873|109 Tileston Street|Residential
-- Now let's find info on the package
SELECT * FROM "packages" WHERE "from_address_id" = 9873;
9523|Flowers|9873|4983
-- Now we know that the packages are flowers and we have the address id
-- Next let's find out status
SELECT * FROM "scans" WHERE "package_id" = 9523 AND "address_id" = 9873;
10432|11|9523|9873|Pick|2023-08-16 21:41:43.219831
-- From this we can see that it was picked up but has not been dropped off (dead flowers incoming!) 
-- Let's find out who has it
SELECT "name" FROM "drivers" WHERE "id" = 11;
Maegan

--*** Dese ***
-- Find the names all public schools in Massachusetts
SELECT "name" FROM "schools" WHERE "type" = 'Public School' AND "state" = 'MA';
-- This returns a long list of 1761 public schools
-- Find name of districts that are no longer operational.
SELECT "name"  FROM "districts" WHERE "name" LIKE '%(non-op)%';
-- Returns a long list of 121 districts
-- Get average per-pupil expenditure for all school districts in Massachusetts
SELECT "district_id", AVG("per_pupil_expenditure") AS "Average District Per-Pupil Expenditure"
   ...> FROM "expenditures"
   ...> GROUP BY "district_id";
-- This returns a long list of 178 districts with their average per-pupil expenditure
-- Find 10 cities with the highest number of public schools in Massachusetts
SELECT "city", COUNT("id") AS "Number of Public Schools" FROM "schools"
   ...> WHERE "type" = 'Public School' AND "state" = 'MA'
   ...> GROUP BY "city"
   ...> ORDER BY "Number of Public Schools" DESC
   ...> LIMIT 10;
   Springfield|64
Worcester|47
Lynn|27
New Bedford|26
Lowell|26
Lawrence|26
Dorchester|25
Brockton|24
Quincy|19
Fall River|18
-- Find cities with 3 or fewer public schools in Massachusetts
SELECT "city", COUNT("id") AS "Number of Public Schools" FROM "schools"
   ...> WHERE "type" = 'Public School' AND "state" = 'MA'
   ...> GROUP BY "city"
   ...> HAVING "Number of Public Schools" <= 3
   ...> ORDER BY "Number of Public Schools" ASC;