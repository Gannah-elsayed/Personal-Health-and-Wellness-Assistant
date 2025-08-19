## SHROOQ AMIN SAAD
## 202300112

def BMI(weight, height):
    x=weight/((height/100)**2)
    if x<16:
        print("\t\t\t\t\t\t\t\tYou're Severely Thin")
    elif 16<= x <=17:
        print("\t\t\t\t\t\t\t\tYou're Moderately Thinness")
    elif 17<=x<18.5:
        print("\t\t\t\t\t\t\t\tYou're Mildly Thinness")
    elif 18.5<=x<25:
        print("\t\t\t\t\t\t\t\tYou're of Normal Weight")
    elif 25<=x<30:
        print("\t\t\t\t\t\t\t\tYou're Overweight")
    elif 30<=x<35:
        print("\t\t\t\t\t\t\t\tYou're of Obese Class I")
    elif 35<=x<40:
        print("\t\t\t\t\t\t\t\tYou're of Obese Class II")
    elif x>=40:
        print("\t\t\t\t\t\t\t\tYou're of Obese Class III")
    return x

def waterIn(weight):
    y=(weight*30)/250
    return y

def ExH(y,x):
    # H = int(input("Plz enter your height:"))
    # W = int(input("Plz enter your weight:"))
    S = weight/((height/100)**2)
    if S == 18.5 or S< 25 :
       X = int(input("What is your focus part for a normal weight?: choose 1 for 'ARM', 2 for 'BELLY' , 3 for 'THIGH':\n"))
       while X!= 1 or X!= 2 or X!=3:
           break
       if X == 1 :
            print("\t\t\t\t\t\t\t\t ARM EXERCISE \t \t \t ")
            print("You should do 6 times :\n1- ARM SCISSORS.\n2- CLAPS OVER HEAD.\n3- CHEST PRESS PULSE.\n"
               "4- PUNCHES.\n""5- SEATED OVERHEAD TRICEP EXTENSION.\n6- ARM SCISSORS.\n")
       elif X ==2:
           print("\t\t\t\t\t\t\t\t BELLY EXERCISE \t \t \t ")
           print("You should do 5 times :\n1- CRUNCH KICKS.\n2- ABDOMINAL CRUNCHES.\n3- REVERSE CRUNCHES.\n"
              "4- SLOW MOUNTAIN CLIMBER.\n5- RUSSIAN TWIST.\n")
       else :
            print("\t\t\t\t\t\t\t\t THIGH EXERCISE \t \t \t ")
            print("You should do 7 times :\n1- PLIE SQUATS.\n2- FROG PRESS.\n3- DONKEY KICKS LEFT.\n"
               "4- DONKEY KICKS RIGHT.\n5- SIDE LEG CIRCLES LEFT.\n6-SIDE LEG CIRCLES RIGHT.\n7- PLIE SQUATS.\n")
    return "\t\t\t\t\t\t\t\tDo your best*"
## print(ExH(y,x))


def DH():
    X = int(input("Plz choose which diet you want to follow: choose 1 for 'Premium',2 for 'Low-Card' ,3 for 'Keto' ,"
                  "4 for 'Vegetarian' ,5 for 'Vegan'.:\n"))
    if X ==1:
        print("\t\t\t\t\t\t\t\t Premium DIET \t \t \t ")
        print("Your caloric range [0 : 385] for each recipe .")
        print("Benefits:\n No forbidden foods.\n Hundreds of Premium Recipes.\n Balanced nutrition.\n "
              "Considered the healthiest option for weight loss.\n Excellent for long-term maintenance.")
        print("---------------------")
        print("Sample Recipes\n Lemon Chicken [145 cals].\n Flank Steak [179cals]")
    elif X ==2 :
        print("\t\t\t\t\t\t\t\t Low-Card DIET \t \t \t ")
        print("Your caloric range [0 : 195] for each recipe.")
        print("Benefits:\n Protein-rich meals keep you filled and fueled.\n Helps lower blood sugar and improve insulin\n Allows more vegetables and fruit than keto diet.\n"
              " Good for short-term weight loss.")
        print("---------------------")
        print("How to benefit it :\n Lose weight a little faster by limiting calories coming from carbs in turn, safely lower your blood sugar.\n Replace most  carbs with quality proteins and fats to feel fuller longer with sustained energy and no sugar-drop energy crashes.")
        print("---------------------")
        print("Sample Recipes\n Low-Carb Turkey [147 cals].\n Sheet pqn shrimp and peppers [180 cals].")
    elif X==3:
        print("\t\t\t\t\t\t\t\t Keto DIET \t \t \t ")
        print("Your caloric range [0 : 480] for each recipe .")
        print("Benefits:\n Burns fat more effectively than other diets.\n Helps lower blood sugar.\n "
              "Higher fat content shown to reduce appetite.\n Requires discipline.")
        print("---------------------")
        print("Sample Recipes\n Keto Avocado Chicken Salad [410 cals].\n Keto Chicken zoodle soup [330 cals].")
    elif X==4 :
        print("\t\t\t\t\t\t\t\t Vegetarian DIET \t \t \t")
        print("Your caloric range [0 : 471] for each recipe .")
        print("Benefits:\n Includes dairy products and eggs, with a focus on plant foods.\n Nutritionally sound and well-balanced.\n "
             "May help you lose weight and reduce risks of heart attack, stroke, and type 2 diabetes. ")
        print("---------------------")
        print("Sample Recipes\n Powerhouse Salad [471 cals].\n Avocado and Hummus Toast [385 cals]. ")

    else :
        print("\t\t\t\t\t\t\t\t Vegan DIET \t \t \t ")
        print("Your caloric range [0 : 430] for each recipe .")
        print("Benefits:\n rich in high-fiber plant foods.\n May help you lose weight and reduce risk of heart attack, "
              "stroke, and type 2 diabetes.\n May support animal welfare and environmental concerns.")
        print("---------------------")
        print("Sample Recipes\n Slow cooker Vegan Red [250 cals].")
    return "\t\t\t\t\t\t\t\tKeep going*"
