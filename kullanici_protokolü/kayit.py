#database eklentisi
from database import MongoDB
userdb=MongoDB(db_name="userlist",collection_name="users")

userlists={}
#kullanici adi kayit

while True:
    input_username=input("Kullanıcı adı belirleyiniz : ")
    input_username=str(input_username.strip())#Whitespace temizlemea
    input_username=str(input_username.lower())#harf hassasiyetini kaldırma
    value=userdb.collection.find_one({"username":input_username})
    if input_username in str(value) :
        print("Kullanıcı adı zaten kayıtlı ")
        break
    else:
        input_password=input("Şifre belirleyiniz : ")
        input_password=str(input_password.strip())#Whitespace temizleme
    
        data={"username":input_username,"password":input_password}
    
        userlists={"username":input_username,
                   "password":input_password}
        userdb.collection.insert_one(userlists)
        break
    

#şifre kayıt

userdb.close_connection()
