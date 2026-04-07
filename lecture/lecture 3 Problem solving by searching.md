### reflex agents
- choose action based on current percept
- doesnt consider the future outcomes
- may have model

### planning agents
- decisions based on (hypothesized ) consequences of actions
- must have a model of how the world evolves in response to actions
- must formulate a goal
- consider how the world would be

1. optimal planning - хамгийн шилдэг төлөвлөгөө боловсруулдаг
2. complete planning - ямар нэгэн байдлаар хариу олдог
 - planning - нэг төлөвлөгөө гаргадаг
 - replanning - алхам бүрдээ шаардлагатай бол дахин төлөвлөгөө гаргадаг

A **search problem** consists of :
1. a state space
2.  successor function(with actions, costs)
3. a start state and a goal test
A solution is a sequence of actions which transforms the start state to goal state.
