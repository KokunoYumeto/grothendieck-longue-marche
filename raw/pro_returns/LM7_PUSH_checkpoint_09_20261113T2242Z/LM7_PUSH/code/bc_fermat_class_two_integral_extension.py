#!/usr/bin/env python3
"""Literal nine-coset F extension in exact doubled-log coordinates."""
from functools import cache
import numpy as np
import bc_fermat_class_two_integral_model as q

def collect_f(word):
    deck=(0,0);signed=[]
    for letter in word:
        nxt=q.f.step(deck,letter)
        edge=q.f.EDGES[deck,letter] if letter>0 else -q.f.EDGES[nxt,-letter]
        if edge:signed.append(edge)
        deck=nxt
    return deck,q.collect_signed(signed)

@cache
def action(deck):
    word=q.f.section(deck)
    columns=np.stack([q.literal(word+w+q.f.inverse_word(word)) for w in q.f.NWORDS],axis=1)
    out=np.zeros((55,55),dtype=np.int64)
    out[:,:10]=columns;out[10:,10:]=q.exterior(columns[:10])
    return out

@cache
def carry(a,b):
    total=tuple((i+j)%3 for i,j in zip(a,b))
    return q.literal(q.f.section(a)+q.f.section(b)+q.f.inverse_word(q.f.section(total)))

class FExtension:
    def __init__(self):self.one=((0,0),q.ZERO.copy())
    @staticmethod
    def mul(g,h):
        a,x=g;b,y=h
        total=tuple((i+j)%3 for i,j in zip(a,b))
        return total,q.multiply(q.multiply(x,action(a)@y),carry(a,b))
    @staticmethod
    def inv(g):
        a,x=g;ai=tuple(-i%3 for i in a)
        return ai,q.multiply(-carry(ai,a),action(ai)@(-x))
    def power(self,g,n):
        if n<0:return self.power(self.inv(g),-n)
        out=self.one
        while n:
            if n%2:out=self.mul(out,g)
            g=self.mul(g,g);n//=2
        return out
    def conj(self,g,h):return self.mul(self.mul(g,h),self.inv(g))
    def comm(self,g,h):return self.mul(self.conj(g,h),self.inv(h))
    @staticmethod
    def word(word):return collect_f(word)

def hall_coordinates(g):
    numerator=g[10:]-g[q.I]*g[q.J]
    assert not np.any(numerator%2)
    return np.r_[g[:10],numerator//2]
