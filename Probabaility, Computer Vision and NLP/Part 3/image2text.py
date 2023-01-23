from PIL import Image, ImageDraw, ImageFont
import sys
import math

CHARACTER_WIDTH=14
CHARACTER_HEIGHT=25


def load_letters(fname):
    im = Image.open(fname)
    px = im.load()
    (x_size, y_size) = im.size
    print(im.size)
    print(int(x_size / CHARACTER_WIDTH) * CHARACTER_WIDTH)
    result = []
    for x_beg in range(0, int(x_size / CHARACTER_WIDTH) * CHARACTER_WIDTH, CHARACTER_WIDTH):
        result += [ [ "".join([ '*' if px[x, y] < 1 else ' ' for x in range(x_beg, x_beg+CHARACTER_WIDTH) ]) for y in range(0, CHARACTER_HEIGHT) ], ]
    return result

def load_training_letters(fname):
    TRAIN_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' "
    letter_images = load_letters(fname)
    return { TRAIN_LETTERS[i]: letter_images[i] for i in range(0, len(TRAIN_LETTERS) ) }

#####
# main program
if len(sys.argv) != 4:
    raise Exception("Usage: python3 ./image2text.py train-image-file.png train-text.txt test-image-file.png")

(train_img_fname, train_txt_fname, test_img_fname) = sys.argv[1:]
train_letters = load_training_letters(train_img_fname)
test_letters = load_letters(test_img_fname)
# print(train_letters['I'])
# print(test_letters[0])
keys=list(train_letters.keys())
# print(keys,'keys')
stri=''
TRAIN_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(),.-!?\"' "

def read_data(fname):
    exemplars = []
    file = open(fname, 'r')
    for line in file:
        data = tuple([w for w in line.split()])
        exemplars += [(data[0::2]), ]
#         print(exemplars,'examplars')
    return exemplars

def return_clean_data():
    train_data = read_data(train_txt_fname)
    cleaned_data = ""

    for line1 in train_data:
        strp = ""
        for line in line1:
            # TRAIN_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+(),.-!?\"' "
            strp += " " + ''.join(c for c in line if c in TRAIN_LETTERS)
        for a in ",.-!?\"' ":
            strp = strp.replace(" "+a, a)
        cleaned_data += strp + "\n"
    return cleaned_data.strip()

a=return_clean_data().splitlines()
# a.lower()
# print(a,'a')
tot={}
ini={}
# print(a[0])
for i in a:
#     print(i)
    if i[0]!=' ':
        if i[0] not in ini:
            ini[i[0]]=1
        else:
            ini[i[0]]+=1
        for x in i:
            if x not in tot:
                tot[x]=1
            else:
                tot[x]+=1
    elif len(i)>1:
        if i[1] not in ini:
            ini[i[1]]=1
        else:
            ini[i[1]]+=1
        for x in i[1:]:
            if x not in tot:
                tot[x]=1
            else:
                tot[x]+=1
                
def emission(tr,te):
    p=1
#     print(len(tr),len(te),'trte')
    for j in range(len(tr)):
        for i in range(len(tr[j])):
            if tr[j][i]==te[j][i]:
                if tr[j][i]=='*':
                    p*=0.75
                else:
                    p*=0.15
            else:
                p*=0.1
#     return p
    return math.log(p)*-1
i=0
# print(test_letters[7],'000')
# print(train_letters['o'],'III')
for test in test_letters:
#     print(test,'test')
    max=keys[0]
    if max in tot:
        max_prob=emission(train_letters[max],test)+(math.log(tot[max]/sum(tot.values()))*-1)
    for train in keys:
#         print(train,'train')
        if train in tot:
            if max_prob>emission(train_letters[train],test)+(math.log(tot[train]/sum(tot.values()))*-1):
                max=train
                max_prob=emission(train_letters[train],test)+(math.log(tot[train]/sum(tot.values()))*-1)
#             print(max,max_prob,i)
    stri+=max
    i+=1
# print(stri,'str')

## Below is just some sample code to show you how the functions above work. 
# You can delete this and put your own code here!

# print(tot)
# print(ini)
ini_prob={}
for i in tot.keys():
    if i in ini.keys():
        ini_prob[i]=math.log(ini[i]/tot[i])*-10
# print(ini_prob)
# for test in test_letters:
#     print(test,'test')
d_after={}
# d_before={}
for i in a:
    for j in range(len(i)-1):
        if (i[j],i[j+1]) not in d_after:
            d_after[(i[j],i[j+1])]=1
        else:
            d_after[(i[j],i[j+1])]+=1
# print(d_after)

