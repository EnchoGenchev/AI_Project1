# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    #storing state and path to state
    stack = util.Stack()
    startState = problem.getStartState()
    stack.push((startState, []))

    #keeping track of visited states to avoid cycles
    visited = set()

    while not stack.isEmpty():
        #checking top of the stack
        state, path = stack.pop()

        #add if new state
        if state not in visited:
            visited.add(state)

        #check if at the goal
        if problem.isGoalState(state):
            return path
        
        #checking all successor states (tuples)
        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                #adds next action to current list of actions
                stack.push((successor, path + [action]))

    
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    
    #storing state and path to state
    queue = util.Queue() #BFS needs FIFO so nodes closer to start are expanded first
    startState = problem.getStartState()
    queue.push((startState, []))

    visited = set()
    seen = set() #handles cases where paths converge to avoid copies of same node

    seen.add(startState)

    while not queue.isEmpty():
        #getting next node
        currentState, path = queue.pop() #queue stores tuples

        #marking states as visited so they aren't repeated
        if currentState not in visited:
            visited.add(currentState)

        if problem.isGoalState(currentState):
            return path
        
        #if not at goal then check all sucessors
        for successor, action, stepCost in problem.getSuccessors(currentState):
            if successor not in visited and successor not in seen:
                #adding new action to list in path
                queue.push((successor, path + [action]))
                seen.add(successor) #node has been located but may not have bee expanded yet
        
    return[]

    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    from math import inf
    pq = util.PriorityQueue()
    start = problem.getStartState()
    # best known cost to each state
    dist = {start: 0}
    # best known path (list of actions) to each state
    path = {start: []}
    pq.push(start, 0)

    while not pq.isEmpty():
        state = pq.pop()

        # If this pop is stale (we already found a cheaper way), skip it
        current_cost = dist[state]

        if problem.isGoalState(state):
            return path[state]

        for succ, action, stepCost in problem.getSuccessors(state):
            new_cost = current_cost + stepCost

            if new_cost < dist.get(succ, inf):
                dist[succ] = new_cost
                path[succ] = path[state] + [action]
                pq.update(succ, new_cost)

    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
