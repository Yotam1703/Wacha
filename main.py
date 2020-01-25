def WrdPerf(word,isStart,isEnd): 
                CritFilled = 0
                if isStart:
                    CritFilled += 1
                if isEnd:
                    CritFilled += 1
                if len(word) <= 4: 
                    CritFilled += 1
                if word[0] == "ב":
                    CritFilled -= 1
                if word[0] == "ל":
                    CritFilled -= 1
                if word[0] == "ע":
                    CritFilled += 1  
                if word.endswith("י"):
                    CritFilled += 1
                if word.endswith("א"):
                    CritFilled -= 1
                IsAmb = CritFilled >= 1
                return IsAmb

def SentPerf(sentence):
    AreAmb = []
    SplitSentence = sentence.split(" ")
    for word in SplitSentence:
        IsStart = word == SplitSentence[0]
        IsEnd = word == SplitSentence[-1]
        AreAmb.append(WrdPerf(word,IsStart,IsEnd)) 
    return AreAmb

def Eval(sentence,RealSentPerf):
    SuccessfullEvals = 0 
    SentencePerformance = SentPerf(sentence) 
    for i in range(len(SentencePerformance)):
        if SentencePerformance[i] == RealSentPerf[i]:
            SuccessfullEvals += 1 
    return 100*SuccessfullEvals/len(SentencePerformance) 

##ריח של ים
Sentence1 = "בעיני רבים ההגדרה של החופשה המושלמת היא בטן גב ברצועת חוף אקזוטית"
RealSentencePerf1 = [True,True,False,True,False,True,True,False,False,False,False,False]
Sentence2 = "המרכיבים ההכרחיים הם חול בין אצבעות הרגליים שמש מלטפת המיית הגלים ואוויר של ים"
RealSentencePerf2 = [True,False,True,True,True,False,True,True,False,False,False,False,True,False]
Sentence3 = "אבל מהו בעצם אוויר של ים איך הוא מקבל את הניחוח הייחודי שלו והאם בכלל כדאי לנו לדעת מה אנחנו מכניסים לריאות כשאנו לוקחים נשימה עמוקה על החוף"
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
Sentence23 = "כותבת הפוסט הישראלית שמספרת כי אביה הוא בעל משק חקלאי כבר שלושים שנים ביקשה בפוסט שאם חשובה לכם מדינת ישראל והחקלאות הישראלית התעלמו מהסרטון תסבירו לחברים שלכם מה זה אומר ותזכירו לכולם שבישראל רק חקלאות ישראלית"
RealSentencePerf23 = [True,False,True,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,True,False,True]
Sentence24 = "ותמשיכו לאכול חסה לא מסרטנת מלאה בברזל טובה לעיכול ועוד מלא סגולות ששמורות רק לה ולא לאף ירק אחר"
RealSentencePerf24 = [False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True]
Sentence25 = "לפוסט צורף סרטון של אביה בו הוא מסביר שנעשה לחסה עוול גדול"
RealSentencePerf25 = [False,True,False,True,False,False,False,True,False,True,False,True]
##איך הכחדנו את הממותות... שוב
Sentence26 = "בערבות סיביר פורחת בשנים האחרונות תעשייה יוצאת דופן באופייה"
RealSentencePerf26 = [True,False,True,False,True,False,True,False,False]
Sentence27 = "חטים קדומים של ממותות ששרידים רבים מהן השתמרו בקרקעות הקפואות נחפרים בהמוניהם מתוך האדמה כדי לענות על הביקוש הרב לשנהב בסין שם תכשיטים וחפצי אומנות מגולפים משנהב הפכו סמל סטטוס לעשירים"
RealSentencePerf27 = [False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True]
Sentence28 = "הסחר שהיקפו עומד על יותר מחמש מאות טונות בשנה מתנהל ברובו הרחק מעיני הרשויות והחוק ועוזר לפרנס את תושביו של אחד האזורים העניים ביותר ברוסיה"
RealSentencePerf28 = [False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,True,True,False,True]


def avg(numbers):
    return sum(numbers)/len(numbers)

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
Evaluations = [Eval1,Eval2,Eval3,Eval4,Eval5,Eval6,Eval7,Eval8,Eval9,Eval10,Eval11,Eval12,Eval13,Eval14,Eval15,Eval16,Eval17,Eval18,Eval19,Eval20,Eval21,Eval22,Eval23,Eval24,Eval25,Eval26,Eval27,Eval28]

BigSentence = [Sentence1,Sentence2,Sentence3,Sentence4,Sentence5,Sentence6,Sentence7,Sentence8,Sentence9,Sentence10,Sentence11,Sentence12,Sentence13,Sentence14,Sentence15,Sentence16,Sentence17,Sentence18,Sentence19,Sentence20,Sentence21,Sentence22,Sentence23,Sentence24,Sentence25,Sentence26,Sentence27,Sentence28]
BigRealSentencePerf = [RealSentencePerf1,RealSentencePerf2,RealSentencePerf3,RealSentencePerf4,RealSentencePerf5,RealSentencePerf6,RealSentencePerf7,RealSentencePerf8,RealSentencePerf9,RealSentencePerf10,RealSentencePerf11,RealSentencePerf12,RealSentencePerf13,RealSentencePerf14,RealSentencePerf15,RealSentencePerf16,RealSentencePerf17,RealSentencePerf18,RealSentencePerf19,RealSentencePerf20,RealSentencePerf21,RealSentencePerf22,RealSentencePerf23,RealSentencePerf24,RealSentencePerf25,RealSentencePerf26,RealSentencePerf27,RealSentencePerf28]

TFListList = []
for sent in BigSentence:
    TFListList += [SentPerf(sent)]
lennTFLIST = 0
for TFList in TFListList:
    for TF in TFList:
        if TF:
            print(1)
        else:
            print(0)

    
