# Sprite Specification

Default RTS sprite settings:

- directions: 8
- camera: isometric
- background: transparent
- output: PNG
- preview: contact sheet PNG
- unit pivot: bottom-center
- building pivot: footprint-center

Required unit animations:

- idle
- walk
- attack
- death

Optional unit animations:

- build
- gather
- reload
- celebrate
- flee

Required building states:

- normal
- under_construction
- damaged
- destroyed

Recommended naming:

```text
assets/units/{faction}/{unit_id}/{animation}_{direction}.png
assets/buildings/{faction}/{building_id}/{state}_{direction}.png
assets/vfx/{effect_id}/{state}_{frame}.png
```

Example:

```text
assets/units/polish/pikeman_t1/walk_ne.png
```

Sprite manifest shape:

```json
{
  "sprites": [
    {
      "id": "unit_pikeman_polish_t1",
      "type": "unit",
      "directions": ["n", "ne", "e", "se", "s", "sw", "w", "nw"],
      "required_animations": ["idle", "walk", "attack", "death"],
      "animations": {
        "idle": {"frames": 12, "files": []},
        "walk": {"frames": 16, "files": []},
        "attack": {"frames": 18, "hit_frame": 11, "files": []},
        "death": {"frames": 20, "loop": false, "files": []}
      },
      "pivot": [64, 96],
      "preview": "reviews/previews/unit_pikeman_polish_t1.png"
    }
  ]
}
```
