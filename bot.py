class Bot(object):
    def __init__(self):
        self.group_message_callbacks=[]
        self.private_message_callbacks=[]
    def on_group_message(self):
        def do_register(func): # func : Group, Sender, Message -> _
            self.group_message_callbacks.append(func)
        return do_register
    def _do_on_group_message(self, group, sender, message):
        for callback in self.group_message_callbacks:
            callback(group, sender, message)
    def on_private_message(self):
        def do_register(func): # func : Sender, Message -> _
            self.private_message_callbacks.append(func)
        return do_register
    def _do_on_private_message(self, sender, message):
        for callback in self.private_message_callbacks:
            callback(sender, message)
