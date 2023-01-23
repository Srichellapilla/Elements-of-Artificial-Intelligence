###################################
# CS B551 Spring 2021, Assignment #3
#
# Your names and user ids:
#
# (Based on skeleton code by D. Crandall)
#


import random
import math


# We've set up a suggested code structure, but feel free to change it. Just
# make sure your code still works with the label.py and pos_scorer.py code
# that we've supplied.
#
class Solver:
    prob=1
    va=0
    ini_word={}
    ini_part={}
    tot={}
    tot_word={}
    tran={}
    ps={}
    hmm={}
    emi={}
    # word_speech={}
    ini={}
    # Calculate the log10 of the posterior probability of a given sentence
    #  with a given part-of-speech labeling. Right now just returns -999 -- fix this!
    def posterior(self, model, sentence, label):
        if model == "Simple":
            return math.log10(self.prob)
        elif model == "HMM":
            return self.va
        elif model == "Complex":
            for i in range(len(sentence)):
                if i==0:
                    p=math.log10(self.ini[label[i]])
                else:
                    p=math.log10(self.tran(label[i-1],label[i]))
                return math.log(self.emi.get((sentence[i],label[i]),1e-10))+p
        else:
            print("Unknown algo!")

    # Do the training!
    #
    def train(self, data):
        word=[]
        pos=[]
        for i in range(len(data)):
            word.append(data[i][0])
            pos.append(data[i][1])
#         print(word[0:100])
        for j in range(len(word)):
#             print(self.tot)
            wor=word[j]
            for i in range(len(wor)):
                if pos[j][i] not in self.ps:
                    self.ps[pos[j][i]]=1
                else:
                    self.ps[pos[j][i]]+=1                    
                if i==0:
                    if pos[j][i] not in self.ini:
                        self.ini[pos[j][i]]=1
                    else:
                        self.ini[pos[j][i]]+=1
                if wor[i] not in self.tot_word:
                    self.tot_word[wor[i]]=1
                    self.tot[(wor[i],pos[j][i])]=1
                else:
                    self.tot_word[wor[i]]+=1
                    if (wor[i],pos[j][i]) not in self.tot:
                        self.tot[(wor[i],pos[j][i])]=1
                    else:
                        self.tot[(wor[i],pos[j][i])]+=1
                if i<len(wor)-1:
                    if (pos[j][i],pos[j][i+1]) not in self.tran:
                        self.tran[(pos[j][i],pos[j][i+1])]=1
                    else:
                        self.tran[(pos[j][i],pos[j][i+1])]+=1
        tr=sum(self.tran.values())
        for word in self.tot_word:
            for pos in self.ps:
                if (word,pos) not in self.tot:
                    self.tot[(word,pos)]=0
        for i in self.ini.keys():
            self.ini[i]=self.ini[i]/tr
        for i in self.tran.keys():
            self.tran[i]=self.tran[i]/tr
        for i in self.tot.keys():
            if self.tot[i]:
                self.emi[i]=self.tot[i]/self.ps[i[1]]
            else:
                self.emi[i]=1e-10
        # for i in em.keys():
        #     em[i]=(em[i]*(self.ps[i[1]]/tr))/(self.tot_word[i[0]]/tr)
        # print(em[('the','det')])

    # Functions for each algorithm. Right now this just returns nouns -- fix this!
    #
    def simplified(self, sentence):
        self.prob=1
        st=[]
        pos=list(self.ps.keys())
        l=list(self.tot.keys())
        tot=self.tot
        se=sum(self.tot_word.values())
        for i in sentence:
            maxi=1e-10
            max_ele='noun'
            for j in pos:
                if i in self.tot_word:
                    if self.emi[(i,j)]>maxi:
                        maxi=self.emi[(i,j)]
                        max_ele=j
#             print(i)
            st.append(max_ele)
            self.prob*=maxi
#         print(st,prob)
        # st=['noun']*len(sentence)
        return st

    def hmm_viterbi(self, sentence):
        # print(sentence)
        # print(em)
        em=self.emi
        ini=self.ini
        ps_list=list(self.ps.keys())
        le=len(ps_list)*len(ps_list)
        su=sum(self.tot_word.values())
        malo=math.log10(1e-10)
        tran=self.tran
        tot=self.tot_word
        self.hmm={}
        for i in ps_list:
            # i=str(i)
            # print(i)
            if sentence[0] in tot:
                self.hmm[i]=-1*(math.log10(ini[i])+math.log10(em[sentence[0],i]))
            else:
                self.hmm[i]=-1*malo
        for i in range(1,len(sentence)):
            hmm_list=list(self.hmm.keys())
            for l in hmm_list:
                # print(l)
                # z=0
                x=l.split(',')
                # print(x,str(x))
                pss=ps_list[0]
                min_ele=pss
                if sentence[i] in tot:
                    mini=self.hmm[l]-math.log10(em[(sentence[i],pss)])
                else:
                    mini=self.hmm[l]-malo
                if (x[-1],pss) in tran:
                    # print('b')
                    mini=mini-math.log10(tran[(x[-1],pss)])
                else:
                    mini=mini-malo
                for j in range(1,len(ps_list)):
                    if sentence[i] in tot:
                        p=self.hmm[l]-math.log10(em[(sentence[i],ps_list[j])])
                    else:
                        p=self.hmm[l]-malo
                    if (x[-1],ps_list[j]) in tran:
                        # print(math.log10(self.tran[(x[-1],ps_list[j])]),math.log10(self.tot[(sentence[i],ps_list[j])]))
                        p=p-math.log10(tran[(x[-1],ps_list[j])])
                    else:
                        p=p-malo
                    # print(p)
                    if mini>p:
                        mini=p
                        min_ele=ps_list[j]
                self.hmm[l+','+min_ele]=self.hmm.pop(l)
                self.hmm[l+','+min_ele]=mini
                # print(mini,x[-1],min_ele)
        v=min(self.hmm.values())
        a=''
        for key, val in self.hmm.items():
            if val==v:
                a=key
                break
        x=a.split(',')
        # print(x)
        self.va=v*-1
        return x

    def complex_mcmc(self, sentence):
        ps_list=list(self.ps.keys())
        ret=[]
        bp = []
        l=[]
        for i in sentence:
            st=[]
            for p in ps_list:
                if (i, p) in self.tot:
                    st.append(self.tot[(i,p)]/sum(self.tot_word.values()))
                else:
                    st.append(1e8)
            m=min(st)
            for i in range(len(st)):
                if st[i] == 1e8:
                    st[i] = m*1e-10
            s=sum(st)
            for i in range(len(st)):
                st[i]=st[i]/s
            t=0
            for i in range(len(st)):
                t+=st[i]
                st[i]=t
            bp.append(st)
        for i in range(len(sentence)):
            j=50
            l.append([])
            while j>0:
                j-=1
                rx=random.random()
                for k in range(12):
                    if rx<=bp[i][k]:
                        l[i].append(ps_list[k])
                        break
        for i in l:
            ret.append(i[-1])
        return ret


    # This solve() method is called by label.py, so you should keep the interface the
    #  same, but you can change the code itself. 
    # It should return a list of part-of-speech labelings of the sentence, one
    #  part of speech per word.
    #
    def solve(self, model, sentence):
        if model == "Simple":
            return self.simplified(sentence)
        elif model == "HMM":
            return self.hmm_viterbi(sentence)
        elif model == "Complex":
            return self.complex_mcmc(sentence)
        else:
            print("Unknown algo!")
