import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

@dataclass(frozen=True)
class Node:
    value: Any
    left: Optional["Node"]
    right: Optional["Node"]

BinTree = Optional[Node]

@dataclass(frozen=True)
class frozenBinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree

def is_empty(tree: BinTree) -> bool:
    return tree is None

def insert(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
    match tree:
        case None:
            return Node(value, None, None)
        case Node(v, left, right):
            if comes_before(value, v):
                return Node(v, insert(left, value, comes_before), right)
            else:
                return Node(v, left, insert(right, value, comes_before))

def lookup(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> bool:
    match tree:
        case None:
            return False
        case Node(v, left, right):
            if not comes_before(value, v) and not comes_before(v, value):
                return True
            elif comes_before(value, v):
                return lookup(left, value, comes_before)
            else:
                return lookup(right, value, comes_before)

def delete(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
    match tree:
        case None:
            return None
        case Node(v, left, right):
            if not comes_before(value, v) and not comes_before(v, value):
                match (left, right):
                    case (None, _):
                        return right
                    case (_, None):
                        return left
                    case (_, _):
                        successor = right
                        while successor.left:
                            successor = successor.left
                        return Node(successor.value, left, delete(right, successor.value, comes_before))
            elif comes_before(value, v):
                return Node(v, delete(left, value, comes_before), right)
            else:
                return Node(v, left, delete(right, value, comes_before))


def example_fun(x : int) -> bool:
    return x < 142
