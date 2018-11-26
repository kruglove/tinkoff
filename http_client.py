import requests
import json

class HttpClient(object):

    def _init_(self):
        self.base_url = 'https://fintech-trading-qa.tinkoff.ru/v1/md'
        self.headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}

    def get_sub(self,request_id,system_code, siebel_id):
        url = self.base_url + '/contacts/' + siebel_id+'/subscriptions?request_id=='+request_id+'&system_code='+system_code
        response = requests.get(url, headers=self.headers)
        return response

    def del_sub(self, request_id, system_code, subscription_id, siebel_id ):
        url = self.base_url + '/contacts/' + siebel_id+ '/subscriptions/'+subscription_id +'?request_id==' + request_id + '&system_code=' + system_code
        response = requests.delete(url, headers=self.headers)
        return response

    def post_sub(self, request_id, system_code, instrument_id, sec_name, sec_type, price_alert, siebel_id):
        url = self.base_url + "contacts/" + siebel_id + "/subscriptions?request_id=" + request_id + "&system_code=" + system_code
        head = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh', 'Content-type': 'application/json'}
        data = {"body": [{"instrument_id": instrument_id, "sec_name": sec_name, "sec_type": sec_type,
                                                                                        "price_alert": price_alert}]}
        return requests.post(url, json=json.dumps(data), headers=head)



