import logging
from time import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def gen(n=None):
    logging.info(f'Before yield for loop N is {n}')
    for i in range(n):
        logging.info(f'    In loop Iteration is {i} before yield keyword N is {n}')
        n = yield n
        logging.info(f'    In loop Iteration is {i} after yield keyword N is {n}')
    logging.info(f'After for loop before yield keyword N is {n}')
    n = yield n
    logging.info(f'After for loop after yield keyword N is {n}')
    # n = yield n 

if __name__ == '__main__':
    for_iterations = 2 
    logging.info(f'Create generator with {for_iterations} for loop iterations')
    g = gen(for_iterations)
    logging.info(f'Start generator')
    g.__next__()
    logging.info(f'Send 3 to generator')
    g.send(3)
    logging.info(f'Send 4 to generator')
    g.send(4)
    # g.__next__()
    logging.info(f'Send 5 to generator (more than gen loop expected)')
    try:
        g.send(5)
    except StopIteration as e:
        logging.info(f'Get StopIteration exception')
    logging.info(f'Stop example')
    

    # g.send(6)
