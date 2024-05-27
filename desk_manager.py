from queue import Queue
def register_paitent (queue):
    name = input("Enter paitent name:")
    queue.put()
    print("paitent", name, "registered." )

def remove_paitent (queue):
    if queue.empty():
        print('queue is empty')
    else:
        paitent_removed = queue.get()
        print("paitent", paitent_removed, "removed")

def display_paitent(queue) :
    if queue.empty():
        print("queue is empty")
    else:
        for paitent in __name__

    





