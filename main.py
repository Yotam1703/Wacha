#WrdPerf returns True if the word is ambiguous (==Satisfies at least one criterion), False otherwise.
##SentPerf returns a list of True and False, evalutaing WrdPerf on each word.
##Eval compares SentPerf and the actual, provided evaluation, returning the percentage of successfull evaluations.

###TODO: בכלמ seprately, ו, ש, combinations ("ומ..."), different lens, place, XXX letter is in word
###TODO: (excel sheet of AmbLetters composition vs. HebLetters),  ים/ות seperately, י,ות ending, 
###TODO: longer corpus!!, automation!! ONLP lib, hindsight explanations!!, grade vs. AmbCount
###TODO: NN discussion, 


def WrdPerf(word,isStart,isEnd): 
                CritFilled = 0
#                if isStart: ##word is in head of sentence
 #                               CritFilled += 1
  #              if isEnd:
   #                             CritFilled += 1
                if len(word) <= 4: 
                                CritFilled += 1
                if len(word) >= 6: 
                                CritFilled -= 1              
#                if word[-1:-2] == "ים": 
#                                CritFilled += 1
#                if word[-1:-2] == "ות": 
#                               CritFilled += 1
                if word[0] == "ה":
                               CritFilled -= 1 ##
#                if word[0] == "ב":
 #                              CritFilled += 1
#                if word[0] == "מ":
 #                              CritFilled -= 1
                if word[0] == "ל":
                               CritFilled -= 1
                if word[0] == "כ":
                               CritFilled += 1                                   
#                if word[0] == "ו":
#                               CritFilled += 1
                if word[0] == "ש":
                               CritFilled += 1

                IsAmb = CritFilled >= 1 ##One criterion filled is enough (???)
                return IsAmb

def SentPerf(sentence):
    AreAmb = [] ##True/False list for the sentence
    SplitSentence = sentence.split(" ") ##turns the sentence to a list
    for word in SplitSentence:
        IsStart = word == SplitSentence[0]
        IsEnd = word == SplitSentence[-1]
        AreAmb.append(WrdPerf(word,IsStart,IsEnd)) 
    return AreAmb

def Eval(sentence,RealSentPerf):
    SuccessfullEvals = 0 
    SentencePerformance = SentPerf(sentence) 
    for i in range(len(SentencePerformance)): ##at every index...
        if SentencePerformance[i] == RealSentPerf[i]: ##...compare the evaluation and the actual evaluation
            SuccessfullEvals += 1 
    return 100*SuccessfullEvals/len(SentencePerformance) 


