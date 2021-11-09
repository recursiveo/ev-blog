from src.MongoConnection import connect_mongo


def insert_mongo(username, password, email):
    ev_trendz = connect_mongo()
    user_obj = ev_trendz['Signup']
    output = user_obj.insert_one({'name': username, 'password': password, 'email': email})
    return output


def search_mongo(data):
    ev_trendz = connect_mongo()
    user_obj = ev_trendz['Signup']
    data = user_obj.find(data).count()
    return data


def fetch_data(data):
    ev_trendz = connect_mongo()
    user_obj = ev_trendz['Signup']
    data = user_obj.find(data)
    return data


def update_data(data, updated_data):
    ev_trendz = connect_mongo()
    user_obj = ev_trendz['Signup']
    print("daataaa", data)
    data = user_obj.update(data, updated_data)
    return True


def delete_data(data):
    ev_trendz = connect_mongo()
    user_obj = ev_trendz['Signup']
    print("daataaa", data)
    data = user_obj.remove(data)
    return data