# #print(DH())


def ChronicDis(c):
    #c = int(input(chronic))
    while c < lowC or c > high:
         c = int(input('Error! ' + chronic))
    else:
        if c==0 :
            print("\t\t\t\t\t\t\t\tGood job,you're in a good health* ")
        if c==1:
            print("\t\t\t\t\t\t\t\tSorry to hear that. You suffer from Diabetes")
        elif c==2:
            print("\t\t\t\t\t\t\t\tSorry to hear that. You suffer from Pressure")
        elif c== 3:
            print("\t\t\t\t\t\t\t\tSorry to hear that. You suffer from Heart")
    return c

def DietHeart():
    print("\t\t\t\t\t\t\t\t Plz follow these instructions* 'Diet for heart disease' \t \t \t \t ")
    print("1-Diet for Heart Disease:Emphasize fruits and vegetables: Aim to include a variety of colorful fruits and vegetables in your diet. They are rich in vitamins, minerals, and antioxidants that help support heart health.\n"
"2-Choose whole grains: Opt for whole grains like whole wheat, brown rice, oats, and quinoa instead of refined grains. Whole grains are high in fiber and can help lower cholesterol levels.\n"
"3-Include lean protein sources: Select lean sources of protein such as skinless poultry, fish, legumes, and tofu. Limit red meat and choose lean cuts when consumed.\n"
"4-Healthy fats: Focus on consuming healthy fats like olive oil, avocados, nuts, and seeds. These fats provide essential nutrients and can help improve cholesterol levels.\n"
"5-Reduce sodium intake: Limit your sodium intake by avoiding processed and packaged foods, as they tend to be high in sodium. Use herbs, spices, and other flavorings to season your meals instead.")
    print("___________________________________________________________________________________________________________________")

def DietDiabetes():
    print("\t\t\t\t\t\t\t\t Plz follow these instructions* 'Diet for Diabetes disease' \t \t \t \t")
    print("1-Carbohydrate management: Monitor and control your carbohydrate intake, as carbohydrates have the most significant impact on blood sugar levels. Choose high-fiber carbohydrates like whole grains, legumes, fruits, and vegetables, as they have a slower impact on blood sugar.\n"
"2-Portion control: Pay attention to portion sizes to avoid excessive calorie intake. Use measuring cups, a food scale, or visual cues to help you estimate appropriate portion sizes.\n"
"3-Balanced meals: Aim for balanced meals that include a combination of carbohydrates, lean protein, and healthy fats. This can help stabilize blood sugar levels and provide sustained energy.\n"
"4-Fiber-rich foods: Include fiber-rich foods like whole grains, legumes, fruits, and vegetables. Fiber helps regulate blood sugar levels, improves digestion, and promotes satiety.\n"
"5-Limit added sugars and processed foods: Minimize the consumption of sugary beverages, sweets, processed snacks, and high-sugar desserts. Opt for natural sources of sweetness like fruits.")
    print("___________________________________________________________________________________________________________________")

def DietPressure():
    print("\t\t\t\t\t\t\t\tPlz follow these instructions* 'Diet for pressure disease' \t \t \t \t")
    print("1-DASH diet: Follow the Dietary Approaches to Stop Hypertension (DASH) eating plan, which emphasizes fruits, vegetables, whole grains, lean proteins, and low-fat dairy products. It also encourages reducing sodium (salt) intake.\n"
"2-Reduce sodium intake: Limit your consumption of high-sodium foods, such as processed and packaged foods, fast food, and salty snacks. Opt for fresh, whole foods and use herbs, spices, and other flavorings to season your meals instead.\n"
"3-Increase potassium-rich foods: Include potassium-rich foods like bananas, oranges, leafy greens, sweet potatoes, and avocados. Potassium helps counteract the effects of sodium and supports healthy blood pressure levels.\n"
"4-Limit saturated and trans fats: Reduce your intake of saturated fats found in red meat, full-fat dairy products, and fried foods. Avoid trans fats found in processed snacks, baked goods, and margarine. Instead, choose healthier fats like olive oil, nuts, and seeds.\n"
"5-Moderate alcohol consumption: If you choose to drink alcohol, do so in moderation. Limit it to one drink per day for women and up to two drinks per day for men.")
    print("___________________________________________________________________________________________________________________")

