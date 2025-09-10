def opn():
    d1 = ["Abc@gmail.com","abc@gmail.com","xyz@gmail.com","pqr@gmail.com","xyz"]
    d2 = ["xyz","mno","opq","stu","xyz","abc"]
    d3 = ["abc","abc","pqr","xyz"]
    s1 = set(x.lower() for x in d1)
    s2 = set(x.lower() for x in d2)
    s3 = set(x.lower() for x in d3)
    print(s1,s2,s3)
    print("Unique attendees",len(s1|s2|s3))
    print("Who attended all days",len(s1&s2&s3))
    print("Who attended exactly one day",len((s1-(s2|s3))|(s2-(s1|s3))|(s3-(s1|s2))))
    print(f"Overlap counts : Day1&2 ->{(s1&s2)}, Day2&3 -> {(s2&s3)}, Day3&1 -> {(s1&s3)}")
opn()


