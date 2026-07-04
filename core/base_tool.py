from abc import ABC, abstractmethod


class BaseTool(ABC):

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Execute Tool
        """
        #raise NotImplementedError
        pass