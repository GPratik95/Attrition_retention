from flask import Flask, render_template, request
import pandas as pd
import pickle 

app = Flask(__name__)
model = pickle.load(open('rforest_model.pkl', 'rb'))
@app.route('/')

def home():
    #print("hlw1")    
    
    return render_template('codeTest.html')

@app.route('/prediction',methods =['POST'])
def prediction():
    #print("hlw2")    
    sales=0
    accounting=0
    hr=0
    technical =0
    support =0
    management =0
    it=0
    product_mng=0
    marketing = 0
    randD=0 

    if request.method == 'POST':
        """
        satisfaction_level = request.form['satisfaction_level']
        last_evaluation = request.form['last_evaluation']
        number_project = request.form['number_project']
        average_montly_hours = request.form['average_montly_hours']
        time_spend_company = request.form['time_spend_company']
        work_accident = request.form['work_accident']
        promotion_last_5years = request.form['promotion_last_5years']
        """
        department = request.form['department']
        
        randD = 0
        if department == "sales":
            sales = 1
        elif department == "accounting":
            accounting = 1
        elif department == "hr":
            hr = 1
        elif department == "technical":
            technical = 1
        elif department == "support":
            support = 1
        elif department == "management":
            management = 1
        elif department == "it":
            it = 1
        elif department == "product_mng":
            product_mng = 1
        elif department == "marketing":
            marketing = 1
        else:
            randD = 1
        
        Satisfaction_Level = [request.form['satisfaction_level']]
        Last_Evaluation = [request.form['last_evaluation']]
        Number_Of_Projects = [request.form['number_project']]
        Average_Monthly_Hours = [request.form['average_montly_hours']]
        Time_Spend_company = [request.form['time_spend_company']]
        Work_Accident = [request.form['work_accident']]
        Promotion_In_Last_5Years = [request.form['promotion_last_5years']]
        Salary = [request.form['salary']]
        
        pro_var = 0
        avg_mon_hr_var = 0
        salary_var = 0
        st1 = 0
        promotion_var = 0
        cnt = 0
        average_montly_hours = 0
        
        
        final_data = pd.DataFrame({"Satisfaction_Level":Satisfaction_Level, "Last_Evaluation":Last_Evaluation, \
          "Number_Of_Projects": Number_Of_Projects, "Average_Monthly_Hours": Average_Monthly_Hours, "Time_Spend_company": Time_Spend_company,\
          "Work_Accident":Work_Accident, "Promotion_In_Last_5Years":Promotion_In_Last_5Years, "Salary": Salary, "department_IT":[it], \
          "department_RandD":[randD], "department_accounting":[accounting ],"department_hr":[hr], "department_management":[management], "department_marketing":[marketing], \
          "department_product_mng":[product_mng], "department_sales":[sales], "department_support":[support], "department_technical":[technical] })

        for i in range(5):
             
            final_data = pd.DataFrame({"Satisfaction_Level":Satisfaction_Level, "Last_Evaluation":Last_Evaluation, \
          "Number_Of_Projects": [int(Number_Of_Projects[0]) + pro_var], "Average_Monthly_Hours": Average_Monthly_Hours, "Time_Spend_company": Time_Spend_company,\
          "Work_Accident":Work_Accident, "Promotion_In_Last_5Years": [int(Promotion_In_Last_5Years[0]) + pro_var], "Salary": [int(Salary[0]) + salary_var], "department_IT":[it], \
          "department_RandD":[randD], "department_accounting":[accounting ],"department_hr":[hr], "department_management":[management], "department_marketing":[marketing], \
          "department_product_mng":[product_mng], "department_sales":[sales], "department_support":[support], "department_technical":[technical] })
            
            if int(Number_Of_Projects[0]) < 7:
                pro_var = pro_var+1
        
            if i > 3:
                if average_montly_hours[0] < 220:
                    avg_mon_hr_var = avg_mon_hr_var + 30
                elif average_montly_hours[0] > 280:
                    avg_mon_hr_var = avg_mon_hr_var - 40
        
            if int(Salary[0]) < 3:
                salary_var = salary_var + 1
            
            if i >=4:   
                if int(Promotion_In_Last_5Years[0]) == 0:
                    cnt = cnt + 1
                    pro_var = 1
            
            
            
            predi = model.predict(final_data)
            print(predi)        
            if predi==0:
                status=" Employee will stay in the organisation."
                if i > 0:
                    status=" Employee might leave the organisation."
                    strategy1 ="salary increased "
                    strategy2 = 'new project given increased !'
                    strategy = 2
                elif i > 3:
                    status=" Employee might leave the organisation."
                    strategy1 ="salary increased and new project given increased"
                    strategy2 = 'change working hrs to : '+avg_mon_hr_var
                      
                else:
                    strategy = "Not Required"
                break;
            elif predi==1:
                status=" Employee might leave the organisation."
           
        return render_template('codeTest.html',Dep=department,prediction_text = status, retention_text = strategy, suggestion1_text = strategy1,suggestion2_text = strategy2, Satisfaction_Level=request.form['satisfaction_level'],last_evaluation = request.form['last_evaluation'],number_project = request.form['number_project'],average_montly_hours = request.form['average_montly_hours'],time_spend_company = request.form['time_spend_company'],work_accident = request.form['work_accident'],promotion_last_5years = request.form['promotion_last_5years'],salary = "Salary")
    return render_template('codeTest.html')
        
if __name__ == "__main__":
    app.run(debug=True)