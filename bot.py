from typing import List, Callable
class Group:
    def __init__(self):
        pass # WIP
class User:
    def __init__(self):
        pass # WIP
class Message:
    def __init__(self):
        pass # WIP
class Bot:
    def __init__(self):
        self.group_message_callbacks : List[Callable[[Group, User, Message]] =  []
        self.private_message_callbacks : List[Callable[[User, Message]] = []
    def on_group_message(self):
        def do_register(func : Callable[[Group, User, Message], None]) -> None:
            self.group_message_callbacks.append(func)
        return do_register
    def _do_on_group_message(self, group : Group, sender : User, message : Message) -> None:
        for callback in self.group_message_callbacks:
            callback(group, sender, message)
    def on_private_message(self):
        def do_register(func : Callable[[User, Message], None]):
            self.private_message_callbacks.append(func)
        return do_register
    def _do_on_private_message(self, sender : User, message : Message) -> None:
        for callback in self.private_message_callbacks:
            callback(sender, message)
    def send_group_message(self, group : Group, message : Message) -> None:
        pass
    def send_private_message(self, user : User, message : Message) -> None:
        pass
    
