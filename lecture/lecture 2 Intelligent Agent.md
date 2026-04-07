- An agent is an entity that perceives and acts
- Rational agent selects actions that maximize its expected utility
- Agent is able to make decisions itself.
- Sensors, actuators, and environment dictate techniques for selecting rational actions
- Agent function maps percept sequences to actions

episodic vs sequential environment
1. is the choice of current action dependent on previous actions? -> if not, then the environent is episodic
2. in non-episodic environment -> current choice will affect future ones

known vs unknown
1. in a known environment:
	1. the outcomes (or outcome probabilities if the environment is non determenistic) for all actions are given
2. if the environment is unknown:
	1. the agent will have to learn how it works in order to make good decisions.


partially observable -> agent requires memory
stochastic -> agent may prepare for **contingencies**
multi-agent -> agent may need to behave randomly
static -> agent has to compute rational decision
unknown physics -> need for exploration
continuous time -> continuously operating controller
unknown performance measure -> 


**Simple reflex agents** -> agents select actions on the basis of the current percept, ignoring the rest of percept history. no memory required

**Reflex agents with states** -> model-based reflex agents.
1. know how world evolves
2. know how agent actions affect the world 

**Goal based agents** -> 
**Utility based agents** 
1. goals are not always enough
2. a utility function maps a state onto a real number which describes the associated degree of '"happiness' , 'goodness', 'success'
3. utility measures come from economics, biology etc.
**Learning agents**
- performance element is what was ...
