from util import encryption, HTTPClient
import json

BLOCK_CHAIN_API_URL = "localhost:8081"


def get_block_head_id(userid):
    return encryption.encrypt(str(userid)+"+"+str(userid))


def create_user_initial_block(userid):
    data = dict()
    data['_id'] = get_block_head_id(userid)
    return HTTPClient.post_data("POST", BLOCK_CHAIN_API_URL, data, '/user/insertdata')


def add_user_data(user_data, userid, current_user_id, current_org_id):
    data = dict()
    data['_id'] = get_block_head_id(userid)
    user_data = json.loads(user_data)
    user_data['org_id'] = current_org_id
    user_data['user_id'] = current_user_id
    data['block_data'] = user_data
    return HTTPClient.request_data("PUT", BLOCK_CHAIN_API_URL, data, '/user/insertdata')


def request_data(userid, record_type, st, et):
    data = dict()
    data['_id'] = get_block_head_id(userid)
    data['record_type'] = record_type
    data['st'] = st
    data['et'] = et
    return HTTPClient.request_data("PUT", BLOCK_CHAIN_API_URL, data, '/user/insertdata')