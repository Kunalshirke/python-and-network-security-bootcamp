import hashlib
n=input("Enter any string:")


result = hashlib.md5(n.encode("utf-8")).hexdigest()
print("MD5 ENCRYPTION :",result)