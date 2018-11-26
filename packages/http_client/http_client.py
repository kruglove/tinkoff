import requests


class HttpClient(object):

    def _init_(self):
        self.base_url = 'https://fintech-trading-qa.tinkoff.ru/v1/md'
        self.headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}

    def get_sub(self,request_id,system_code):
        url = self.base_url + '/contacts/e.kruglova/subscriptions?request_id=='+request_id+'&system_code='+system_code
        response = requests.get(url, headers=self.headers)
        return response

    def del_sub(self, request_id, system_code, sub_id):
        url = self.base_url + '/contacts/e.kruglova/subscriptions/'+sub_id+'?request_id==' + request_id + '&system_code=' + system_code
        response = requests.delete(url, headers=self.headers)
        return response



