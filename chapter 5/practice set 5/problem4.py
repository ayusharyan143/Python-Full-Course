'''
    What will be the length of following set s:
        s = set()
        s.add(20)
        s.add(20.0)
        s.add('20') # length of s after these operations?

'''

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print("Length : " , len(s))

# Here it will return 2 bcz 20 == 20.0 is same and in set it only store uniqe element