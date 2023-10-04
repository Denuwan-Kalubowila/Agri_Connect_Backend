def individul_serial(user)->dict:
    return{
        "id":str(user["_id"]),
        "name":user["name"],
        "email":user["email"],
        "age":user["age"],
        "password":user["password"]
    }

def list_serial_list(users)->list:
    return[individul_serial(user) for user in users]