# for i in a:
#     for j in range(len(i)-1,0,-1):
#         if (i[j],i[j-1]) not in d_before:
#             d_before[(i[j],i[j-1])]=1
#         else:
#             d_before[(i[j],i[j-1])]+=1
# print(d_before)
# tran_before={}
at=""
for i in range(len(a)):
    at+=str(a[i])
at=at.upper()
    # print(at,'at')
for j in range(len(at)-1):
    if (at[j],at[j+1]) not in d_after:
        d_after[(at[j],at[j+1])]=1
    else:
        d_after[(at[j],at[j+1])]+=1
at=at.lower()
for j in range(len(at)-1):
    if (at[j],at[j+1]) not in d_after:
        d_after[(at[j],at[j+1])]=1
    else:
        d_after[(at[j],at[j+1])]+=1
tran_after={}
for (i,j) in d_after.keys():
    tran_after[(i,j)]=math.log(d_after[(i,j)]/(tot[i]))*-1

# print(tran_after)
# for (i,j) in d_before.keys():
#     tran_before[(i,j)]=d_before[(i,j)]/tot[j]
# print(d_before.keys(),'keys')
str=''
# print(ini_prob[keys[1]])
z=0
p=0
phrase={}
for train in ini.keys():
    phrase[train]=emission(train_letters[train],test_letters[0])
# print(phrase,'phr')
for test in test_letters[1:]:
    ph_keys=list(phrase.keys())
#     print(ph_keys,'ph')
    for train in ph_keys:
        mini=train
        min_prob=phrase[mini]
        x=0
        while(1):
            if (train[-1],keys[x]) in tran_after:
#                 print(train[-1],keys[x])
                mini=train+keys[x]
                min_prob=phrase[train]+tran_after[(train[-1],keys[x])]+emission(train_letters[keys[x]],test)
                break
            else:
                x+=1
        for t in keys[x+1:]:
            if (train[-1],t) in tran_after:
                prob=phrase[train]+tran_after[(train[-1],t)]+emission(train_letters[t],test)
#                 if t=='o':
#                     print(prob,tran_after[(train[-1],t)],emission(train_letters[t],test),t)
                if min_prob>prob:
                    min_prob=prob
                    mini=train+t
#                     print(min_prob,tran_after[(train[-1],t)],emission(train_letters[t],test),mini)
        phrase[mini]=phrase.pop(train)
        phrase[mini]=min_prob
#     print(phrase,'phrase')
val=min(phrase.values())
a=''
for k,v in phrase.items():
#     print(k,v)
    if v==val:
        a=k
        break
        
        
# print(test_letters[0],'testst')
for test in test_letters:
    t=0
    max=keys[0]
    if z==0:
        if max in ini_prob:
            max_prob=emission(train_letters[max],test)+ini_prob[max]+(math.log(tot[max]/sum(tot.values()))*-1)
        for train in keys:
        #         print(train,'train')
            e=emission(train_letters[train],test)
    #         print(e,train)
            if train in ini_prob:
#                 print(e,ini_prob[train],train)
                if max_prob>e+ini_prob[train]+(math.log(tot[train]/sum(tot.values()))*-1):
                    max=train
                    max_prob=e+ini_prob[train]+(math.log(tot[train]/sum(tot.values()))*-1)
    else:
        while(1):
            if (str[z-1],max) in tran_after:
                max_prob=emission(train_letters[max],test)+tran_after[(str[z-1],max)]+(math.log(tot[max]/sum(tot.values()))*-1)
                break
            else:
                t+=1
                max=keys[t]
        for train in keys:
        #         print(train,'train')
            e=emission(train_letters[train],test)
#                     print(max,max_prob,i)
            if (str[z-1],train) in tran_after:
#                 print(e,tran_after[(str[z-1],train)],str[z-1],train)
                if max_prob>e+tran_after[(str[z-1],train)]+(math.log(tot[train]/sum(tot.values()))*-1):
                    max=train
                    max_prob=e+tran_after[(str[z-1],train)]+(math.log(tot[train]/sum(tot.values()))*-1)
                
    str+=max
#     print(str)
    z+=1
#     p+=max_prob

str1=""
str1+=str[-1]
test_back=test_letters[::-1]
# for test in test_letters[1:]:
    
# print(str,'sss')


# Each training letter is now stored as a list of characters, where black
#  dots are represented by *'s and white dots are spaces. For example,
#  here's what "a" looks like:
# print("\n".join([ r for r in train_letters['o'] ]))

# Same with test letters. Here's what the third letter of the test data
#  looks like:
# print("\n".join([ r for r in test_letters[2] ]))



# The final two lines of your output should look something like this:
print("Simple: " + stri)
print("   HMM: " + a) 
