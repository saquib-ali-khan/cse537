# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"
  from game import Actions
  # fringe: list of active nodes
  # explr: list of explored nodes
  #i = 0
  soln = []
  explr = []
  visit = []
  fringe = util.Stack()
  node = [None, problem.getStartState(), '', 0]
  fringe.push(node)

  #while i < 5:
  while not fringe.isEmpty():    
    node = parent, state, dirctn, cost = fringe.pop()
    if problem.isGoalState(state):
      visit.append(node)
      #print str(node[1]) + '--' + str(node[2]) + '-->' + str(node[0])
      soln.append(node[2])
      #explr.append(state)
      break

    if not (state in explr):# and \
        #not (state in fringe.getList()):
      for successor in problem.getSuccessors(state):
      #for successor in reversed(problem.getSuccessors(state)):
        fringe.push([state, successor[0], successor[1], successor[2]])
      visit.append(node)
      explr.append(state)

  #print explr
  #print visit

  parentNode = visit.pop()
  while len(visit) != 1:    
    curNode = visit.pop()
    #print str(curNode) + str(parentNode)
    #print str(curNode[0]) + ', ' + str(curNode[1]) + ' == ' + str(goalState)
    while curNode[1] != parentNode[0]:
      curNode = visit.pop()
    if curNode[0] is None:
      break
    parentNode = curNode
    #print str(curNode[1]) + '--' + str(curNode[2]) + '-->' + str(curNode[0])
    soln.append(curNode[2])
    #i = i + 1
    #print explor
    #print '-----------'
  #print soln[::-1]
  #print visit
  return soln[::-1]
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  soln = []
  explr = []
  visit = []
  fringe = util.Queue()
  node = [None, problem.getStartState(), '', 0]
  fringe.push(node)

  while not fringe.isEmpty():    
    node = parent, state, dirctn, cost = fringe.pop()
    if problem.isGoalState(state):
      visit.append(node)
      soln.append(node[2])
      break
    if not (state in explr):
      for successor in problem.getSuccessors(state):
        fringe.push([state, successor[0], successor[1], successor[2]])
      visit.append(node)
      explr.append(state)

  parentNode = visit.pop()
  while len(visit) != 1:    
    curNode = visit.pop()
    while curNode[1] != parentNode[0]:
      curNode = visit.pop()
    if curNode[0] is None:
      break
    parentNode = curNode
    soln.append(curNode[2])

  return soln[::-1]
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  soln = []
  explr = []
  visit = []
  fringe = util.PriorityQueue()
  node = [None, problem.getStartState(), '', 0]
  fringe.push(node, 0)

  while not fringe.isEmpty(): 
    flag = True
    node = parent, state, dirctn, cost = fringe.pop()
    #print '-------------------------'
    #print node
    #print explr
    if problem.isGoalState(state):
      visit.append(node)
      soln.append(node[2])
      break
    for vState, vCost in explr:
      if state == vState and cost >= vCost:
        #print str(vState) + ' $$ ' + str(vCost)
        flag = False        
    if flag:
      for successor in problem.getSuccessors(state):
        #print cost + successor[2]
        fringe.push([state, successor[0], successor[1], cost+successor[2]], cost+successor[2])
      visit.append(node)
      explr.append((state, cost))
  
  parentNode = visit.pop()
  while len(visit) != 1:    
    curNode = visit.pop()
    while curNode[1] != parentNode[0]:
      curNode = visit.pop()
    if curNode[0] is None:
      break
    parentNode = curNode
    soln.append(curNode[2])

  return soln[::-1]
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  soln = []
  explr = []
  visit = []
  fringe = util.PriorityQueue()
  node = [None, problem.getStartState(), '', 0]
  fringe.push(node, heuristic(node[1], problem))

  while not fringe.isEmpty():
    flag = True
    node = parent, state, dirctn, cost = fringe.pop()
    if problem.isGoalState(state):
      visit.append(node)
      soln.append(node[2])
      break
    for vState, vCost in explr:
      if state == vState and cost >= vCost:
        flag = False
    if flag:
      for successor in problem.getSuccessors(state):
        fringe.push([state, successor[0], successor[1], cost + successor[2]], \
                    cost + successor[2] + heuristic(state, problem))
      visit.append(node)
      explr.append((state, cost))

  parentNode = visit.pop()
  while len(visit) != 1:    
    curNode = visit.pop()
    while curNode[1] != parentNode[0]:
      curNode = visit.pop()
    if curNode[0] is None:
      break
    parentNode = curNode
    soln.append(curNode[2])

  return soln[::-1]
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch