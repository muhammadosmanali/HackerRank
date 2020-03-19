/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

Select CITY, Length(CITY) From (Select CITY, Length(CITY) FROM STATION Order By CITY) 
Where Length(CITY) = (Select min(Length(CITY)) From STATION) 
And Rownum = 1;

Select CITY, Length(CITY) From (Select CITY, Length(CITY) FROM STATION Order By CITY) 
Where Length(CITY) = (Select max(Length(CITY)) From STATION) 
And Rownum = 1;