# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:18:42 2020

@author: javid
"""

print('            ***********')
print('         ******************')
print('      ************************')
print(' *************************************')
print('Welcome to the GTA Vice City Trial Test')
print(' *************************************')
print('      ************************')
print('         ******************')
print('            ************')

name = input('Please enter your name: ')
print()
print('We\'ll ask you questions,you just need to enter the number of the answer.')
print()
print('At the end we will show your result :D')
print()
print("Q1: what is the cheat for sabre turbo?")
print('1.getthereamazinglyfast')
print('2.getthereveryfastindeed')
print('3.gettherefast')
print('4.gettherequickly')
q1 = int(input('Please enter the answer: '))
print()

print("Q2: what is the cheat for remote grenade?")
print('1.nuttertools')
print('2.professionaltools')
print('3.thugstools')
print('4. 1 & 2')
q2 = int(input('Please enter the answer: '))
print()

print("Q3: which cheat give you money?")
print('1.moneymoney')
print('2.hesoyam')
print('3.bigbang')
print('4.none')
q3 = int(input('Please enter the answer: '))
print()

print("Q4: which year did the game release?")
print('1.1986')
print('2.1992')
print('3.2000')
print('4.2002')
q4 = int(input('Please enter the answer: '))
print()


print("Q5: the twins work for whom?")
print('1.lance vance')
print('2.kent paul')
print('3.pastor richards')
print('4.ricardo diaz')
q5 = int(input('Please enter the answer: '))
print()

print("Q6: who is in the chopper in the first scene?")
print('1.lance vance')
print('2.kent paul')
print('3.sonny forelli')
print('4.none')
q6 = int(input('Please enter the answer: '))
print()

print("Q7: how many cars will be parked atlast in sunshine autos?")
print('1.three')
print('2.two')
print('3.four')
print('4.five')
q7 = int(input('Please enter the answer: '))
print()

print("Q8: which way will make you very rich indeed?")
print('1.vigilante mission with tank')
print('2.taxi mission')
print('3.cone crazy mission')
print('4.100% complete')
q8 = int(input('Please enter the answer: '))
print()


print("Q9: who's song is missing in pc version?")
print('1.michael jackson')
print('2.lionel richie')
print('3.kim wilde')
print('4.laura branigan')
q9 = int(input('Please enter the answer: '))
print()

print("Q10: where does ken rosenberg live?")
print('1.ocean view hotel')
print('2.hotel harrison')
print('3.3321 vice point')
print('4.moist plalms hotel')
q10 = int(input('Please enter the answer: '))
print()

print("Q11: who is tommy vercetti?")
print('1.mobster')
print('2.lawyer')
print('3.driver')
print('4.drug dealer')
q11 = int(input('Please enter the answer: '))
print()

print("Q12: what color is first tommy's shirt?")
print('1.pink')
print('2.blue')
print('3.green')
print('4.white')
q12 = int(input('Please enter the answer: '))
print()

print("Q13: what is the last color of tommy's shirt?")
print('1.pink')
print('2.blue')
print('3.green')
print('4.white')
q13 = int(input('Please enter the answer: '))
print()

print("Q14: how can you explode banner-pulling dodo?")
print('1.by tank')
print('2.with rpg')
print('3.with chopper')
print("4.can't")
q14 = int(input('Please enter the answer: '))
print()
print('            ***********')
print('         ******************')
print('      ************************')
print(' ********************************')
print('Thaaaaaaaaaaaaaaankkkkksssssssssssss')
print(' ********************************')
print('      ************************')
print('         ******************')
print('            ************')
print()
a = 0
ans = []
if q1 == 3:
    a = a+1
else:
    ans.append('gettherefast is the cheat for sabre turbo')
if q2 == 2:
    a = a+1
else:
    ans.append('professionaltools is the only cheat for remote grenade')
if q3 == 3:
    a = a+1
else:
    ans.append('there\'s no money cheats, but by using bigbang cheat you\'ll earn money by exploded vehicles')
if q4 == 4:
    a = a+1
else:
    ans.append('the game storyline taken place in 1986 but the game release in our world in 2002')
if q5 == 4:
    a = a+1
else:
    ans.append('the twins had an artwork with diaz')
if q6 == 1:
    a = a+1
else:
    ans.append('you see lance vance in the chopper in the very first of the game')
if q7 == 4:
    a = a+1
else:
    ans.append('at sunshine Autos with one car that always parked in, there will be 5 cars')
if q8 == 3:
    a = a+1
else:
    ans.append('with some nice works during conecrazy mission you can get the highest money rank, search in youtube for detail')
if q9 == 2:
    a = a+1
else:
    ans.append('the song running with the night by lionel richie had been removed from flash radio in pc versions and some ps2 versions')
if q10 == 2:
    a = a+1
else:
    ans.append('ken rosenberg lives in hotel harrison')
if q11 == 1:
    a = a+1
else:
    ans.append('tommy vercetti is a gangster and the drug lord, not just a drug dealer')
if q12 == 2:
    a = a+1
else:
    ans.append('the first tommy\'s shirt is blue with dark trees')
if q13 == 4:
    a = a+1
else:
    ans.append('when you finish the game 100% a white shirt with quotes appears in diaz\'s house')
if q14 == 3:
    a = a+1
else:
    ans.append('you can explode the dodo in the sky by hunter(army helicopter)')

a_p = (a/14)*100

if len(ans) == 0:
    print('   ***************')
    print('  **\/**/\**/\**\/*')
    print(' ***/\**\/**\/**/\**')
    print('*********************')
    print('*****CONGRAAATSSSS*****')
    print('YOU ANSWER 100% CORRECT')
    print('*****TOMMY VERCETTI*****')
    print('*********CONGRATS AGAIN:')
    print(name)
    print('*****************')
    print('*************************')
    print('*****\/***/\**\/***/\****')
    print('*****/\***\/**/\***\/****')
    print('*************************')
else:
    print('congrats')
    print('you answer:')
    print(a_p)
    print('percent')
    print('correctly')
    print()
    print('and here is your wrong answers, correct essays:')
    print(ans)
print('Thank you so much')
print('God bless you')
print('bye bye')
print('see you in miami2, 2022')
input('press any key for end')