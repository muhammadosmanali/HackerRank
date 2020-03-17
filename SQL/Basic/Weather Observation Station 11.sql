/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

Select Distinct CITY From STATION 
Where (SubStr(CITY,1,1) <> 'A' and
    SubStr(CITY,1,1) <> 'E' and 
    SubStr(CITY,1,1) <> 'I' and 
    SubStr(CITY,1,1) <> 'O' and 
    SubStr(CITY,1,1) <> 'U') 
      or
      (SubStr(CITY, -1, Length(CITY)) <> 'a' and 
    SubStr(CITY, -1, Length(CITY)) <> 'e' and 
    SubStr(CITY, -1, Length(CITY)) <> 'i' and 
    SubStr(CITY, -1, Length(CITY)) <> 'o' and 
    SubStr(CITY, -1, Length(CITY)) <> 'u');