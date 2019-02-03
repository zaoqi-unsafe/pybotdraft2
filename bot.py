class Bot(object):
    def __init__(self):
        self.group_message_callbacks=[]
        self.private_message_callbacks=[]
    def on_group_message(self):
        def do_register(func): # func : Group, Message -> _
            self.group_message_callbacks.append(func)
        return do_register
    def on_private_message(self):
        def do_register(func): # func : Message -> _
            self.private_message_callbacks.append(func)
        return do_register
