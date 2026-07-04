from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """
    Base class for every Agent in Project BRAHMA.
    """

    def __init__(self, name: str):

        self.name = name

    @abstractmethod
    def run(self, query: str):
        """
        Execute agent logic.

        Args:
            query: User query

        Returns:
            Agent response
        """
        pass
        #raise NotImplementedError