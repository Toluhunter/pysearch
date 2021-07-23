import time
from threading import Thread

class Animation(Thread):

    def __init__(self, text='fetching packages'):
        super().__init__()
        self.animation = True
        self.TEXT = text

    def run(self):
        '''Function to execute on a seperate Thread'''
        print(self.TEXT, end='', flush=True)
        count = 0

        while self.animation:
            if count > 3:
                count = 0

            print('.'*count, end='', flush=True)
            time.sleep(0.5)
            
            print('\b \b'*count, end='', flush=True)
            count += 1
        print()

    def join(self):
        '''
        Overloaded join function to Stop 
        animation before clossing thread
        '''
        self.animation = False
        super().join()

if __name__ == "__main__":
    #Example of how to use replace sleep with function

    animate = Animation()

    animate.start()
    
    time.sleep(5)

    animate.join()
