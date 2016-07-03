#!/usr/bin/python
import re
import urllib2
import copy
import couchdb
import time 
import datetime
import json



def Dyn_Fw():
    """class is used for the addding the status of the ipaddress
    and the return to the some of the class
    """    
    ipaddress_list = {}
    #Flow_data = []
    global Flow_Table
    actionUrl_sp = 'https://www.spamhaus.org/drop/drop.txt'
        #self.html_sp = response_sp.read()
        
	#self.ActionUrl = 'http://data.phishtank.com/data/'
    '4078babbc55da159368a2824a7eb39b423f27199a24b09c7a1c29e78a9eda2a7/online-valid.json'
    Actionurl_ph = 'https://www.spamhaus.org/drop/drop.txt'
    response_ph = urllib2.urlopen(Actionurl_ph)
    html_ph = response_ph.read()
    couch = couchdb.Server()
    try:
        couch.delete('flow_table')
    except:
        print()

    self.Flow_Table = couch.create('flow_table')

       
    def url_spamhaus(self):
        """ this method is used to add the  status
        of the ip address.
        """
        """
        couch = couchdb.Server()
        try:
	    couch.delete('flow_table')
        except:
	    print()

        Flow_Table = couch.create('flow_table')
        """
        response_sp = urllib2.urlopen(self.actionUrl_sp)
        self.html_sp = response_sp.read()
        if self.html_sp.find("Spamhaus"):
            Sourceid = "Spamhaus"
        iplist = re.findall(r'[0-9]+(?:\.[0-9]+){3}',self.html_sp)
        whitelist_Iplist = []
        block_iplist = []
        db_iplist = self.Blst_Wlst()
        if db_iplist:
            whitelist_Iplist.append(list(set(db_iplist)-set(iplist)))
            
	if iplist:
            if db_iplist == None:
                block_iplist=iplist
            else:
                block_iplist.append(list(set(iplist)-set(db_iplist)))
        now_time = datetime.datetime.now()
        flow_time = str(now_time)
        Flow_data = []
        for ip in block_iplist:
	    if ip:
                
                Data = "{'IP' : ip, 'Source': Sourceid, 'TimeStamp':flow_time} "
                Flow_data.append(self.Flow_Table.save(eval(Data)))
        print whitelist_Iplist,block_iplist
        return whitelist_Iplist,block_iplist

    def url_phistank(self):
	#""" this method is used to add the  status
	#of the ip address.
	#"""

        if self.html_ph.find("Phishtank"):
            Sourceid = "Phishtank"
        iplist = re.findall(r'ip_address...[0-9]+(?:\.[0-9]+){3}',self.html_ph)
        db_iplist = Blst_Wlst()
        if db_iplist:
            whitelist_Iplist = list(set(db_iplist)-set(iplist))
	if iplist:
            block_iplist = list(set(iplist)-set(db_list))
        now_time = datetime.datetime.now()
        flow_time = str(now_time)
        Flow_data = []
        for ip in iplist:
	    if ip:
                
                Data = "{'IP' : ip, 'Source': Sourceid, 'TimeStamp':flow_time} "
                Flow_data.append(self.Flow_Table.save(eval(Data)))
        #print Flow_data
        return Flow_data
    def Blst_Wlst(self):
        iplist = []
	for id in obj.Flow_Table:  #  To Display the Content in Database
           dp_table = obj.Flow_Table[id]
           iplist.append(re.findall(r'[0-9]+(?:\.[0-9]+){3}',str(dp_table)))
        #print iplist
         

obj = Dyn_Fw()
obj.url_spamhaus()
#obj.url_phistank()
#obj.Blst_Wlst()



