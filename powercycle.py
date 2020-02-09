import os
import datetime
import time

PlugIP = '192.168.0.211'
PlugToken = '2987f0fd0ad1517415cab085099a9a23'
DutIP = '192.168.68.1'
TestCount = 100

def OnOffPlug(OnOrOff):
    OnOffResult = os.popen('sudo miplug --ip %s --token %s %s'%(PlugIP,PlugToken,OnOrOff)).readlines()
    return OnOffResult

def MyPing(IP):
    if(os.system('ping -c 4 %s'%DutIP)==0):
        print('Ping OK ')
        return 0
    else:
        print('Ping Not OK!')
        return -1
if __name__=="__main__":
    #1.Test reboot time
    OnOffPlug('off')
    OnOffPlug('on')
    starttime = datetime.datetime.now()
    while MyPing(DutIP) == -1:
        continue
    endtime = datetime.datetime.now()
    RebootTime = (endtime - starttime).seconds
    print('Totally need %d seconds to reboot'%(RebootTime))
    
    #2.Do the Powercycle
    for icount in range(TestCount):
        icount += 1
        print('--------------Doing Powercycle: %d/100--------------'%icount)
        OnOffPlug('off')
        OnOffPlug('on')
        time.sleep(RebootTime)
        starttime = datetime.datetime.now()
        #allow fail 5*4 times
        for i in range(5):
            if MyPing(DutIP) == 0:
                break
        else:
            print('--------------Fail when: %d/100--------------'%icount)
            exit(0)
        endtime = datetime.datetime.now()
        print('--------------Complete Powercycle: %d/100--------------'%icount)    
