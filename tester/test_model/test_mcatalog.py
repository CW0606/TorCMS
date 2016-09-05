# -*- coding:utf-8 -*-

from torcms.core import tools
from torcms.model.mcatalog import MCatalog
import tornado.escape


class TestCatalog():
    def setup(self):
        print('setup 方法执行于本类中每条用例之前')
        self.uu = MCatalog()
        self.uid = tools.get_uu4d()
        self.slug = 'ccc'

    def test_insert(self):
        uid = self.uid
        post_data = {
            'name': 'titlesdf',
            'slug':self.slug,
            'order':'1',

        }

        newid=self.uu.insert_data(uid,post_data)

        tt = self.uu.get_by_slug(self.slug)
        #assert tt == newid



    def test_insert_2(self):
        '''Wiki insert: Test invalid title'''
        post_data = {
            'name': [''],
            'slug':['asa'],
            'order':['2'],
        }
        uu = self.uu.insert_data(self.uid,post_data)
        #assert uu == False

        post_data = {
           'name':[ 'f'],
           'slug':[self.uid],
           'order':['3'],
        }
        uu = self.uu.insert_data(self.uid,post_data)
        #assert uu == False



    def test_upate(self):
        assert True

    def tearDown(self):
        print("function teardown")
        tt = self.uu.get_by_slug(self.slug)
        self.uu.delete(self.uid)
