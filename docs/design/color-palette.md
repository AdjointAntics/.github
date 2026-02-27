# AdjointAntics Color Palette

An adjunction is not a symmetry. It's a directed relationship — one functor dominates, the other recedes. The palette reflects this. Cyan speaks. Everything else listens.

## Core

| Role | Name | Hex | Rationale |
|:--|:--|:--|:--|
| Background | **Void** | `#0A0A0A` | The category itself. Contains all objects and morphisms. Shows none. Almost everything is this. |
| Text | **Morphism** | `#D4D4D4` | Arrows between objects. Not pure white — pure white is a statement, and the text isn't making one. |
| Primary | **Left Adjoint** | `#00FFCE` | F. The free functor. Constructs, synthesizes, reaches forward. Used sparingly, which is why it works. |

## Accent

| Role | Name | Hex | Rationale |
|:--|:--|:--|:--|
| Secondary | **Right Adjoint** | `#9558B2` | G. The forgetful functor. Inherited from Julia. This isn't tribute — it's type-theoretic. We are a Julia org. The lineage should be visible in the color space. |
| Alert | **Unit** | `#FF3366` | η: 1 → GF. The natural transformation that starts a round trip. Used only for things that demand attention — errors, breaking changes, deprecations. If you see this color, something is asking you to act. |

## Structure

| Role | Name | Hex | Rationale |
|:--|:--|:--|:--|
| Surface | **Elevation** | `#1A1A1A` | Code blocks, cards, anything that lifts off the void. The difference between `0A` and `1A` is subtle. That's the point — structure should be felt, not seen. |
| Border | **Counit** | `#4A4A4A` | ε: FG → 1. The return. Muted text, borders, dividers. The things that organize without competing. |

## The seven

```
#0A0A0A · #1A1A1A · #4A4A4A · #D4D4D4 · #00FFCE · #9558B2 · #FF3366
```

## Usage rules

1. **Cyan is earned.** Headers, links, the logo, key data. Never decoration.
2. **Rose is rare.** If more than 5% of a page is `#FF3366`, something is wrong with the page, not the palette.
3. **Purple connects.** Links to Julia ecosystem, references to dependencies, inherited concepts.
4. **When in doubt, use gray.** The palette has three grays for a reason. Most UI is structure, and structure is gray.
5. **No gradients.** Flat color. The algebra is discrete.

## CSS variables

```css
:root {
  --void: #0A0A0A;
  --elevation: #1A1A1A;
  --counit: #4A4A4A;
  --morphism: #D4D4D4;
  --left-adjoint: #00FFCE;
  --right-adjoint: #9558B2;
  --unit: #FF3366;
}
```

## Julia constants

```julia
const PALETTE = (
    void          = "#0A0A0A",
    elevation     = "#1A1A1A",
    counit        = "#4A4A4A",
    morphism      = "#D4D4D4",
    left_adjoint  = "#00FFCE",
    right_adjoint = "#9558B2",
    unit          = "#FF3366",
)
```
