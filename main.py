##WrdPerf returns True if the word is ambiguous (==Satisfies at least one criterion), False otherwise.
##SentPerf returns a list of True and False, evalutaing WrdPerf on each word.
##Eval compares SentPerf and the actual, provided evaluation, returning the percentage of successfull evaluations.

###TODO: בכלמ seprately, ו, ש, combinations ("ומ..."), different lens, place, XXX letter is in word
###TODO: (excel sheet of AmbLetters composition vs. HebLetters),  ים/ות seperately, י,ות ending, 
###TODO: longer corpus!!, automation!! ONLP lib, hindsight explanations!!, grade vs. AmbCount
###TODO: NN discussion, 

def WrdPerf(word,isStart): 
    CritFilled = 0 ##criterions for ambiguous words
    if isStart: ##word is in head of sentence
        CritFilled += 1 
    if len(word) <= 4: ##word is four letters or less
        CritFilled += 1
    if word[-1:-2] == "ים" or word[-1:-2] == "ות": ##word ends in "ים" or "ות"
        CritFilled += 1
#    if word[0] == "ב" or word[0] == "כ" or word[0] == "ל" or word[0] =="מ":
#        CritFilled += 1 ##word begins with "ב" "כ" "ל" "ם"
#    if word[0] == "ה":
#        CritFilled += 1
    IsAmb = CritFilled != 0 ##One criterion filled is enough (???)
    return IsAmb

def SentPerf(sentence):
    AreAmb = [] ##True/False list for the sentence
    SplitSentence = sentence.split(" ") ##turns the sentence to a list
    for word in SplitSentence:
        IsStart = word == SplitSentence[0] ##checks if the word is in head of sentence
        AreAmb.append(WrdPerf(word,IsStart)) ##check if word is ambiguous, and add the result to AreAmb
    return AreAmb

def Eval(sentence,RealSentPerf):
    SuccessfullEvals = 0 ##number of successes
    SentencePerformance = SentPerf(sentence) ##True/False list for the sentence
    for i in range(len(SentencePerformance)): ##at every index...
        if SentencePerformance[i] == RealSentPerf[i]: ##...compare the evaluation and the actual evaluation
            SuccessfullEvals += 1 ##if success - increment SuccessfullEvals
    return 100*SuccessfullEvals/len(SentencePerformance) 

EXsentence1 = "בעיני רבים ההגדרה של החופשה המושלמת היא בטן גב ברצועת חוף אקזוטית"
EXRealSentencePerf1 = [True,True,False,True,False,True,True,False,False,False,False,False]
EXsentence2 = "המרכיבים ההכרחיים הם חול בין אצבעות הרגליים שמש מלטפת המיית הגלים ואוויר של ים"
EXRealSentencePerf2 = [True,False,True,True,True,False,True,True,False,False,False,False,True,False]

print (SentPerf(EXsentence1))
print (EXRealSentencePerf1)
print (Eval(EXsentence1,EXRealSentencePerf1))
