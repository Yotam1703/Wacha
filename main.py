#WrdPerf returns True if the word is ambiguous (==Satisfies at least one criterion), False otherwise.
##SentPerf returns a list of True and False, evalutaing WrdPerf on each word.
##Eval compares SentPerf and the actual, provided evaluation, returning the percentage of successfull evaluations.

def WrdPerf(word,isStart,isEnd): 
                CritFilled = 0
                if isStart: ##word is in head of sentence
                                CritFilled += 1
                # if isEnd:
                #                 CritFilled += 1
                if len(word) <= 4: 
                                CritFilled += 1
                # if len(word) >= 6: 
                                # CritFilled -= 1              
#                 if word[-1] == "ם": 
#                                 CritFilled += 1
# #                if word[-1:-2] == "ות": 
#                               CritFilled += 1
                # if word[0] == "ה":
                #               CritFilled -= 1 
                if word[0] == "ב":
                              CritFilled -= 1
                if word[0] == "מ":
                              CritFilled += 1
                if word[0] == "ל":
                              CritFilled -= 1
                # if word[0] == "כ":
                #               CritFilled += 1                                   
                if word[0] == "ו":
                              CritFilled -= 1
                # if word[0] == "ש":
                #               CritFilled += 1

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


##ריח של ים
Sentence1 = "בעיני רבים ההגדרה של החופשה המושלמת היא בטן גב ברצועת חוף אקזוטית"
RealSentencePerf1 = [True,True,False,True,False,True,True,False,False,False,False,False]
Sentence2 = "המרכיבים ההכרחיים הם חול בין אצבעות הרגליים שמש מלטפת המיית הגלים ואוויר של ים"
RealSentencePerf2 = [True,False,True,True,True,False,True,True,False,False,False,False,True,False]
Sentence3 = "אבל מהו בעצם אוויר של ים איך הוא מקבל את הניחוח הייחודי שלו והאם כדאי לנו לדעת מה אנחנו מכניסים לריאות כשאנחנו לוקחים נשימה עמוקה על החוף"
RealSentencePerf3 = [True,False,True,False,True,False,False,True,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,False]
Sentence4 = "כשמבקשים מאנשים לתאר את ריחו של הים התשובות הנפוצות כוללות בדרך כלל את המושגים רענן טרי מלוח או דגי בווריאציות שונות"
RealSentencePerf4 = [True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,]
Sentence5 = "ריח הים נוצר מקוקטייל של כימיקלים רבים שמקורם בריקבון מוות ופירוק חיידקי עם קורטוב של מליחות אצות ואורגניזמים ימיים"
RealSentencePerf5 = [False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,False]
Sentence6 = "לעיתים הריח יקושר לסביבה הקרובה יותר כמו הריח של קרם הגנה או של כלב רטוב לאחר טבילה בים"
RealSentencePerf6 = [True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,True,False,True]
Sentence7 = "יש מי שיפליגו על גלי הדימויים וידברו על ריח של חופש נעורים אנרגיה ובריאות"
RealSentencePerf7 = [True,True,False,True,True,False,False,True,False,True,True,False,False,True]
Sentence8 = "חובבי המילה הכתובה בטח ייזכרו במשורר או בסופר האהובים עליהם יוצקים בריח הים רומנטיקה ואהבה"
RealSentencePerf8 = [False,False,True,True,False,True,False,True,True,True,True,False,False,False,True]
Sentence9 = "פחות סביר שתשמעו את התשובה המדעית המלאה ויש לזה סיבה טובה"
RealSentencePerf9 = [True,True,False,True,False,False,True,True,False,False,True]
Sentence10 = "ריח הים נוצר מקוקטייל של כימיקלים רבים שמקורם בריקבון מוות ופירוק חיידקי עם קורטוב של מליחות אצות ואורגניזמים ימיים"
RealSentencePerf10 = [False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,True,True,False,False] 
Sentence11 = "לא נשמע רומנטי ורענן כמו רוב השירים שנכתבו על הים אבל זה מה שיש"
RealSentencePerf11 = [False,True,False,True,True,True,False,False,True,False,True,False,True,False]
Sentence12 = "אז כדי להבין קצת יותר מאיפה מגיע הריח ומה מרכיב אותו נבחן כמה מהמולקולות היותר נפוצות שמתעופפות במשבי הבריזה"
RealSentencePerf12 = [True,True,False,True,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True]
##MILA stopped working here
Sentence13 = "מדובר במולקולה קטנה אך מסריחה שריחה מתואר כדומה לזה של כרוב או אספרגוס מבושל"
RealSentencePerf13 = [True,False,True,False,True,False,True,True,False,True,True,False,False,True]
Sentence14 = "אבל לא מדובר בחומר שריחו בהכרח דוחה אותנו"
RealSentencePerf14 = [True,False,True,False,False,False,True,False]
Sentence15 = "בריכוזים מסוימים תוכלו למצוא אותו ביין או בירה במגוון ירקות ופירות לרבות עגבניות ומנגו והוא תורם גם לניחוח של גבינות קשות מיושנות ופטריות כמהין"
RealSentencePerf15 = [False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,]
Sentence16 = "טכנולוגי מזון אף משתמשים בו כדי להעניק טעמי בשר דגים ביצים חמאה פירות וירקות למוצרי מזון מעובדים"
RealSentencePerf16 = [True,False,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True]
##סרטון הפלסטיק בחסה
Sentence17 = "בימים האחרונים סוערת הרשת הישראלית בעקבות סרטון בו מראים שבחסה שאנו אוכלים קיימת שכבת פלסטיק שניתן ממש לקלף אותה אחרי שמטביעים את החסה במים רותחים"
RealSentencePerf17 = [False,False,True,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True]
Sentence18 = "אולם בפוסט ויראלי שעלה בעמוד הפייסבוק סטטוסים מצייצים נראה כי כל עניין הפלסטיק בחסה יצא מפרופורציות ומדובר בסך הכל באפידרמיס שכבה שמגנה על העלה ונמצאת גם בעורם של בני האדם"
RealSentencePerf18 = [True,False,False,True,False,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False]
Sentence19 = "מצב החקלאות גם ככה בקריסה נכתתב בפוסט הסותר את טענת הפלסטיק בחסה"
RealSentencePerf19 = [True,False,False,False,False,False,False,True,True,True,False,False]
Sentence20 = "מספיקה לנו הממשלה שדואגת לחסל לאט לאט אבל בטוח את ענף החקלאות הישראלי"
RealSentencePerf20 = [True,True,False,True,False,True,True,True,True,True,True,False,True]
Sentence21 = "אין לנו צורך באנשים ללא כל ידע שינסו לחסל את החקלאות"
RealSentencePerf21 = [True,True,True,False,False,False,True,True,False,True,False]
Sentence22 = "אלו אנשים שידם קלה על המקלדת אנשים שלא חושבים פעמיים מי נמצא בצד השני"
RealSentencePerf22 = [True,True,True,True,True,False,False,False,False,False,True,False,False,True]
Sentence23 = "כותבת הפוסט הישראלית שמספרת כי אביה הוא בעל משק חקלאי כבר שלושים שנים ביקשה בפוסט שאם חשובה לכם מדינת ישראל והחקלאות הישראלית התעלמו מהסרטון תסביאו לחברים שלכם מה זה אומר ותזכירו לכולם שבישראל רק חקלאות ישראלית"
RealSentencePerf23 = [True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True]
Sentence24 = "ותמשיכו לאכול חסה לא מסרטנת מלאה בברזל טובה לעיכול ועוד מלא סגולות ששמורות רק לה ולא לאף ירק אחר"
RealSentencePerf24 = [False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True]
Sentence25 = "לפוסט צורף סרטון של אביה בו הוא מסביר שנעשה לחסה עוול גדול"
RealSentencePerf25 = [False,True,False,True,False,False,False,True,False,True,False,True]
##איך הכחדנו את הממותות... שוב
Sentence26 = "בערבות סיביר פורחת בשנים האחרונות תעשייה יוצאת דופן באופייה"
RealSentencePerf26 = [True,False,True,False,True,False,True,False,False]
Sentence27 = "חטים קדומים של ממותות ששרידים רבים מהן השתמו בקרקעות הקפואות נחפרים בהמוניהם מתוך האדמה כדי לענות על הביקוש הרב לשנהב בסין שם תכשיטים וחפצי אומנותג מגולפים משנהב הפכו סמל סטטוס לעשירים"
RealSentencePerf27 = [False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True]
Sentence28 = "הסחר שהיקפו עומד על יותר מחמש מאות טונות בשנה מתנהל ברובו הרחק מעיני הרשויות והחוק ועוזר לפרנס את תושביו של אחד האזורים העניים ביותר ברוסיה"
RealSentencePerf28 = [False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,True,True,False,True]


