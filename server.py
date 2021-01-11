from flask import Flask, render_template, request, redirect, url_for
import csv, mysql.connector
from twilio.rest import Client
app = Flask(__name__)



 
account_sid = 'AC1a12907b714663c20b1fc6ba2155e8f9' 
auth_token = '1ad5334f13a1cbca99e922fe3cc29702' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(         
							  from_='+12513188064',  
                              body='Hello',  
                              to='+351919881259' 
                          ) 
 
print(message.sid)


## DATABASE ##



mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="password123",
		database="testdb"
	)

mycursor = mydb.cursor(buffered=True)



sql_insert_formula = "INSERT INTO stores (store_name, store_description, store_status, box, sold_boxes) VALUES (%s, %s, %s, %s, %s)"
sql_select_formula = "SELECT * FROM stores"
sql_delete_formula = "DELETE FROM stores WHERE store_name='Lanchonete Lebron'"


store1 = ("Lanchonete Lebron", "grande loja", "activa", 1, 0)
store2 = ("Mercearia", "péssimo", "activa", 1, 0)

mycursor.execute(sql_select_formula)
result = mycursor.fetchone()

# for x in result:
# 	if x == 22:
# 		store_id = result[2]
# 		print(store_id)

#mydb.commit()





	

 ## DATABASE ##
@app.route('/work.html')
def fds(result):
    return render_template("work.html", render_template("work.html", store_name = result[1], store_description = result[2], store_status = result[3], number_of_boxes = result[4]))

@app.route('/<string:page_name>')
def components(page_name):
    return render_template(page_name, title=page_name)
    
@app.route('/reservation_form', methods=["POST"])
def reservation():
	if request.method == "POST":
		phone = request.form["phone"]
		account_sid = 'AC1a12907b714663c20b1fc6ba2155e8f9' 
		auth_token = '1ad5334f13a1cbca99e922fe3cc29702' 
		client = Client(account_sid, auth_token)
		message = client.messages.create(         
							  from_='+12513188064',  
                              body='Parabens pela compra da Caixa Surpresa. O teu código é o 456-234',  
                              to=phone 
                          ) 
		print(message.sid)
		return render_template("reservado.html")
    

@app.route('/work/<int:store_id>')
def stores(store_id):
        #select_query = "SELECT * FROM stores"
        mycursor.execute("SELECT * FROM stores WHERE store_id = %s" % store_id)
        result = mycursor.fetchone()
        print(result)
        return render_template("work.html", store_name = result[1], store_description = result[2], store_status = result[3], number_of_boxes = result[4])
 
        
#ISTO é o route que usei com <form> em vez de href
# @app.route('/<int:store_id>', methods=["POST"])
# def stores1(store_id):
#     if request.method == "POST":
#         #select_query = "SELECT * FROM stores"
#         mycursor.execute("SELECT * FROM stores WHERE store_id = %s" % store_id)
#         result = mycursor.fetchone()
#         print(result)
#         return render_template("work.html", store_name = result[1], store_description = result[2], store_status = result[3], number_of_boxes = result[4])







# @app.route('/submit_form', methods=["POST", "GET"])
# def submit_form():
#     if request.method == "POST":
#     	data = request.form.to_dict()
#     	write_to_csv(data)
#     	return redirect("thankyou.html")
#     else:
#     	return "failed"
 
# def write_to_file_json(data): #JSON Format
# 	with open("database.txt", "a") as database:
# 		database.write(json.dumps(data))

# def write_to_file(data): #Desfazendo o dict e append os valores em separado
# 	with open("database.txt", "a") as database:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		database.write(f"\n{email}, {subject}, {message}")

# def write_to_csv(data): #Desfazendo o dict e append os valores em separado
# 	with open("database.csv", "a", newline='') as database_csv:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# 		csv_writer.writerow([email, subject, message])













# if __name__ == "__main__":
#     app.run()
