from whalealert.whalealert import WhaleAlert
import time
from queue import Queue
from auth import WHALE_API_KEY

class Whale:
    '''Class to define the API connection , retrieve all transaction from the last 10 minutes and select only the ones with a predifined value'''
    WHALE=WhaleAlert()
    API_KEY=WHALE_API_KEY



    def get_transactions(self):
        initial_time=int(time.time()-600)
        succes,trans,status=self.WHALE.get_transactions(start_time=initial_time,api_key=self.API_KEY)
        time.sleep(10)

        return trans

    def process_transactions(self,twiter_instance):
        transaction_queue=Queue()
        list_trans=self.get_transactions()

        for tran in list_trans:
            dict_trans = {}
            if tran['symbol'] in ['BTC'] and tran['amount_usd'] > 20000000:

                dict_trans['coin']=tran['symbol']
                dict_trans['amount']=tran['amount']
                dict_trans['usd_amount']=tran['amount_usd']
                if tran['from']['owner_type'] == 'unknown':
                    dict_trans['from']='Unknown Adress'
                elif tran['from']['owner_type'] == 'exchange':
                    dict_trans['from']=f"{tran['from']['owner'].title()} Exchange"
                else:
                    dict_trans['from']=tran['from']['owner'].title()

                if tran['to']['owner_type'] =='unknown':
                    dict_trans['to']='Unknonw Adress'
                elif tran['to']['owner_type'] == 'exchange':
                    dict_trans['to']=f"{tran['to']['owner'].title()} Exchange"
                else:
                    dict_trans['to']=tran['to']['owner'].title()
            if dict_trans:
                transaction_queue.put(dict_trans)

        while not transaction_queue.empty():
            transaction_to_be_processed=transaction_queue.get()
            try:
                tweeter_text=f"\U0001F6A8 \U0001F6A8 \U0001F6A8 BITCOIN WHALE ALERT: {transaction_to_be_processed['amount']} #BTC ({transaction_to_be_processed['usd_amount']} USD) was just transferred from {transaction_to_be_processed['from']} to {transaction_to_be_processed['to']}"
                twiter_instance.post_tweet(tweeter_text)
            except:
                pass



