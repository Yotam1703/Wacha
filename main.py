
def WrdPerf(word,pos):
    CritFilled = 0
    if pos:
        CritFilled += 1
    if len(word) <= 4:
        CritFilled += 1
    if word[-1:-2] == "ים" or word[-1:-2] == "ות":
        CritFilled += 1
    if word[0] == "ב" or word[0] == "כ" or word[0] == "ל" or word[0] =="מ":
        CritFilled += 1
    IsAmb = CritFilled != 0
    return IsAmb

def SentPerf(sentence):
    AreAmb = []
    SplitSentence = sentence.split(" ")
    for word in SplitSentence:
        pos = word == SplitSentence[0]
        AreAmb.append(WrdPerf(word,pos))
    return AreAmb

def Eval(sentence,RealSentPerf):
    SuccessfullEvals = 0
    SentencePerformance = SentPerf(sentence)
    for Eval in SentencePerformance:
        if Eval == RealSentPerf[SentencePerformance.index(Eval)]:
            SuccessfullEvals += 1
    return SuccessfullEvals/len(sentence)*100

ExSentence = "ששש"
print (SentPerf(ExSentence))