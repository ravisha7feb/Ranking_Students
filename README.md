# Ranking_Students
You are given a text file, that contains the roll numbers and marks of students
in five subjects. (What the subjects are is immaterial and in fact so are roll
numbers. We will use A, B, C for roll numbers.) Here is a sample file:
A 12 14 16
B 5 6 7
C 17 20 23
D 2 40 12
E 6 44 15
F 7 8 9
G 4 5 6
We say that a student P is better than another student Q, if in all subjects
P has scored more than Q. This is represented by P >Q.
The >relationship is transitive. That is if T >U and U >V, then T >V. We
can represent the whole relationship with T >U >V.
It is possible that in some subjects P has scored more while Q has scored
more in the others. So there may not be a relationship between P and Q.
Mathematicians say that this relation is a partial order.
The problem is to show the existing ordering relationship for the given data.
For example the above file data will be represented as:
C >A >F >B >G
E >D
2
