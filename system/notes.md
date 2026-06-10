# Notes

## Rolls

### Cumulative Check

Roll Nd6, where N increments at each consecutive attempt. N resets once an outcome is obtained.

**Success and Failure**: Potentially whenever:

 - a target value is obtained on any die (e.g. a 1, or surpassing some minimum DC value)
 - a fixed number of target values are obtained simultaneously
 - a fixed number of target values are obtained cumulatively, racing total successes against total failures.

**Circumstantial bonuses**

 - If a player character has a relevant skill, consider starting N at some non-zero value
 - If repeated attempts confer more benefit, consider allowing N to increment in bigger step sizes
 - If skill is relevant (and success is measured in DC value), allow skill to be added.

**Use Case**

 - to simulate a random environmental effect
 - to simulate sustained effort towards a goal
 - whenever there is the potential for "no outcome...yet"

**Example: Dungeon Encounters**

Rolled each dungeon turn, with "failure" (combat encounter occurs) being any die equalling a single specific value (e.g. 1).

| N | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| % Outcome | 17 | 31 | 43 | 52 | 60 | 67 | 73 | 77 | 81 | 84 | 87 | 89 |


### Ability Check

Roll 2d6+X where X is the relevant ability (Might, Wit, Charm). A result of 7 or 8 is a minor success, 9 or 10 is a moderate success, and 11 or 12 is a major success.

| Bonus | % Minor | % Medium | % Major |
|---|---|---|---|
| 0 | 58 | 27 | 8  |
| 1 | 72 | 41 | 16 |
| 2 | 83 | 58 | 27 |
| 3 | 91 | 72 | 41 |

**Use Case**

 - One-off, intsantaneous individual effort (attack roll, etc)

#### Advantange and Disadvantange

Roll (3d6-L/H)+X for advantage and disadvantage respectively.

**Advantage**
| Bonus | % Minor | % Medium | % Major |
|---|---|---|---|
| 0 | 80 | 52 | 19 |
| 1 | 89 | 68 | 35 |
| 2 | 94 | 80 | 52 |
| 3 | 98 | 89 | 68 |

**Disadvantage**
| Bonus | % Minor | % Medium | % Major |
|---|---|---|---|
| 0 | 31 | 10 |  1 |
| 1 | 47 | 19 |  5 |
| 2 | 64 | 31 | 10 |
| 3 | 80 | 47 | 19 |


### Group Check

Each participating member rolls Nd6, where N is their relevant ability modifier. Successes and failures are counted as for the Cumulative check.

**Use case**

 - One-off, instantaneous distributed effort (foraging, scouting, etc)
