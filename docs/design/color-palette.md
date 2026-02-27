# AdjointAntics Color Palette

An adjunction is not a symmetry. It's a directed relationship — one functor dominates, the other recedes. The palette reflects this. Cyan speaks. Everything else listens.

## Core

| Role | Name | Hex | Contrast on Void | Rationale |
|:--|:--|:--|:--|:--|
| Background | **Void** | `#0A0A0A` | — | The category itself. Contains all objects and morphisms. Shows none. Almost everything is this. |
| Text | **Morphism** | `#D4D4D4` | 13.4:1 AAA | Arrows between objects. Not pure white — pure white is a statement, and the text isn't making one. |
| Primary | **Left Adjoint** | `#00FFCE` | 15.3:1 AAA | F. The free functor. Constructs, synthesizes, reaches forward. Used sparingly, which is why it works. |

## Accent

| Role | Name | Hex | Contrast on Void | Rationale |
|:--|:--|:--|:--|:--|
| Secondary | **Right Adjoint** | `#AA78C8` | 5.9:1 AA | G. The forgetful functor. Evolved from Julia purple. The lineage is visible in the color space. |
| Alert | **Unit** | `#FF3366` | 5.6:1 AA | η: 1 → GF. The natural transformation that starts a round trip. Used only for things that demand attention — errors, breaking changes, deprecations. If you see this color, something is asking you to act. |

## Structure

| Role | Name | Hex | Contrast on Void | Rationale |
|:--|:--|:--|:--|:--|
| Surface | **Elevation** | `#1A1A1A` | — | Code blocks, cards, anything that lifts off the void. The difference between `0A` and `1A` is subtle. That's the point — structure should be felt, not seen. |
| Border | **Counit** | `#666666` | 3.4:1 AA-large | ε: FG → 1. The return. Borders, dividers, de-emphasized text. The things that organize without competing. |

## The seven

```
#0A0A0A · #1A1A1A · #666666 · #D4D4D4 · #00FFCE · #AA78C8 · #FF3366
```

## Accessibility

All text-bearing colors meet WCAG 2.1 AA or higher on both Void (`#0A0A0A`) and Elevation (`#1A1A1A`) backgrounds:

| Color | On Void | On Elevation | Minimum required |
|:--|:--|:--|:--|
| Morphism `#D4D4D4` | 13.4:1 AAA | 11.7:1 AAA | AAA (body text) |
| Left Adjoint `#00FFCE` | 15.3:1 AAA | 13.4:1 AAA | AA (headings, links) |
| Right Adjoint `#AA78C8` | 5.9:1 AA | 5.2:1 AA | AA (links, labels) |
| Unit `#FF3366` | 5.6:1 AA | 4.9:1 AA | AA (alerts) |
| Counit `#666666` | 3.4:1 AA-large | 3.0:1 AA-large | AA-large (muted text, borders) |

Never convey meaning through color alone. Pair color with shape, icon, or text label.

## Usage rules

1. **Cyan is earned.** Headers, links, the logo, key data. Never decoration.
2. **Rose is rare.** If more than 5% of a page is `#FF3366`, something is wrong with the page, not the palette.
3. **Purple connects.** Links to Julia ecosystem, references to dependencies, inherited concepts.
4. **When in doubt, use gray.** Most UI is structure, and structure is gray.
5. **No gradients.** Flat color. The algebra is discrete.
6. **Never color alone.** Errors get an icon. Links get an underline. Status gets a label. Color reinforces — it doesn't carry.

## CSS variables

```css
:root {
  --void: #0A0A0A;
  --elevation: #1A1A1A;
  --counit: #666666;
  --morphism: #D4D4D4;
  --left-adjoint: #00FFCE;
  --right-adjoint: #AA78C8;
  --unit: #FF3366;
}
```

## Julia constants

```julia
const PALETTE = (
    void          = "#0A0A0A",
    elevation     = "#1A1A1A",
    counit        = "#666666",
    morphism      = "#D4D4D4",
    left_adjoint  = "#00FFCE",
    right_adjoint = "#AA78C8",
    unit          = "#FF3366",
)
```
