def print_num(x):
    p = {
        0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"
    }

    for i in str(x):
        print(p[(int)(i)])
    
print_num(123)