### Data munging

The code in the Python program, [solution.py](solution.py), contains the solutions to the **data munging** part of this exam.

### Spreadsheet analysis

The spreadsheet file, [users.xlsx](./data/users.xlsx), contains the solutions to the **spreadsheet analysis** part of this exam. In addition, the formulas used in that spreadsheet are indicated below:

- abide by [the instructions](./instructions/instructions.md#entering-respones-into-the-readme-file) for how to enter responses into this file correctly.
- **Make sure that all spreadsheet formulae you enter into this document work exactly as written.**

1. Total number of users of the social network

```
=COUNT(A2:A1001)
```

2. Number of users in each of the states in the Pacific sub-region, which includes Alaska, California, Hawaii, Oregon and Washington.

```
=COUNTIF(H2:H1001, H317)
=COUNTIF(H2:H1001, H5)
=COUNTIF(H2:H1001, H193)
=COUNTIF(H2:H1001, H256)
=COUNTIF(H2:H1001, H3)
```

3. Number of users in each of the given 5 cities of the USA: Nashville, Tennessee; San Diego, California; New York City, New York; Dallas, Texas; and Seattle, Washington.

```
=COUNTIFS(G2:G1001,G32,H2:H1001,H32)
=COUNTIFS(G2:G1001,G80, H2:H1001,H80)
=COUNTIFS(G2:G1001,G197,H2:H1001,H197)
=COUNTIFS(G2:G1001,G2,H2:H1001,H2)
=COUNTIFS(G2:G1001,G60,H2:H1001,H60)
```

4. The average affinity category IDs of all users in New York for each of the content types.

```
=AVERAGEIF(H2:H1001, H7, I2:I1001)
=AVERAGEIF(H2:H1001, H7, J2:J1001)
=AVERAGEIF(H2:H1001, H7, K2:K1001)
=AVERAGEIF(H2:H1001, H7, L2:L1001)
```

### SQL queries

This section shows the SQL queries that you determined solved each of the given problems.

- abide by [the instructions](./instructions/instructions.md#entering-respones-into-the-readme-file) for how to enter responses into this file correctly.
- **Make sure that all SQL commands you enter into this document work exactly as written, including semi-colons, where necessary.**

1. Write two SQL commands to create two tables named `users` and `affinity_categories` within the given database file.

```sql
create table users (
    id INTEGER PRIMARY KEY,
    handle TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    street TEXT NOT NULL,
    city TEXT NOT NULL,
    states TEXT NOT NULL,
    animal TEXT NOT NULL,
    food INTEGER NOT NULL,
    luxury INTEGER NOT NULL,
    tech INTEHER NOT NULL,
    travel INTEGER NOT NULL
    );
.tables
.schema users
```

```sql
create table affinity_categories (
    id INTEGER PRIMARY KEY,
    type_ TEXT NOT NULL,
    level_ INTEGER NOT NULL,
    cost_impression INTEGER NOT NULL,
    cost_thousand INTEGER NOT NULL
    );
.tables
.schema affinity_categories
```

2. Import the data in the `users.csv` and `affinity_categories.csv` CSV files into these two tables.

```sql
create table temp_table (
    id INTERGER NOT NULL,
    handle TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    street TEXT NOT NULL,
    city TEXT NOT NULL,
    states TEXT NOT NULL,
    animal TEXT NOT NULL,
    food INTEGER NOT NULL,
    luxury INTEGER NOT NULL,
    tech INTEHER NOT NULL,
    travel INTEGER NOT NULL
    );
 ```

```sql   
.mode csv
.headers on
.separator ","
```

```sql
.import /Users/tt/Desktop/exam-1-TiXiao/data/users.csv users --skip 1
```

```sql
INSERT INTO users
(id, handle, first_name, last_name, email, street, city, states, animal, food, luxury, tech, travel)
SELECT * FROM temp_table;
```

```sql
DROP TABLE temp_table;
```

```sql
create table temp_table (
    id INTEGER NOT NULL,
    type_ TEXT NOT NULL,
    level_ INTEGER NOT NULL,
    cost_impression INTEGER NOT NULL,
    cost_thousand INTEGER NOT NULL
    );
```

```sql   
.mode csv
.headers on
.separator ","
```

```sql
.import /Users/tt/Desktop/exam-1-TiXiao/data/affinity_categories.csv affinity_categories --skip 1
```

```sql
INSERT INTO affinity_categories
(id, type_, level_, cost_impression, cost_thousand)
SELECT * FROM temp_table;
```

```sql
DROP TABLE temp_table;
```

3. Display the state name and the number of users in that state for each of the states for which we have users.

```sql
select states, count(handle)from users group by states; 
```

4. Display the state name, the number of users in that state, and the average `travel_affinity_category_id` for each of the states for which we have users.

```sql
select states, count(handle), avg(travel) from users group by states;
```

5. Display the email addresses only of all users residing in Pittsburgh, Pennsylvania.

```sql
select email from users where city = "Pittsburgh" and states = "Pennsylvania";
```

6. Display the email addresses of all users residing in Pittsburgh, Pennsylvania, along with the price the social network would charge an advertiser to show one advertisement to each of them, based on their `travel_affinity` level.

```sql
select email, cost_impression from users INNER JOIN affinity_categories on users.travel = affinity_categories.id where users.city = "Pittsburgh" and users.states = "Pennsylvania";
```

7. Display the amount the social network would charge an advertiser to show two advertisement to three thousand users with a `real_food_affinity` level of `0.75`.

```sql
select 6*cost_thousand from affinity_categories where type_='real_food_affinity' and level_=0.75;
```

8. Show all the users for whom the `tech_gadget_affinity_category_id` field contains an invalid foreign key.

```sql
select * from users where tech = "NULL";
```

9. Write an additional SQL query of your choice using SQL with this table; then describe the results

Write a description of the query here.

```sql
select level_, states from users INNER JOIN affinity_categories on users.travel = affinity_categories.id group by users.states;
```
This query identifies all of the users from different states have different affinities for travel, while Illinois, Montana, Oregon, South Carolina, Washington, Massachusetts, Maryland, and District of Columbia has a strong affinity for travel.

### Normalization and Entity-relationship diagramming

This section contains responses to the questions on normalization and entity-relationship diagramming.

- abide by [the instructions](./instructions/instructions.md#entering-respones-into-the-readme-file) for how to enter responses into this file correctly.

1. Is the data in `users.csv` in fourth normal form?

```
No, the users.csv is not in 4NF.
```

2. Explain why or why not the `users.csv` data meets 4NF.

```
Because it violetes the requirement of 4NF, it has two more independent multi-valued fact about an enity. For example, the street belongs to city, while city belongs to states).
Also, it violets the requirement of 3NF. All non-key field are not about the fact of the primary key, like the city, city animals.etc are about the place/address rather than the users.
```

3. Is the data in `affinity_categories.csv` in fourth normal form?

```
No, the affinity_categories.csv is not in 4NF. 
```

4. Explain why or why not the `affinity_categories.csv` data meets 4NF.

```
Because it contains two or more independent multi-valued facts about an entity which is not allowed in 4NF, A single affinity has multiple preference levels and/or multiple types (two independent multi-valued facts about them) might [erroneously] be represented with two or more independent multi-valued fact fields.
```

5. Use [draw.io](https://draw.io) to draw an Entity-Relationship Diagram showing a 4NF-compliant form of this data, including primary key field(s), relationship(s), and cardinality.

![ E-R Diagram](./images/images_ERD.svg)
