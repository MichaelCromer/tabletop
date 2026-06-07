# System

This is a modular TTRPG system.

## Modes of Play

Play advances by moving from one mode to another. The GM should always know what mode the game is currently in and shift narration, detail level, and pacing to match. Controlling this flow is the most powerful tool available for setting the mood and texture of the game.

### Narration and Mood

Two independent dimensions shape how a scene feels at the table: how much the **environment constrains movement**, and how much **time bears down on decisions**. These are often, but not always related. They aren't rules, instead being natural features of gameplay. Understanding them helps the GM recognise when a scene is drifting in mood and decide whether to follow it or redirect it.

#### Axis : Spatial Restriction

At **low spatial restriction**, movement is trivially resolved. Players go where they want and geography is just flavour. The world is accessible and navigable, and the GM's attention is on *what happens* at locations rather than *how to reach them*. This produces an open, player-driven feel.

At **medium spatial restriction**, movement starts to become a strategic part of gameplay. Not everywhere is reachable from anywhere. Paths have costs, and the environment becomes a factor. Players must think about routes, resources, and the implications of where they are.

At **high spatial restriction**, positioning is critical. Movement becomes a limited resource that is granular, mechanically precise, and potentially dangerous. 

The GM raises spatial restriction by introducing meaningful geographic stakes: distances that cost resources, paths that require decisions, locations that are genuinely hard to reach, or dangerous to be in. It drops in familiar territory, open roads, and safety.

#### Axis : Temporal Pressure

At **low temporal pressure**, the clock is generous. Events are ordered loosely, time passes in chunks of hours or days, and even retroactive actions are considered within reason. This produces an expansive, deliberate feel.

At **medium temporal pressure**, the flow of time starts to become a mechanical component of play. The party must commit to their next move before something else happens, and resources deplete in meaningful intervals. Decisions become consequential without being frantic.

At **high temporal pressure**, every second is accounted for. The order of events matters completely, and decisions are irrevocable the moment they're made.

The GM raises temporal pressure by introducing scenarios that present a "failure state" if no action is taken. It drops when players are given room to deliberate, when time is summarized in chunks, and when consequences are no longer tied to in-game durations.

#### How the Axes Combine

These dimensions are related, but can be varied independently, and their different combinations reflect real modes of play. High spatial restriction with low temporal pressure -- carefully mapping an empty ruin -- feels methodical and investigative. Add high temporal pressure and the same ruin becomes a race against the clock. Low spatial restriction with high temporal pressure produces urgency without friction: the players can go anywhere, but something is happening *right now*.

The four game modes below represent the combinations this system has specific mechanics for, arranged from lowest to highest intensity.

### Game Modes

This system introduces specific modes of play. Each mode has its own mechanics and calls for a distinct narration style. The GM should announce mode changes clearly; once players become familiar with what these modes mean, this announcement will be enough to initiate the correct mood at the table.

#### Downtime

Downtime is **low spatial restriction** combined with **low temporal pressure**. Players are in a settlement or other safe, navigable location with time available and no immediate threat. Any known location is accessible without meaningful cost (the GM should consider how broadly "anywhere" should be applied). Time passes in hours, days, or longer.

Downtime should feel **expansive and player-driven**. Ask players what their characters want. Introduce the world through conversation, discovery, and the arrival of news — not through obstacles. Not every moment needs a scene; summarize freely with scene cuts. Retroactive actions are appropriate: if a character would obviously have done something during their two free days in town, they did it.

Downtime is the natural home of long-term consequences: healing, crafting, faction responses to the party's prior actions, rumors spreading, relationships developing. These are things that happen *over time* rather than *in a moment*.

*Example:* The party arrives in Mollen with four days before their contact returns. The GM gives each player one or two meaningful scenes: a late-night conversation at the inn; a suspicious figure watching the docks; a letter that arrives on day three; the rest is summarised or implied. There is little to no resource tracking. "Where do you each wake up on the fourth morning?"

#### Travel

Travel is **medium spatial restriction** combined with **low to medium temporal pressure**. Players are moving through wilderness or between regions, a road through contested territory, a river crossing in uncertain weather. Movement follows connected geography, costs time and resources, and carries the ambient risk of environental danger or hostile encounters.

The GM narrates at the scale of **legs of a journey** rather than individual steps. Each day's march or terrain feature crossed is a meaningful unit. Track what the situation calls for, such as supply, weather, terrain costs, or the occasional encounter, without simulating every hour.

