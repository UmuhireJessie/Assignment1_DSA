from abc import ABCMeta, abstractmethod


class ListOperation(object):
    __metaclass__ = ABCMeta

    def __init__(self, list_, item):
        self.list_ = list_
        self.item = item

    @abstractmethod
    def __call__(self):
        return

    @abstractmethod
    def undo(self):
        return


class Insert(ListOperation):
    def __call__(self):
        self.list_.append(self.item)
        self.list_.sort()

    def undo(self):
        self.list_.remove(self.item)
        self.list_.sort()


class Delete(ListOperation):
    def __call__(self):
        self.deleted = False
        if self.item in self.list_:
            self.list_.remove(self.item)
            self.list_.sort()
            self.deleted = True

    def undo(self):
        if self.deleted:
            self.list_.append(self.item)
            self.list_.sort()


class UndoableList(object):
    def __init__(self):
        self.undo_commands = []
        self.redo_commands = []

    def push_undo_command(self, command):
        """Push the given command to the undo command stack."""
        self.undo_commands.append(command)

    def pop_undo_command(self):
        """Remove the last command from the undo command stack and return it.
        If the command stack is empty, EmptyCommandStackError is raised.

        """
        try:
            last_undo_command = self.undo_commands.pop()
        except IndexError:
            return "Nothing to undo"
        return last_undo_command

    def push_redo_command(self, command):
        """Push the given command to the redo command stack."""
        self.redo_commands.append(command)

    def pop_redo_command(self):
        """Remove the last command from the redo command stack and return it.
        If the command stack is empty, EmptyCommandStackError is raised.

        """
        try:
            last_redo_command = self.redo_commands.pop()
        except IndexError:
            return "Nothing to redo"

        return last_redo_command

    def do(self, command):
        """Execute the given command. Exceptions raised from the command are
        not catched.

        """
        command()
        self.push_undo_command(command)
        # clear the redo stack when a new command was executed
        self.redo_commands[:] = []

    def undo(self):
        """Undo the last n commands. The default is to undo only the last
        command. If there is no command that can be undone because n is too big
        or because no command has been emitted yet, EmptyCommandStackError is
        raised.

        """
        if len(self.undo_commands) != 0:
            command = self.pop_undo_command()
            command.undo()
            self.push_redo_command(command)
        else:
            print('Nothing to undo')

    def redo(self):
        """Redo the last n commands which have been undone using the undo
        method. The default is to redo only the last command which has been
        undone using the undo method. If there is no command that can be redone
        because n is too big or because no command has been undone yet,
        EmptyCommandStackError is raised.

        """
        if len(self.redo_commands) != 0:
            command = self.pop_redo_command()
            command()
            self.push_undo_command(command)
        else:
            print('Nothing to redo')


""" Testing using an example from the question """

my_List = [2, 5, 7]
print(f'\nMy_List: {my_List}\n')
L = UndoableList()

L.do(Insert(my_List, 6))
print(f'After insert(6): {my_List}\n')

L.do(Delete(my_List, 5))
print(f'After delete(5): {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.redo()
print(f'After redo: {my_List}\n')

L.do(Insert(my_List, 4))
print(f'After insert(4): {my_List}\n')

L.redo()
print(f'After redo: {my_List}\n')

L.do(Delete(my_List, 3))
print(f'After delete(3): {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.undo()
print(f'After undo: {my_List}\n')

L.redo()
print(f'After redo: {my_List}\n')

L.redo()
print(f'After redo: {my_List}\n')