EXsentence1 = "בעיני רבים ההגדרה של החופשה המושלמת היא בטן גב ברצועת חוף אקזוטית"
EXRealSentencePerf1 = [True,True,False,True,False,True,True,False,False,False,False,False]
EXsentence2 = "המרכיבים ההכרחיים הם חול בין אצבעות הרגליים שמש מלטפת המיית הגלים ואוויר של ים"
EXRealSentencePerf2 = [True,False,True,True,True,False,True,True,False,False,False,False,True,False]
EXsentence3 = "אבל מהו בעצם אוויר של ים איך הוא מקבל את הניחוח הייחודי שלו והאם כדאי לנו לדעת מה אנחנו מכניסים לריאות כשאנחנו לוקחים נשימה עמוקה על החוף"
EXRealSentencePerf3 = [True,False,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False]
EXsentence4 = "כשמבקשים מאנשים לתאר את ריחו של הים התשובות הנפוצות כוללות בדרך כלל את המושגים רענן טרי מלוח או דגי בווריאציות שונות"
EXRealSentencePerf4 = [True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,]
EXsentence5 = "ריח הים נוצר מקוקטייל של כימיקלים רבים שמקורם בריקבון מוות ופירוק חיידקי עם קורטוב של מליחות אצות ואורגניזמים ימיים"
EXRealSentencePerf5 = [False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False]
EXsentence6 = "לעיתים הריח יקושר לסביבה הקרובה יותר כמו הריח של קרם הגנה או של כלב רטוב לאחר טבילה בים"
EXRealSentencePerf6 = [True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,True]
EXsentence7 = "יש מי שיפליגו על גלי הדימויים וידברו על ריח של חופש נעורים אנרגיה ובריאות"
EXRealSentencePerf7 = [True,True,False,True,True,False,False,True,False,True,True,False,False,True]
EXsentence8 = "חובבי המילה הכתובה בטח ייזכרו במשורר או בסופר האהובים עליהם יוצקים בריח הים רומנטיקה ואהבה"
EXRealSentencePerf8 = [False,False,True,True,False,True,False,True,True,True,True,False,False,False,True]
EXsentence9 = "פחות סביר שתשמעו את התשובה המדעית המלאה ויש לזה סיבה טובה"
EXRealSentencePerf9 = [True,True,False,True,False,False,True,True,False,False,True]
EXsentence10 = "ריח הים נוצר מקוקטייל של כימיקלים רבים שמקורם בריקבון מוות ופירוק חיידקי עם קורטוב של מליחות אצות ואורגניזמים ימיים"
EXRealSentencePerf10 = [False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False] 
EXsentence11 = "לא נשמע רומנטי ורענן כמו רוב השירים שנכתבו על הים אבל זה מה שיש"
EXRealSentencePerf11 = [False,True,False,True,True,True,False,False,True,False,True,False,True,False]
EXsentence12 = "אז כדי להבין קצת יותר מאיפה מגיע הריח ומה מרכיב אותו נבחן כמה מהמולקולות היותר נפוצות שמתעופפות במשבי הבריזה"
EXRealSentencePerf12 = [True,True,False,True,True,False,False,True,False,True,False,True,Trgue,False,False,True,False,False,True]
##MILA stopped working here
EXsentence13 = "מדובר במולקולה קטנה אך מסריחה שריחה מתואר כדומה לזה של כרוב או אספרגוס מבושל"
EXRealSentencePerf13 = [False,True,True,False,True,False,True,True,True,True,True,False,False,False]
EXsentence14 = "אבל לא מדובר בחומר שריחו בהכרח דוחה אותנו"
EXRealSentencePerf14 = [True,False,True,False,False,False,True,True]
EXsentence15 = "בריכוזים מסוימים תוכלו למצוא אותו ביין או בירה במגוון ירקות ופירות לרבות עגבניות ומנגו והוא תורם גם לניחוח של גבינות קשות מיושנות ופטריות כמהין"
EXRealSentencePerf15 = [False,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,True,False,False,
EXsentence16 = ""
EXRealSentencePerf16 = []
EXsentence17 = ""
EXRealSentencePerf17 = []
EXsentence18 = ""
EXRealSentencePerf18 = []
EXsentence19 = ""
EXRealSentencePerf19 = []
EXsentence20 = ""
EXRealSentencePerf20 = []
EXsentence21 = ""
EXRealSentencePerf21 = []
EXsentence22 = ""
EXRealSentencePerf22 = []
EXsentence23 = ""
EXRealSentencePerf23 = []
EXsentence24 = ""
EXRealSentencePerf24 = []
EXsentence25 = ""
EXRealSentencePerf25 = []



def avg(numbers):
    return sum(numbers)/len(numbers)

Eval1 = Eval(EXsentence1, EXRealSentencePerf1)
Eval2 = Eval(EXsentence2, EXRealSentencePerf2)
Eval3 = Eval(EXsentence3, EXRealSentencePerf3)
Eval4 = Eval(EXsentence4, EXRealSentencePerf4)
Eval5 = Eval(EXsentence5, EXRealSentencePerf5)
Eval6 = Eval(EXsentence6, EXRealSentencePerf6)
Eval7 = Eval(EXsentence7, EXRealSentencePerf7)
Eval8 = Eval(EXsentence8, EXRealSentencePerf8)
Eval9 = Eval(EXsentence9, EXRealSentencePerf9)
Eval10 = Eval(EXsentence10, EXRealSentencePerf10)
Eval11 = Eval(EXsentence11, EXRealSentencePerf11)
Eval12 = Eval(EXsentence12, EXRealSentencePerf12)
Eval13 = Eval(EXsentence13, EXRealSentencePerf13)
Eval14 = Eval(EXsentence14, EXRealSentencePerf14)
Eval = [Eval1,Eval2,Eval3,Eval4,Eval5,Eval6,Eval7,Eval8,Eval9,Eval10,Eval11,Eval12]

print (avg(Eval))
