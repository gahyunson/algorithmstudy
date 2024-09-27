`LEFT JOIN`   
~~~sql
   SELECT * 
     FROM Sales s
LEFT JOIN Product p
       ON p.id = s.id;
~~~
Product table gives the information to Sales table.

`JOIN` or `INNER JOIN`
~~~sql
    SELECT * 
      FROM Sales s
INNER JOIN Product p
        ON p.id = s.id;
~~~
Each tables give the information to each them, but they don't give columns and data if each don't have.
So tables's order doesn't matter.

`RIGHT JOIN`
`FULL OUTER JOIN`
