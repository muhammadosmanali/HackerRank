/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

Select Distinct CITY From STATION Where SubStr(CITY, -1, Length(CITY)) = 'a' or SubStr(CITY, -1, Length(CITY)) = 'e' or SubStr(CITY, -1, Length(CITY)) = 'i' or SubStr(CITY, -1, Length(CITY)) = 'o' or SubStr(CITY, -1, Length(CITY)) = 'u';