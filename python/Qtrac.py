#!/usr/bin/env python
# -*- coding=utf-8 -*-


def has_methods(*methods):
    def decorator(Base):
        def __subclasshook__(Class, Subclass):
            if Class is Base:
                needed = set(methods)
                for Superclass in Subclass.__mro__:
                    for meth in needed.copy():
                        if meth in Superclass.__dict__:
                            needed.discard(meth)
                    if not needed:
                        return True
            return NotImplemented
        Base.__subclasshook__ = classmethod(__subclasshook__)
        return Base
    return decorator
