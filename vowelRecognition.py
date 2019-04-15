#! /usr/bin/env python3




vowels ="aeiouAEIOU"
count = 0


def vowel_recognition(s):
    global count
    count =0

    def vowel_count_char(exaimin):
        global count
        global vowels

        for i in range(len(exaimin)):
            if exaimin[i] in vowels:
                count+=1

    def vowel_count_thro(ns):
        global count
        global vowels
        times= len(ns)
        x=0


        for j in range(times):
            for i in range(len(ns)-1):
                check= ns[0:(i+2)]
                vowel_count_char(check)
            ns= ns[(x+1):]



    vowel_count_char(s)
    vowel_count_thro(s)


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