Eval1 = Eval(Sentence1, RealSentencePerf1)
Eval2 = Eval(Sentence2, RealSentencePerf2)
Eval3 = Eval(Sentence3, RealSentencePerf3)
Eval4 = Eval(Sentence4, RealSentencePerf4)
Eval5 = Eval(Sentence5, RealSentencePerf5)
Eval6 = Eval(Sentence6, RealSentencePerf6)
Eval7 = Eval(Sentence7, RealSentencePerf7)
Eval8 = Eval(Sentence8, RealSentencePerf8)
Eval9 = Eval(Sentence9, RealSentencePerf9)
Eval10 = Eval(Sentence10, RealSentencePerf10)
Eval11 = Eval(Sentence11, RealSentencePerf11)
Eval12 = Eval(Sentence12, RealSentencePerf12)
Eval13 = Eval(Sentence13, RealSentencePerf13)
Eval14 = Eval(Sentence14, RealSentencePerf14)
Eval15 = Eval(Sentence15, RealSentencePerf15)
Eval16 = Eval(Sentence16, RealSentencePerf16)
Eval17 = Eval(Sentence17, RealSentencePerf17)
Eval18 = Eval(Sentence18, RealSentencePerf18)
Eval19 = Eval(Sentence19, RealSentencePerf19)
Eval20 = Eval(Sentence20, RealSentencePerf20)
Eval21 = Eval(Sentence21, RealSentencePerf21)
Eval22 = Eval(Sentence22, RealSentencePerf22)
Eval23 = Eval(Sentence23, RealSentencePerf23)
Eval24 = Eval(Sentence24, RealSentencePerf24)
Eval25 = Eval(Sentence25, RealSentencePerf25)
Eval26 = Eval(Sentence26, RealSentencePerf26)
Eval27 = Eval(Sentence27, RealSentencePerf27)
Eval28 = Eval(Sentence28, RealSentencePerf28)
Eval = [Eval1,Eval2,Eval3,Eval4,Eval5,Eval6,Eval7,Eval8,Eval9,Eval10,Eval11,Eval12,Eval13,Eval14,Eval15,Eval16,Eval17,Eval18,Eval19,Eval20,Eval21,Eval22,Eval23,Eval24,Eval25,Eval26,Eval27,Eval28]

Lengths = [len(RealSentencePerf1),len(RealSentencePerf2),len(RealSentencePerf3),len(RealSentencePerf4),
           len(RealSentencePerf5),len(RealSentencePerf6),len(RealSentencePerf7),len(RealSentencePerf8),
           len(RealSentencePerf9),len(RealSentencePerf10),len(RealSentencePerf11),len(RealSentencePerf12),
           len(RealSentencePerf13),len(RealSentencePerf14),len(RealSentencePerf15),len(RealSentencePerf16),
           len(RealSentencePerf17),len(RealSentencePerf18),len(RealSentencePerf19),len(RealSentencePerf20),
           len(RealSentencePerf21),len(RealSentencePerf22),len(RealSentencePerf23),len(RealSentencePerf24),
           len(RealSentencePerf25),len(RealSentencePerf26),len(RealSentencePerf27),len(RealSentencePerf28)]


def avg(numbers):
    return sum(numbers)/len(numbers)


print (sum(Lengths))
print (avg(Eval))
