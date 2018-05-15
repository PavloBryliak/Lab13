import random
from arrays import Array
from TicketCounterSimulation.llistqueue import Queue
from TicketCounterSimulation.people import TicketAgent, Passenger


class TicketCounterSimulation:
    # Create a simulation object.
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
    # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
    # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array( numAgents )
        for i in range( numAgents ) :
            self._theAgents[i] = TicketAgent(i+1)

    # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # If a customer arrives, he is added to the queue.
    # At most, one customer can arrive during each time step.
    def _handleArrival(self, curTime):
        person = random.random()
        if person< self._arriveProb:
            self._numPassengers += 1
            self._passengerQ.enqueue(Passenger(self._numPassengers, curTime))
            print("Costumer number {} arrived".format(self._numPassengers))

    # If there are customers waiting, for each free server,
    #  the next customer in line begins her transaction.
    def _handleBeginService(self, curTime):
        for agent in self._theAgents:
            if agent.isFree() and len(self._passengerQ):
                self._totalWaitTime += curTime-self._passengerQ.peek()._arrivalTime
                agent.startService(self._passengerQ.dequeue(), curTime+self._serviceTime)
                print("Serving a costumer...")

    # For each server handling a transaction, if the transaction is complete,
    # the customer departs and the server becomes free.
    def _handleEndService(self, curTime):
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                agent.stopService()

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        for curTime in range(self._numMinutes + 1) :
            self._handleArrival( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )

    # Print the simulation results.
    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print( "" )
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" % len(self._passengerQ) )
        print( "The average wait time was %4.2f minutes." % avgWait )


n = TicketCounterSimulation(2, 10000, 2, 4)
n.run()
n.printResults()