from Pos import Pos
import pygame

class Life():
    def __init__(self, pos:Pos):
        self._name = 'Life'
        self._color = (0,0,0,255)
        self._pos = pos

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def pos(self):
        return self._pos

    @property
    def col(self):
        return self._pos.col
    
    @property
    def row(self):
        return self._pos.row

    def __str__(self):
        return f"[Name:{self._name}, Pos:{self._pos}]"

