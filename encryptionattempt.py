import math

primes = {'A': 1,'B': 2,'C': 3,'D': 5,'E': 7,'F': 11,'G': 13,'H': 17,'I': 19,'J': 23,'K': 29,'L': 31,'M': 37,'N': 41,'O': 43,'P': 47,'Q': 53,'R': 59,'S': 61,'T': 67,'U': 71,'V': 73,'W': 79,'X': 83,'Y': 89,'Z': 97};
A = 1;
B = 2;
C = 3;
D = 5;
E = 7;
F = 11;
G = 13;
H = 17;
I = 19;
J = 23;
K = 29;
L = 31;
M = 37;
N = 41;
O = 43;
P = 47;
Q = 53;
R = 59;
S = 61;
T = 67;
U = 71;
V = 73;
W = 79;
X = 83;
Y = 89;
Z = 97;

def hash(string):
    split = [];
    value = 0;
    values1 = [];
    values2 = [];
    values3 = [];
    values4 = [];
    nup = [];
    c = 0;
    binary = "";

    for i in string:
        split.append(str.upper(i));
        
    print(split);

    for i in split:
        value = primes[i];
        value2 = value * 3;
        value3 = value * 7;
        values1.append(value);
        values1.append(value2);
        values1.append(value3);
        
    print(values1);
    while (c < 100):
        for i in values1:
            if (c < 100):
                for j in values1:
                    if (c < 100):
                        k = i * j;
                        values2.append(k);
                        c += 1;
                        print(c);
                
    print(values2);

    for i in values2:
        k = i;
        if (k > 1):
            k = i;
            while (k > 1):
                k = k / 2;
                if (k < 1):
                    k = k - 0.25;
                    k = round(k);
        values3.append(k);

    print(values3);
    for i in values3:
        binary+=str(i);
    print(binary);
    print(len(binary));

while True:
    string = input("hash: ");
    hash(string);
