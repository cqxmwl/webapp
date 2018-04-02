#!/usr/bin/env python
# coding=utf-8

import sys
import orm,asyncio
from models import User,Blog,Comment


async def test(loop,**kw):
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')
    u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'))
    await u.save()
    await orm.destory_pool()

data=dict(name='gaf', email='235123345@qq.com', passwd='1312345', image='about:blank')
loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop,**data))
loop.close()
