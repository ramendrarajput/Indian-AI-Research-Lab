"""
Base Retrieval Augmented Generation class.
"""

from abc import ABC, abstractmethod


class BaseRAG(ABC):

    @abstractmethod
    def ingest(self, source):
        """
        Index documents.
        """
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, query):
        """
        Retrieve relevant chunks.
        """
        raise NotImplementedError

    @abstractmethod
    def ask(self, query):
        """
        Generate final answer.
        """
        raise NotImplementedError