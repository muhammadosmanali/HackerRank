/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

Select Case
    When A = B and B = C Then 'Equilateral'
    When (A + B) <= C Then 'Not A Triangle'
    When (B + C) <= A Then 'Not A Triangle'
    When (C + A) <= B Then 'Not A Triangle'
    When A = B and B <> C Then 'Isosceles'
    When B = C and C <> B Then 'Isosceles'
    When A = C and C <> B Then 'Isosceles'
    Else 'Scalene'
End
From TRIANGLES