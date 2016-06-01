####Database Management Systems
----
- Declarative language: a program is the description of the desired result
- Imperative language: a program is a description of computational processes

####SQL
----
- SQL is an ANSI and ISO standard, but DBMS's implement custom variants
- a select statement creates a new table, either from scrath or by projecting a table
- a create table statement gives a global name to a table

#####Selecting Value Literals
----
- A select statement always included a comma separated list of column descriptions

- A column description is an expression, optionally followed by as and a column name

```sql
select [expression] as [name], [expression] as [name];
```

Selecting literals creates a one-row table
The union of two select statements is a table containing the rows of both of their results

```sql
create table parents as
	select "abraham" as parent, "barack" as child union
	select "abraham"		  , "clinton"         union
	select "delano" 		  , "herbert"		  union
	select "fillmore"		  , "abraham"; 
```

The result of a select statement is displayed to the user, but not stored

A create table statement gives the result a name
```sql
create table [name] as [select statement]; 
```

####Projecting Tables 
---
- A select statement can specify an input table using a from clause
- A subset of the rows of the input table can be selected using a where clause
- An ordering over the remaining rows can be declared using an order by clause
- column descriptions determine how much each input row is projected to a result row

```sql
select [expression] as [name], [expression] as [name], ...
select[columns] from [table] where [condition] order by [order]; 
select child from parents where parent = "abraham"; 
select parent from parents where parent > child; # compare strings alphabetically 
