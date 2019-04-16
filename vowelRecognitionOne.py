#! /usr/bin/env python3







def vowel_recognition(s):
    vowels ="aeiouAEIOU"
    count = 0

    times= len(s)
    x=0

    for i in range(len(s)):
            if s[i] in vowels:
                count+=1

    for j in range(times-1):
        for i in range(len(s)-1):
            check= s[0:(i+2)]
            for i in range(len(check)):
                if check[i] in vowels:
                    count+=1
        s= s[(x+1):]


    return count


a= vowel_recognition("bbbb")
b= vowel_recognition("baceb")
c= vowel_recognition("aeiou")
d= vowel_recognition("aeiouAEIOU")
e= vowel_recognition("Programfinishesquiggledwithexitcode1PressENTERtsquiggletconsolehedwithexitcode1PressENTEfinsquiggledwithexitcode1PressENTERtoexitconsquigglesolehe")
print(a)
print(b)
print(c)
print(d)
print(e)






































# end




# end
