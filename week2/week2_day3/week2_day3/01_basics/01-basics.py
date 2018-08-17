import re
'''
#* Name a yellow food that this regular expression will match ```"[abn]+"```
string1 = "banana"
result1 = re.search("[abn]+", string1)
print(result1)

#* Write a sentence that this regular expression will match ```"^Once.*end\.$"```
string2 = "Once upon a time until the end."
result2 = re.search("^Once.*end\.$", string2)
print(result2)

# Write a similar sentence that the expression won't match.
notstring3 = "Once upon a time until the en."
result3 = re.search("^Once.*end\.$", notstring3)
print(result3)


* If a name record has to have a first name and a last name, separated by
and each beginning with a capital letter, write an expression that matches
this and excludes non-matching records.

string4 = "Carter Adams"
result4 = re.search("^[A-Z]* [A-Z]", string4)

string5 = "Jackie O"
result5 = re.search("^[A-Z]* [A-Z]", string5)

string6 = "Joe McGuy"
result6 = re.search("^[A-Z]* [A-Z]", string6)

notstring7 = "Sam"
result7 = re.search("^[A-Z]* [A-Z]", notstring7)

notstring8 = "Alan  Hodgson"
result8 = re.search("^[A-Z]* [A-Z]", notstring8)

notstring9 = "sarah smith"
result9 = re.search("^[A-Z]* [A-Z]", notstring9)

notstring10 = " Larry Sanders"
result10 = re.search("^[A-Z]+ [A-Z]", notstring10)

print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)


* If a name record has to have a first name and a last name, separated by and each beginning
w/ a capital letter, write an expression that matches this and excludes non-matching records.

string30 = "James Baker"
result30 = re.search("^[A-Z]+[a-z]* [A-Z]+[a-z]*$", string30)
print(result30)

* Write an expression that matches "[timestamp: 123456]" where 123456 can be any integer.
Include the [ and ] in the string to be matched.

string31 = "[timestamp: 349202]"
result31 = re.search("^\[timestamp: [0-9]{6}\]$" , string31)
print(result31)


* Write an expression that matches a string that is exactly the equals sign twenty times.
'''
string32 = "===================="
result32 = re.search("={20}" , string32)
print(result32)

