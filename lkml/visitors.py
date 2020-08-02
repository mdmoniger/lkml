from typing import Union
from lkml.tree import (
    ContainerNode,
    BlockNode,
    ListNode,
    PairNode,
    SyntaxToken,
    SyntaxNode,
    Visitor,
)


class BasicVisitor(Visitor):
    @staticmethod
    def _visit(node: Union[SyntaxNode, SyntaxToken]):
        raise NotImplementedError

    def visit_container(self, node: ContainerNode):
        return self._visit(node)

    def visit_block(self, node: BlockNode):
        return self._visit(node)

    def visit_list(self, node: ListNode):
        return self._visit(node)

    def visit_pair(self, node: PairNode):
        return self._visit(node)

    def visit_token(self, token: SyntaxToken):
        return self._visit(token)


class LookMlVisitor(BasicVisitor):
    @staticmethod
    def _visit(node: Union[SyntaxNode, SyntaxToken]) -> str:
        return str(node)