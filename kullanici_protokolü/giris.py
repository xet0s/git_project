from database import MongoDB
#database bağlantısı
userdb=MongoDB(db_name="userlist",collection_name="users")
#değişken
encrypted_password=""
#kullanıcı adı girişi
input_username=input("Kullanıcı adı girinz : ")
input_username=str(input_username.strip())#whitespace temizleme
input_username=str(input_username.lower())#upper-lower sensivity engelleme

value=userdb.collection.find_one({"username":input_username})

#kullanıcı adı sorgulama
if input_username in str(value):
    input_password=input("şifre giriniz : ")
    input_password=str(input_password.strip())
    #şifreleme-şifre çözümü
    for letter in input_password:
        ascii_=ord(letter)
        if chr(ascii_)==" ":
            encrypted_password += chr(ascii_)
        else:
            encrypted_password += chr(ascii_+1)
    
    value_2=userdb.collection.find_one({"username":input_username})
    #şifre sorgulama
    if str(encrypted_password) in str(value_2):
        print("Kullanici girişi başarılı")
    else:
        print("Şifre yanlış")
else:
    print("kullanici adi bulunamadi")

userdb.close_connection()