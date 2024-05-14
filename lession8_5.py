## import pyinputplus as pyip

def cal_bmi(height:float|int,weight:float|int)->float:                   
        bmi = weight / (height / 100) ** 2
        return round(bmi,ndigits=2)


def get_status(bmi:float|int)->str:
        if bmi < 18.5:
            return("體重過輕")
        elif bmi <24:
            return("體重正常")
        elif bmi < 27:
            return("體重過重")
        elif bmi < 30:
            return("輕度肥胖")    
        elif bmi < 35:
            return("中度肥胖") 
        elif bmi >=35 :
            return("重度肥胖")

import pyinputplus as pyip 

name =  pyip.inputStr("請輸入姓名:")
h_val= pyip.inputFloat('請輸入身高(120~230)(cm):',lessThan=230,greaterThan=120) 
w_val = pyip.inputFloat('請輸入體重(40~170)(kg):',lessThan=170,greaterThan=40)
cur_bmi=cal_bmi(weight = w_val, height=h_val )
cur_state = get_status(cur_bmi)

print(f'{name}, 您的BMI: {cur_bmi} , 你目前 {cur_state}')


        
