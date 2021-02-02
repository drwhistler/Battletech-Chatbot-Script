

import os
import sys
import clr
import time
import random
import datetime
import shutil
import threading

clr.AddReference('IronPython.SQLite.dll')
clr.AddReference('IronPython.Modules.dll')

#---------------------------------------
# [Required] Script Information
#---------------------------------------
ScriptName = 'Battletech'
Website = 'https://www.StreamlabsChatbot.com'
Description = 'Battletech Twitch Commands'
Creator = 'DrWhistler'
Version = '1.0.0.0'

#---------------------------------------
# Set Variables
#---------------------------------------
m_Response = 'This is a test message'
m_Command = ''
m_CooldownSeconds = 120
m_CommandPermission = 'Everyone'
m_CommandInfo = ''

userId=""

def Init():
 global m_Response
 m_Response = '' 
 return

def Execute(data):

    global userId
    userId = data.User.lower()

    if data.IsChatMessage():

        if data.GetParam(0).lower() == '!btlance' and not Parent.IsOnCooldown(ScriptName,m_Command) and Parent.HasPermission(data.User,m_CommandPermission,m_CommandInfo):
            
            #read Lance.txt
            with open('C:\\Users\\Jason\\AppData\\Roaming\\AnkhHeart\\AnkhBotR2\\Services\\Scripts\\Battletech\\Lance.txt','r') as file:
                mech1 = file.readline().replace('\n','')
                file.readline().replace('\n','')
                mech2 = file.readline().replace('\n','')
                file.readline().replace('\n','')
                mech3 = file.readline().replace('\n','')
                file.readline().replace('\n','')
                mech4 = file.readline().replace('\n','')

            #write to lance2.txt
            #with open('C:\\Users\\Jason\\AppData\\Roaming\\AnkhHeart\\AnkhBotR2\\Services\\Scripts\\Battletech\\lance2.txt','w') as file:
            #    file.writelines(str(mech1+'\n\n'))
            #    file.writelines(str(mech2+'\n\n'))
            #    file.writelines(str(mech3+'\n\n'))
            #    file.writelines(str(mech4))

            Parent.SendTwitchMessage('DEPLOYMENT - ' + mech1 + ", " + mech2 + ", " + mech3 + ", " + mech4)

        if data.GetParam(0).lower() == '!btmission' and not Parent.IsOnCooldown(ScriptName,m_Command) and Parent.HasPermission(data.User,m_CommandPermission,m_CommandInfo):
            
            #read Mission.txt
            with open('C:\\Users\\Jason\\AppData\\Roaming\\AnkhHeart\\AnkhBotR2\\Services\\Scripts\\Battletech\\Mission.txt','r') as file:
                location = file.readline().replace('\n','')
                file.readline().replace('\n','')
                contractName = file.readline().replace('\n','')
                file.readline().replace('\n','')
                contractType = file.readline().replace('\n','')
                file.readline().replace('\n','')
                biome = file.readline().replace('\n','')
                file.readline().replace('\n','')
                difficulty = file.readline().replace('\n','')

            #write to mission2.txt
            #with open('C:\\Users\\Jason\\AppData\\Roaming\\AnkhHeart\\AnkhBotR2\\Services\\Scripts\\Battletech\\mission2.txt','w') as file:
            #    file.writelines(str(location+'\n\n'))
            #    file.writelines(str(contractName+'\n\n'))
            #    file.writelines(str(contractType+'\n\n'))
            #    file.writelines(str(biome+'\n\n'))
            #    file.writelines(str(difficulty))

            Parent.SendTwitchMessage('MISSION - ' + location + " | " + contractName + " | " + contractType + " | " + biome + " | " + difficulty)

    return

def Tick():
    return

