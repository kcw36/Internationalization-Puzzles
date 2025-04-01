# Puzzle 3 - Unicode passwords

Most websites that accept passwords have some requirements. For example, they make you include at least one digit and at least one capital letter. The idea is that if you pick passwords from a large set of possible characters, the password will be harder to crack using brute force methods. It's much harder to guess a password that include digits, upper-case and lower-case letters (62 possibilities) instead of just lower-case letters (26 possibilities) You wonder why websites don't encourage you to use accented characters, because it would dramatically increase the possibilities even further. Unicode is a boon for strong passwords.

Here we'll look at what such a password system could look like.

The IT department of a ficticious company named "TOPlap" has decided to introduce new, unicode-based password requirements. The requirements are as follows:

a length of at least 4 and at most 12
at least one digit
at least one uppercase letter (with or without accents, examples: A or Ż)
at least one lowercase letter (with or without accents, examples: a or ŷ)
at least one character that is outside the standard 7-bit ASCII character set (examples: Ű, ù or ř)

Your input is a list of passwords, one on each line. Write a program that checks if each password meets the requirements. Your answer should be the number of passwords that are valid. In the test input given above, the number of valid passwords is '2'.

How many passwords from your input data are valid?