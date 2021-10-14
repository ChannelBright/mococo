from todo import Todo

todo = Todo()

print("======= 할일 생성 ========")
todo.save("운동하기")
todo.save("공부하기")
todo.save("식사하기")
todo.save("노래하기")
todo.save("산책하기")
todo.selectAll()

print("\n======= 할일 삭제 ========")
todo.delete("운동하기")
todo.selectAll()

print("\n======= 완료 여부 변경 ========")
todo.changeStatus("산책하기", True)
todo.selectAll()

print("\n======= 중요도 여부 변경 ========")
todo.isIMportant("산책하기", True)
todo.selectAll()


print("\n======= 할일 키값 변경 ========")
todo.changeTodoName("식사하기", "식사하자")
todo.selectAll()