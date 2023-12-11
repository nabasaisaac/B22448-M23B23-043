# Qestion 2

class StudentQueue:
    def __init__(self): #Constructor of our class StudentQueue
        self.student = []   #Creating empty list 
        self.size = 0       #Initialising size of the queue as 0
        
    def enqueue_students(self, student): #This method has one parameter
        self.student.append(student)
        self.size+=1    # Increamenting queue size when a student is added

    def dequeue_students(self):
        if self.is_queue_empty():
            raise Exception("Students' queue is empty")     # Raising error when the queue is empty
        elif self.size == 0:
            raise Exception("Students' queue is empty")     # Raising error when the queue size is 1
        else:
            self.student.pop(0)  # Removing the first student, FIFO, first in first out
            self.size-=1
    
    def is_queue_empty(self):   
        if self.student is None:    #If there are no students, 
            return True
    
    def current_size(self):
        return f'There are {self.size} students in the queue'


if __name__=='__main__':
    student_queue = StudentQueue() #Instantiating the class StudentQueue

    # Demonstration on how the students will join the queue:
    student_queue.enqueue_students('Busingye')
    student_queue.enqueue_students('Apophia')
    student_queue.enqueue_students('Tinah')
    student_queue.enqueue_students('Hope')
    student_queue.enqueue_students('Daphine')

    # Demonstrating how students get served on dinining hall
    # student_queue.dequeue_students()
    student_queue.dequeue_students()
    student_queue.dequeue_students()
    
    # Demonstrating how to assertain the size of the queue
    print(student_queue.current_size())




        
    


        