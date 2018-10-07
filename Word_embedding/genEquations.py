from __future__ import print_function

import sys
import argparse
import random

dict_number = {
"0" : "zéro",
"1" : "un",
"2" : "deux",
"3" : "trois",
"4" : "quatre",
"5" : "cinq",
"6" : "six",
"7" : "sept",
"8" : "huit",
"9" : "neuf",
"10" : "dix",
"11" : "onze",
"12" : "douze",
"13" : "treize",
"14" : "quatorze",
"15" : "quinze",
"16" : "seize",
"17" : "dix-sept",
"18" : "dix-huit",
"19" : "dix-neuf",
"20" : "vingt",
"21" : "vingt et un",
"22" : "vingt-deux",
"23" : "vingt-trois",
"24" : "vingt-quatre",
"25" : "vingt-cinq",
"26" : "vingt-six",
"27" : "vingt-sept",
"28" : "vingt-huit",
"29" : "vingt-neuf",
"30" : "trente",
"31" : "Trente et un",
"32" : "Trente-deux",
"33" : "Trente-trois",
"34" : "Trente-quatre",
"35" : "Trente-cinq",
"36" : "Trente-six",
"37" : "Trente-sept",
"38" : "Trente-huit",
"39" : "Trente-neuf",
"40" : "quarante",
"41" : "quarante et un",
"42" : "quarante-deux",
"43" : "quarante-trois",
"44" : "quarante-quatre",
"45" : "quarante-cinq",
"46" : "quarante-six",
"47" : "quarante-sept",
"48" : "quarante-huit",
"49" : "quarante-neuf",
"50" : "cinquante",
"51" : "cinquante et un",
"52" : "cinquante-deux",
"53" : "cinquante-trois",
"54" : "cinquante-quatre",
"55" : "cinquante-cinq",
"56" : "cinquante-six",
"57" : "cinquante-sept",
"58" : "cinquante-huit",
"59" : "cinquante-neuf",
"60" : "soixante",
"61" : "soixante et un",
"62" : "soixante-deux",
"63" : "soixante-trois",
"64" : "soixante-quatre",
"65" : "soixante-cinq",
"66" : "soixante-six",
"67" : "soixante-sept",
"68" : "soixante-huit",
"69" : "soixante-neuf",
"70" : "soixante-dix",
"71" : "soixante-et-onze",
"72" : "soixante-douze",
"73" : "soixante-treize",
"74" : "soixante-quatorze",
"75" : "soixante-quinze",
"76" : "soixante-seize",
"77" : "soixante-dix-sept",
"78" : "soixante-dix-huit",
"79" : "soixante-dix-neuf",
"80" : "quatre-vingts",
"81" : "quatre-vingt-un",
"82" : "quatre-vingt-deux",
"83" : "quatre-vingt-trois",
"84" : "quatre-vingt-quatre",
"85" : "quatre-vingt-cinq",
"86" : "quatre-vingt-six",
"87" : "quatre-vingt-sept",
"88" : "quatre-vingt-huit",
"89" : "quatre-vingt-neuf",
"90" : "quatre-vingt-dix",
"91" : "quatre-vingt-onze",
"92" : "quatre-vingt-douze",
"93" : "quatre-vingt-treize",
"94" : "quatre-vingt-quatorze",
"95" : "quatre-vingt-quinze",
"96" : "quatre-vingt-seize",
"97" : "quatre-vingt-dix-sept",
"98" : "quatre-vingt-dix-huit",
"99" : "quatre-vingt-dix-neuf",
"100" : "cent"
        }

operations = {
        "+" : "plus",
        "-" : "moins",
        "*" : "fois"
        }


parser = argparse.ArgumentParser(description='Create french mathematical equations')
parser.add_argument("--num", help="number of samples", type=int,default=1000)
parser.add_argument("--maxlength", help="number of maximum elements in equation" , type=int, default=5)
parser.add_argument("--min", help="minimum number value", type=int,default=0)
parser.add_argument("--max", help="maximum number value", type=int, default=100)
parser.add_argument("--path" , help="path to output file", default="./equations.txt")
args = parser.parse_args()

def toFrench(eq,dict_number,operations):
    french = []
    for i in range(len(eq)):
        if(i%2 == 0):
            french.append(dict_number[eq[i]])
        else :
            french.append(operations[eq[i]])
    return " ".join(french)

data = []
for _ in range(args.num):
    eq = []
    eq.append(str(random.randint(args.min,args.max)))

    eqLength = random.randint(3,args.maxlength)
    eqLength -= (1 - eqLength % 2)
    for i in range(eqLength - 1):
        if(i%2 == 0):
            randOp = random.randint(0,2)
            eq.append(['+','-','*'][randOp])
        else :
            eq.append(str(random.randint(args.min,args.max)))

    print(eval(" ".join(eq)) ,"\t",toFrench(eq,dict_number,operations))
    data.append(toFrench(eq,dict_number,operations)+"\t"+str(eval(" ".join(eq)))+"\n")

with open(args.path,'w',encoding='utf8') as f:
    f.writelines(data)


