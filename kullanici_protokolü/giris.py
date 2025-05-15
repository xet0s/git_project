from database import MongoDB
#database bağlantısı
userdb=MongoDB(db_name="userlist",collection_name="users")
#kullanıcı adı girişi
input_username=input("Kullanıcı adı girinz : ")
input_username=str(input_username.strip())#whitespace temizleme
input_username=str(input_username.lower())#upper-lower sensivity engelleme
value=userdb.collection.find_one({"username":input_username})   
print(input_username)
print(value)

#kullanıcı adı sorgulama
if str(input_username) in str(value):
    input_password=input("şifre giriniz : ")
    input_password=str(input_password.strip())

    value_2=userdb.collection.find_one({"password":input_password})
    print(value_2)
    #şifre sorgulama
    if str(input_password) in str(value_2):
        print("Kullanici girişi başarılı")
    else:
        print("Şifre yanlış")
else:
    print("kullanici adi bulunamadi")

userdb.close_connection()