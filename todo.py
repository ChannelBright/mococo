class Todo:

    ## 변수 정의
    todoItem = {}
    isCompleted = False
    isImportant = False

    ## 함수 정의
    def save(self, todo):
        self.todoItem[todo] = [False, False]


    def changeStatus(self, todo, isCompleted):
        self.todoItem[todo][0] = isCompleted

    def isIMportant(self, todo, isImportant):
        self.todoItem[todo][1] = isImportant



    def selectAll(self):
        for key in self.todoItem.keys():
            print(key, "완료여부:", self.todoItem[key][0], "중요여부:", self.todoItem[key][1])




    def delete(self, todo):
        del self.todoItem[todo]

    def changeTodoName(self, todo, changeTodo):
        self.todoItem[changeTodo] = self.todoItem.pop(todo)
