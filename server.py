from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import flash
from flask import session


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# ask for user name
@app.route('/', methods = ['GET', 'POST'])
def index():
    message=""
  
    # setting a global var for balance
    session['balance'] = 100
    session['credit']=300
    session['chequing']=0
    session['savings']=0
    session['debit']=session['chequing']+session['savings']
    
    if request.method == 'POST':
      
        session['name'] = request.form.get('name')
        
        return redirect(url_for('result', name=session['name'], message=message))
    return render_template('index.html')

  
# to get the user name
@app.route('/result')
def result():
    message=""
    session['name'] = request.args.get('name', None)
#      pass the balance
    return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
  
  
# To redirect the user based on the options they chose
@app.route('/shopping', methods=['GET'])
def shopping():
  return render_template("shop.html")
           
@app.route('/bank', methods=['GET'])
def bank():
  return render_template("bank.html")

@app.route('/job', methods=['GET'])
def job():
  return render_template("job.html")

@app.route('/creditcard', methods=['GET'])
def creditcard():
  return render_template("creditcard.html",owe=300-session['credit'])    

@app.route('/savings', methods=['GET'])
def savings():
  return render_template("savings.html",chequing=session['chequing'],savings=session['savings'])    




# User's Choice to Shop
@app.route('/result', methods=['GET','POST'])
def shopper():
  message =""
  
  if request.method == 'POST' and len(dict(request.form)) > 0:
    userdata = dict(request.form)
    print(userdata)
    shop = userdata["shop"][0]
    myPay = request.form.get("m")

    # If they click on cash button
    if myPay=="Cash":

        # Based on the different radio type they chose
        if shop == "20":
          if session['balance']<90:
            message= "you did not have enough cash."
            return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
          else:
            session['balance'] -= 90   
            return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

        elif shop == "15":
          if session['balance']<15:
            message= "you did not have enough cash."
            return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
          else:
            session['balance'] -= 15   
            return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

        elif shop == "25":
          if session['balance']<25:
            message= "you did not have enough cash."
            return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
          else:
            session['balance'] -= 25   
            return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

        elif shop == "1200":
          if session['balance']<1200:
            message= "you did not have enough cash."
            return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
          else:
            session['balance'] -= 1200   
            return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

  #  else:
   #   return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

  # If they clicked on the debit button
  elif myPay=="Debit Card":

      # Based on the radio type they chose
      if shop == "20":
        if session['chequing']<20:
          message= "you did not have enough money."
          return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
        else:
          session['chequing'] -= 20   
          return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

      elif shop == "15":
        if session['chequing']<15:
          message= "you did not have enough money."
          return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
        else:
          session['chequing'] -= 15   
          return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

      elif shop == "25":
        if session['chequing']<25:
          message= "you did not have enough money."
          return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
        else:
          session['chequing'] -= 25   
          return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

      elif shop == "1200":
        if session['chequing']<1200:
          message= "you did not have enough money."
          return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
        else:
          session['chequing'] -= 1200   
          return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

      else:
        return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

  # If they chose the credit option
  elif myPay=="Credit Card":

   # Based on the radio type they chose
    if shop == "20":
      if session['credit']<20:
        message= "you did not have enough limit."
        return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
      else:
        session['credit'] -= 20   
        return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

    elif shop == "15":
      if session['credit']<15:
        message= "you did not have enough limit."
        return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
      else:
        session['credit'] -= 15   
        return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

    elif shop == "25":
      if session['credit']<25:
        message= "you did not have enough limit."
        return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
      else:
        session['credit'] -= 25   
        return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

    elif shop == "1200":
      if session['credit']<1200:
        message= "you did not have enough limit."
        return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
    else:
      session['credit'] -= 1200   
      return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

  else:
   return render_template ('result.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 


  
#   User's choice to work
@app.route('/result2', methods=['GET','POST'])
def worker():
  message =""

  if request.method == 'POST' and len(dict(request.form)) > 0:
    userdata = dict(request.form)
    print(userdata)
    job = userdata["job"][0]
  
  if job == "10":
    session['balance'] += 10   
    return render_template ('result2.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

  elif job == "25":
    session['balance'] += 25   
    return render_template ('result2.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

  elif job == "35":
    session['balance'] += 35   
    return render_template ('result2.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

  elif job == "12":
    session['balance'] += 15   
    return render_template ('result2.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

  else:
    return render_template ('result2.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
  
# User Choice to Chequing / Savings
@app.route('/result3', methods=['GET', 'POST'])
def debit():
  message =""

  try:
    session['amount'] = request.form.get('amount')
    session['amount']= float(session['amount'])
    
    if request.method == 'POST' and len(dict(request.form)) > 0:
      userdata = dict(request.form)
      print(userdata)
      savings = userdata["savings"][0]

    if savings == "chequing":
      if session['balance']<session['amount']:
        message = "You do not have enough money"
        return render_template ('result3.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

      else:
        session['chequing'] += session['amount']   
        session['debit']=session['chequing']+session['savings']
        session['balance']-= session['amount']
        return render_template ('result3.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

    elif savings == "savings":
      if session['balance']<session['amount']:
        message="You do not have enough money"
        return render_template ('result3.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 
      else:
        session['savings'] += session['amount']  
        session['debit']=session['chequing']+session['savings']
        session['balance']-= session['amount']
        return render_template ('result3.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 


  except ValueError :
    message="Please enter a number!"
    return render_template ('result3.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 


  
    
# User Choice to Credit Card
@app.route('/result4', methods=['POST'])
def credit():
  message =""

  try:
    session['pay'] = request.form.get('pay')
    session['pay']= float(session['pay'])
    
    if request.method == 'POST' and len(dict(request.form)) > 0:
      userdata = dict(request.form)
      print(userdata)
      agree = userdata["agree"][0]

    if savings == "agree":
      if session['balance']<session['pay']:
        message = "You do not have enough money to pay"
        return render_template ('result4.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

      else:
        session['credit'] += session['pay']   
        session['debit']=session['chequing']+session['savings']
        session['balance']-= session['pay']
        return render_template ('result4.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 

  except ValueError :
    message="Please enter a number!"
    return render_template ('result4.html', name=session['name'], balance=session['balance'], message=message, savings=session['savings'], chequing=session['chequing'],credit=session['credit'],debit=session['debit']) 


if __name__ == '__main__':
    app.run(debug=True)
