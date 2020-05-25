#!/usr/bin/python3

import click
import random
import statistics
from HCSR04 import HCSR04Provider

def callback(ctx, param, value):
    if value <= 4:
        print("Iteration must be greathen than 4")
        ctx.abort()
    return value

class RandomProvider():
    def getValue(self):
        return random.randint(0,100)

@click.command()
@click.argument("iteration", callback=callback,type=click.INT, default=5)
@click.option("-e","--echo","echo",required=True)
@click.option("-t","--trigger","trigger",required=True)



def hello(iteration, echo, trigger):
    provider=HCSR04Provider(echo, trigger)
    #provider= RandomProvider()
    values=[]
    for i in range(0, iteration):
        values.append(provider.getValue())
    values.sort()
    values.remove(max(values))
    values.remove(min(values))
    print(statistics.median(values))

if __name__ == '__main__':
    hello()
