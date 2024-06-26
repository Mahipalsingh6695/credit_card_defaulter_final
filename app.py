    
from src.CreditCardDefaulter.pipelines.prediction_pipeline import CustomData,PredictPipeline

from flask import Flask,request,render_template,jsonify


app=Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        data=CustomData(
            
            LIMIT_BAL=float(request.form.get('LIMIT_BAL')),
            SEX=float(request.form.get('SEX')),
            EDUCATION=float(request.form.get('EDUCATION')),
            MARRIAGE=float(request.form.get('MARRIAGE')),
            AGE=float(request.form.get('AGE')),
            PAY_0=float(request.form.get('PAY_0')),
            PAY_2=float(request.form.get('PAY_2')),
            PAY_3=float(request.form.get('PAY_3')),
            PAY_4=float(request.form.get('PAY_4')),
            PAY_5=float(request.form.get('PAY_5')),     
            PAY_6=float(request.form.get('PAY_6')),
            BILL_AMT1=float(request.form.get('BILL_AMT1')),
            BILL_AMT2=float(request.form.get('BILL_AMT2')),
            BILL_AMT3=float(request.form.get('BILL_AMT3')),
            BILL_AMT4=float(request.form.get('BILL_AMT4')),
            BILL_AMT5=float(request.form.get('BILL_AMT5')),
            BILL_AMT6=float(request.form.get('BILL_AMT6')),
            PAY_AMT1=float(request.form.get('PAY_AMT1')),
            PAY_AMT2=float(request.form.get('PAY_AMT2')),
            PAY_AMT3=float(request.form.get('PAY_AMT3')),
            PAY_AMT4=float(request.form.get('PAY_AMT4')),
            PAY_AMT5=float(request.form.get('PAY_AMT5')),
            PAY_AMT6=float(request.form.get('PAY_AMT6'))
           
            
        )
        # this is my final data
        final_data=data.get_data_as_dataframe()
        # print("final data", final_data)
        
        predict_pipeline=PredictPipeline()
        # print("predict_pipeline",predict_pipeline)
        
        pred=predict_pipeline.predict(final_data)
        print("pred",pred)
        
        result = ""
    # print("predition", round(pred))
    if pred == 1:
        result = "The credit card holder will be Defaulter in the next month"
    else:
        result = "The Credit card holder will not be Defaulter in the next month"
        
    return render_template("result.html",final_result=result)

#execution begin
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
