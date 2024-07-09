# Tabletop RPG Content

This repo collects together modular TTRPG content (chiefly aimed at D&D5E but ultimately
system agnostic).

## Content Types

The repo contains content of the following types:

### Module 

Modules are built as collections of related _Scenes_, the smallest useful unit of table
time. Scenes are composed using a modular pattern called the _Structure_, which imposes
narrative connections between its components.

- **Scene.** The set of GM-Player interactions (content, exposition, die rolls, etc)
  relating to a single, immediate _Goal_, usually in the format "[Verb] the [Noun]". For
  example, "Defeat the goblin boss", "Loot the locked chest", "Find the secret door".
- **Structure.** Three to five units are composed, with two designated as special
  "beginning" and "end" nodes. Edges are added between nodes in any way, provided that
  all are connected. One "central tension" marker is placed, on either a node or an
  edge, to indicate where the thematic or narrative focus of the Structure sits.  Edges
  provide logical or narrative connections between components, and together with the
  central tension marker indicate what kind of narrative is represented.
  
This allows for the following higher-order compositions:

- **Act.** A Structure of Scenes which make a small story, suitable for approximately 45
  minutes of gameplay. 
- **Dungeon.** A Structure of Acts, providing a mini-adventure suitable for
  approximately one session of gameplay.
- **Module.** A Structure of Dungeons, providing an adventure suitable for something
  like one to three character levels of progression.
