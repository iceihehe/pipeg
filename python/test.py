#!/usr/bin/env python
# -*- coding=utf-8 -*-

import Qtrac
import abc


@Qtrac.has_methods('haha')
class A(object):

    __metaclass__ = abc.ABCMeta


class B(object):
    def haha(self):
        pass


print(isinstance(B(), A))