*Example:* The party crosses the Greyfen Marshes. This is difficult terrain with no road, costing a full day. An encounter roll comes up empty, but the GM describes the sucking mud, a distant cry from something large, and the way the path seems to shift underfoot. That night, camping with poor shelter, they're short a ration. These accumulating pressures compose the texture of the journey.

Travel can tip toward medium temporal pressure when the party is being tracked, navigating in conditions that limit visibility, or racing to reach shelter before something closes in.

#### Exploration

Exploration is **high spatial restriction** combined with **medium temporal pressure**. Players are inside a dungeon, ruin, or other potentially hostile location. Every door, corridor, and decision point is meaningful. Movement is granular and deliberate. Time passes in structured turns with tracked resources that keep the possibility of encounter present.

The GM shifts from narrator to **referee**. Describe what the senses register; don't volunteer what can't be perceived.

The dungeon turn is a chunk of time long enough to accomplish a task, but short enough that resources deplete and dangers can wander. Temporal pressure becomes a strategic component. "We can't spend another turn on this room."

*Example:* The party descends into the Vault of the Pale King. Torches are lit, and marching order is declared. The rogue advances and stops: she's heard something ahead. There's a patrol rounding a far corner. In Exploration mode, this timing of events and spatial decision to scout ahead matters a way it wouldn't elsewhere.

Exploration tips into Pressure the moment a trap springs, a fight erupts, or time becomes critical in some other fashion.

#### Pressure

Pressure is **high spatial restriction** combined with **high temporal pressure**. Time is measured in seconds. Order of events is carefully controlled, and each action is committed the moment it's taken. The shift into Pressure should be **clear and deliberate**. The GM announces it, establishes the physical space if relevant, and expects players to commit to actions in sequence.

The GM's job in Pressure is **clarity over atmosphere**. Players need accurate information about threats, terrain, and options. Don't hold back environmental details for dramatic effect; the situation already provides the drama.

*Example:* The party opens a door: they see a bound captive in a chair, a hooded figure with a crossbow, a burning fuse snaking toward a powder keg. The GM calls Pressure. Players must decide, right now, who does what and in what order. The rogue moves for the fuse. The fighter advances on the hooded figure. The mage is still crossing the threshold. These choices unfold in sequence and cannot be taken back.

**This is not only combat**. Resist letting combat be the only automatic trigger for Pressure.  It is any situation where the clock is an antagonist: a ticking trap, a ritual that must be interrupted, a negotiation where the wrong word ends the scene, water filling a chamber while the party searches for the exit, a public confrontation where a reputation is about to be destroyed, a chase through a collapsing building, a ritual countdown; all carry the same structure and drama.


## Core Modules

These are the core modules of the game implementing the above modes of play.


### Settlement Ruleset

Notes
 - typically Downtime mode
 - settlement size either VILLAGE, TOWN, or CITY.
 - settlement creation structure TBD


### Overland Travel Ruleset

Notes
 - typically Travel mode
 - hex crawl based travel
 - hexes : MOUNTAIN HILL WATER PLAINS FOREST SWAMP DESERT JUNGLE TUNDRA
 - roads between hex centres, rivers along hex edges
 - base hex cost is half day travel (or so -- juggle to get right)
 - rougher hexes add time, road/river travel reduces time appropriately
 - players can see
 - hexes are either empty (wilderness) or have one point of interest (which can be hidden)
 - PoIs are either SETTLEMENT (friendly), FEATURE (neutral), or DUNGEON (hostile)
 - players can 'see' terrain of current hex and all neighbouring six hexes


### Dungeoneering Ruleset

 - typically Exploration mode
 - DUNGEON/FEATURE creation structure TBD


### Pressure Scenario Ruleset

Notes
 - for Pressure mode.
 - time counts in "moments" up from 0, representing unit of about 1 second.
 - typically battlemap based, on hex grid, for combat and other spatially restricted scenarios
 - players roll 2d4+1 (6) to generate an "action moment" when they can first use a main action
 - when players take an action, they roll 2d4+1 again and add the total to the current moment for their next action moment
 - players can always move 1 hex each second until their action moment, when they can take an action
 - minor actions can be taken during any moment, but at a cost of pushing their main action later by 1-3 moments (based on action)
 - each main action (each moment? hard to decide), player action point resource pool ticks up by 1 (can be spent on better actions), action pool resets to 0 at end of pressure scenario.
