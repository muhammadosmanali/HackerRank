/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

Select Name From STUDENTS
Where Marks > 75
Order by SubStr(Name, -3, Length(Name));