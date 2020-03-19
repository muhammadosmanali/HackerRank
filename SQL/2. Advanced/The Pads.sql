/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

Select 
    Case
        When Occupation = 'Doctor' Then Concat(Name, '(D)')
        When Occupation = 'Singer' Then Concat(Name, '(S)')
        When Occupation = 'Professor' Then Concat(Name, '(P)')
        When Occupation = 'Actor' Then Concat(Name, '(A)')
    End
From OCCUPATIONS Order By Name;

Select Concat('There are a total of ', 
              Concat(Count(Occupation), 
                    Concat(' ', 
                          Concat(Lower(Occupation), 's.')))) 
From OCCUPATIONS
Group By Occupation
Order By Count(Occupation), Occupation;
