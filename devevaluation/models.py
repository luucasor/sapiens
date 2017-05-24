# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Notification(models.Model):
    def __init__(self, people):
        self.__name_receiver = people.getName()
        self.__mail_receiver = people.getMail()

        self.__sentFrontEnd = False
        self.__sentBackEnd = False
        self.__sentMobile = False
        self.__sentGeneral = False

        self.sendMail(people)

    def sendMail(self, people):
        if people.isFrontEnd():
            self.__sentFrontEnd = self.sendMailFrontEnd()
        if people.isBackEnd() :
            self.__sentBackEnd = self.sendMailBackEnd()
        if people.isMobile()  :
            self.__sentMobile = self.sendMailMobile()
        if people.isGeneral() :
            self.__sentGeneral = self.sendMailGeneral()

    def sendMailFrontEnd(self):
        return True

    def sendMailBackEnd(self):
        return True

    def sendMailMobile(self):
        return True

    def sendMailGeneral(self):
        return True

    def isSentFrontEnd(self):
         return self.__sentFrontEnd

    def isSentBackEnd(self):
         return self.__sentBackEnd

    def isSentMobile(self):
         return self.__sentMobile

    def isSentGeneral(self):
         return self.__sentGeneral

class People(models.Model):
    def __init__(self, name, mail):
        self.__name = name
        self.__mail = mail
        self.__skills = {"html":0, "css":0, "javascript":0, "python":0, "django":0, "ios":0, "android":0}
        self.__backend = False
        self.__frontend = False
        self.__mobile = False
        self.__general = True

    def evaluation(self):
        if ((self.getSkill('python') + self.getSkill('django')) / 2) >= 7:
            self.__backend = True

        if ((self.getSkill('html') + self.getSkill('css') + self.getSkill('javascript')) / 3) >= 7:
            self.__frontend = True

        if ((self.getSkill('ios') + self.getSkill('android')) / 2) >= 7:
            self.__mobile = True

        if self.__backend or self.__frontend or self.__mobile:
            self.__general = False

        Notification(self)

    def setSkill(self, key, value):
        self.__skills[key] = value

    def getSkill(self, key):
         return self.__skills[key]

    def getName(self):
         return self.__name

    def getMail(self):
         return self.__mail

    def isFrontEnd(self):
         return self.__frontend

    def isBackEnd(self):
         return self.__backend

    def isMobile(self):
         return self.__mobile

    def isGeneral(self):
         return self.__general
