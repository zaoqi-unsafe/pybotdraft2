from typing import List, Callable
class Group(object):
    def __init__(self):
        pass # WIP
class User(object):
    def __init__(self):
        pass # WIP
class Message(object):
    def __init__(self):
        pass # WIP
class Bot(object):
    def __init__(self):
        self.group_message_callbacks = []
        self.private_message_callbacks = []
    def on_group_message(self):
        def do_register(func : Callable[[Group, User, Message], None]):
            self.group_message_callbacks.append(func)
        return do_register
    def _do_on_group_message(self, group : Group, sender : User, message : Message):
        for callback in self.group_message_callbacks:
            callback(group, sender, message)
    def on_private_message(self):
        def do_register(func : Callable[[User, Message], None]):
            self.private_message_callbacks.append(func)
        return do_register
    def _do_on_private_message(self, sender : User, message : Message):
        for callback in self.private_message_callbacks:
            callback(sender, message)
