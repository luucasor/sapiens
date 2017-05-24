# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from devevaluation.models import People, Notification

# Create your tests here.
class ScoreTestCase(TestCase):

    def setUp(self):
        self.people = People(name="Joao", mail="mail@gmail.com")

    def test_score_frontend(self):
        joao = self.people
        joao.setSkill('html', 7)
        joao.setSkill('css', 7)
        joao.setSkill('javascript', 7)
        joao.evaluation()
        self.assertEqual(joao.isFrontEnd(), True)

    def test_score_backend(self):
        joao = self.people
        joao.setSkill('python', 7)
        joao.setSkill('django', 7)
        joao.evaluation()
        self.assertEqual(joao.isBackEnd(), True)

    def test_score_mobile(self):
        joao = self.people
        joao.setSkill('ios', 7)
        joao.setSkill('android', 7)
        joao.evaluation()
        self.assertEqual(joao.isMobile(), True)

    def test_score_general(self):
        joao = self.people
        joao.evaluation()
        self.assertEqual(joao.isGeneral(), True)

class notificationTestCase(TestCase):

    def setUp(self):
        self.people = People(name="Joao", mail="mail@gmail.com")

    def test_sendMail_frontend(self):
        joao = self.people
        joao.setSkill('html', 7)
        joao.setSkill('css', 7)
        joao.setSkill('javascript', 7)
        joao.evaluation()
        notification = Notification(joao)
        self.assertEqual(notification.isSentFrontEnd(), True)

    def test_score_backend(self):
        joao = self.people
        joao.setSkill('python', 7)
        joao.setSkill('django', 7)
        joao.evaluation()
        notification = Notification(joao)
        self.assertEqual(notification.isSentBackEnd(), True)

    def test_score_mobile(self):
        joao = self.people
        joao.setSkill('ios', 7)
        joao.setSkill('android', 7)
        joao.evaluation()
        notification = Notification(joao)
        self.assertEqual(notification.isSentMobile(), True)

    def test_score_general(self):
        joao = self.people
        joao.evaluation()
        notification = Notification(joao)
        self.assertEqual(notification.isSentGeneral(), True)