def ExHeart():
    print("\t\t\t\t\t\t\t\t Plz follow these instructions* 'Exercise for heart disease' \t\t\t\t\t")
    print("1-Aerobic exercise: Engage in moderate-intensity aerobic activities such as brisk walking, cycling, swimming, or dancing for at least 150 minutes per week. Consult with your healthcare provider for specific exercise recommendations based on your condition.\n"
"2-Strength training: Incorporate strength training exercises at least two days a week. This can include using resistance bands, free weights, or weight machines to strengthen your muscles.\n"
"3-Flexibility exercises: Include stretching and flexibility exercises to improve joint mobility and prevent muscle tightness.\n"
"4-Start slowly and progress gradually: If you're new to exercise or have been inactive, start with low-impact activities and gradually increase the intensity or duration over time. Listen to your body and avoid overexertion.\n"
"5-Regular physical activity: Strive for consistency by making exercise a regular part of your routine. Aim for daily movement and find activities you enjoy to help maintain long-term adherence.")
    print("___________________________________________________________________________________________________________________")

def ExDiabetes():
    print("\t\t\t\t\t\t\t\tPlz follow these instructions* 'Exercise for diabetes disease' \t\t\t\t")
    print("1-Aerobic exercise: Engage in moderate-intensity aerobic activities such as brisk walking, cycling, swimming, or dancing for at least 150 minutes per week. This helps improve insulin sensitivity and lowers blood sugar levels.\n"
"2-Strength training: Include resistance training exercises at least two days a week. This helps build muscle mass, which can enhance insulin sensitivity and improve glucose control.\n"
"3-Regular physical activity: Aim for consistency by making exercise a regular part of your routine. Even shorter bouts of activity throughout the day can be beneficial in managing blood sugar levels.\n"
"4-Blood sugar monitoring: Test your blood sugar before and after exercise initially to understand how your body responds. This can help you make adjustments to your medication or food intake as needed.\n"
"5-Stay hydrated: Drink plenty of water before, during, and after exercise to stay hydrated and maintain optimal bodily functions.")
    print("___________________________________________________________________________________________________________________")

def ExPressure():
    print("\t\t\t\t\t\t\t\tPlz follow these instructions* 'Exercise for pressure disease' \t\t\t\t")
    print("1-Aerobic exercise: Engage in moderate-intensity aerobic activities, such as brisk walking, cycling, swimming, or dancing, for at least 150 minutes per week. This helps lower blood pressure and improve cardiovascular fitness.\n"
"2-Strength training: Include strength training exercises at least two days a week. This can involve using weights, resistance bands, or bodyweight exercises to strengthen your muscles.\n"
"3-Regular physical activity: Strive for consistency by making exercise a regular part of your routine. Aim for daily movement, even if it's in shorter bouts throughout the day.\n"
"4-Monitor exertion levels: Be mindful of your exertion levels during exercise. If you have high blood pressure, consult with your healthcare provider to determine appropriate target heart rate ranges and exercise intensity.\n"
"5-Consult with your healthcare provider: It's important to consult with your healthcare provider before starting or modifying your exercise routine. They can provide specific recommendations based on your condition and any potential exercise restrictions.")
    print("___________________________________________________________________________________________________________________")

def menu(msg, low, high):
    x = float(input(msg))
    c = int(input(chronic))
    ChronicDis(c)

    while x < low or x > high:
        x = float(input('Error! ' + msg))
    else:
        if x == 1 and c ==0:
            print(ExH(weight, height))
        if x == 2 and c ==0 :
            print(DH())
        if x == 3 and c ==0 :
            print(ExH(weight, height))
            print(DH())
        if x == 1 and c == 1:
            print(ExDiabetes())
        if x == 1 and c == 2:
            print(ExPressure())
        if x == 1 and c == 3:
            print(ExHeart())

        if x == 2 and c == 1:
            print(DietDiabetes())
        if x == 2 and c == 2:
            print(DietPressure())
        if x == 2 and c == 3:
            print(DietHeart())
        if x == 3 and c == 1:
            print(ExDiabetes())
            print("---------------------")
            print(DietDiabetes())
        if x == 3 and c == 2:
            print(ExPressure())
            print("---------------------")
            print(DietPressure())
        if x == 3 and c == 3:
            print(ExHeart())
            print("---------------------")
            print(DietHeart())


    return "\t\t\t\t\tPerfect*\t\t\t\t"

def FinalH(x,y):
    BMI(x,y)
    waterIn(weight)
    print(menu(msg,low,high))
    return "Thank you for using our health app*"

weight=int(input("Enter your weight in kilograms="))
height=int(input("Enter your height in centimeters="))
msg= "Please choose what you want ?\nchoose 1 for 'exercise' ,'choose 2 for 'a diet' ,choose 3 for 'both'."
chronic ="Plz, choose if you have any chronic disease: 0 for no disease, 1 for 'Diabetes', 2 for 'Pressure disease', 3 for 'Heart disease'"
low = 1
lowC = 0
high = 3
print(FinalH(weight,height))

