/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

Select Distinct CITY From STATION Where SubStr(CITY,1,1) = 'A' or SubStr(CITY,1,1)='E' or SubStr(CITY,1,1)='I' or SubStr(CITY,1,1)='O' or SubStr(CITY,1,1)='U';