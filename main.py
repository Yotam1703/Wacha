#WrdPerf returns True if the word is ambiguous (==Satisfies at least one criterion), False otherwise.
##SentPerf returns a list of True and False, evalutaing WrdPerf on each word.
##Eval compares SentPerf and the actual, provided evaluation, returning the percentage of successfull evaluations.

###TODO: בכלמ seprately, ו, ש, combinations ("ומ..."), different lens, place, XXX letter is in word
###TODO: (excel sheet of AmbLetters composition vs. HebLetters),  ים/ות seperately, י,ות ending, 
###TODO: longer corpus!!, automation!! ONLP lib, hindsight explanations!!, grade vs. AmbCount
###TODO: NN discussion, 

####BLOCK: functions
def WrdPerf(word,isStart): 
                CritFilled = 0
                if isStart: ##word is in head of sentence
                                CritFilled += 1 
                if len(word) <= 4: 
                                CritFilled += 1
#               if word[-1:-2] == "ים": 
#                                CritFilled += 1
#               if word[-1:-2] == "ות": 
#                               CritFilled += 1
#                if word[0] == "ב": 
#                               CritFilled += 1
#                if word[0] == "כ": 
#                                CritFilled += 1
#                if word[0] == "ל":
#                                CritFilled += 1
                if word[0] == "מ": 
                                CritFilled += 1      
#                if word[0] == "ה":
#                               CritFilled += 1
                IsAmb = CritFilled != 0 ##One criterion filled is enough (???)
                return IsAmb

def SentPerf(sentence):
    AreAmb = [] ##True/False list for the sentence
    SplitSentence = sentence.split(" ") ##turns the sentence to a list
    for word in SplitSentence:
        IsStart = word == SplitSentence[0] 
        AreAmb.append(WrdPerf(word,IsStart)) 
    return AreAmb

def Eval(sentence,RealSentPerf):
    SuccessfullEvals = 0 
    SentencePerformance = SentPerf(sentence) 
    for i in range(len(SentencePerformance)): ##at every index...
        if SentencePerformance[i] == RealSentPerf[i]: ##...compare the evaluation and the actual evaluation
            SuccessfullEvals += 1 
    return 100*SuccessfullEvals/len(SentencePerformance) 


####BLOCK:sentences
EXsentence1 = "בעיני רבים ההגדרה של החופשה המושלמת היא בטן גב ברצועת חוף אקזוטית"
EXRealSentencePerf1 = [True,True,False,True,False,True,True,False,False,False,False,False]
EXsentence2 = "המרכיבים ההכרחיים הם חול בין אצבעות הרגליים שמש מלטפת המיית הגלים ואוויר של ים"
EXRealSentencePerf2 = [True,False,True,True,True,False,True,True,False,False,False,False,True,False]
EXsentence3 = "אבל מהו בעצם אוויר של ים איך הוא מקבל את הניחוח הייחודי שלו והאם בכלל כדאי לנו לדעת מה אנחנו מכניסים לריאות כשאנו לוקחים נשימה עמוקה על החוף"
EXRealSentencePerf3 = [True,False,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False]
EXsentence4 = "כשמבקשים מאנשים לתאר את ריחו של הים התשובות הנפוצות כוללות בדרך כלל את המושגים רענן טרי מלוח או דגי בווריאציות שונות"
EXRealSentencePerf4 = [True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,]
EXsentence5 = "ריח הים נוצר מקוקטייל של כימיקלים רבים שמקורם בריקבון מוות ופירוק חיידקי עם קורטוב של מליחות אצות ואורגניזמים ימיים"
EXRealSentencePerf5 = [False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False]
EXsentence6 = "לא נשמע רומנטי ורענן כמו רוב השירים שנכתבו על הים אבל זה מה שיש"
EXRealSentencePerf6 = [False,True,False,True,True,True,False,False,True,False,True,False,True,False]
EXsentence7 = "אז כדי להבין קצת יותר מאיפה מגיע הריח ומה מרכיב אותו נבחן כמה מהמולקולות היותר נפוצות שמתעופפות במשבי הבריזה"
EXRealSentencePerf7 = [True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True]


####BLOCK:results
def avg(numbers):
    return sum(numbers)/len(numbers)

Eval1 = Eval(EXsentence1,EXRealSentencePerf1)
Eval2 = Eval(EXsentence2,EXRealSentencePerf2)
Eval3 = Eval(EXsentence3,EXRealSentencePerf3)
Eval4 = Eval(EXsentence4,EXRealSentencePerf4)
Eval5 = Eval(EXsentence5,EXRealSentencePerf5)
Eval6 = Eval(EXsentence6,EXRealSentencePerf6)
Eval7 = Eval(EXsentence7,EXRealSentencePerf7)
Eval = [Eval1,Eval2,Eval3,Eval4,Eval5,Eval6,Eval7]

print (avg(Eval))
