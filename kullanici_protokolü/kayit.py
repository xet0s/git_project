#database eklentisi
from database import MongoDB


userdb=MongoDB(db_name="userlist",collection_name="users")

userlists={}
#kullanici adi kayit
encrypted_password=""

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
        #şifreleme-sezar şifrelemesi       
        for letter in input_password:
            ascii_=ord(letter)
            if chr(ascii_)==" ":
                encrypted_password += chr(ascii_)
            else:
                encrypted_password += chr(ascii_+1)
        

        data={"username":input_username,"password":input_password}
        userlists={"username":input_username,
                   "password":encrypted_password}
        userdb.collection.insert_one(userlists)
        break
    

#şifre kayıt

userdb.close_connection()
