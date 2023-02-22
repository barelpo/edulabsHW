import re

print(re.match("[A-Z][a-z]+", "dat"))
print(re.search("TATAA(A|C|G|T){3}TT", "ACGACGTTTACACGGATATAAGGGTTACGCGCTGTATAATGTGATCAGCTGATTCGAA"))
print(re.match("[0-9]{2}.[^0-9]{2}", "12*lo"))
print(re.search("TATAA(A|C|G|T){3}TT.*TATAA(A|C|G|T){3}TT", "ACGACGTTTACACGGATATAAGGGTTTATAAGGGTTTGATTCGAA"))

