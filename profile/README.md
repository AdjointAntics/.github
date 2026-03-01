<p align="center">
  <img src="logo.svg" alt="AdjointAntics" width="200"/>
</p>

<h1 align="center">AdjointAntics</h1>

<p align="center"><em>Dual-wielding code with a left & right kan</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/F_%E2%8A%A3_G-adjoint%20paired-00FFCE?style=flat-square" alt="Adjoint Paired"/>
  <img src="https://img.shields.io/badge/julia-1.10+-9558B2?style=flat-square&logo=julia&logoColor=white" alt="Julia 1.10+"/>
  <img src="https://img.shields.io/badge/diagrams-commuting-00FFCE?style=flat-square" alt="Diagrams Commuting"/>
</p>

---

We write Julia libraries that take adjunctions seriously as an engineering discipline — not a curiosity, not a flex, but the computational structure behind differentiation, learning, and optimization.

Where [AlgebraicJulia](https://github.com/AlgebraicJulia) gives you categories as data structures, we're building categories as computational strategies — particularly the adjoint machinery $(F \dashv G)$ that drives autodiff, encoder-decoder architectures, and compositional inference.

The algebra should compile. The abstractions should vanish at runtime. The diagrams should commute.

## Packages

| | Package | What It Does |
|:--|:--|:--|
| ![](https://img.shields.io/badge/T0-kernel-00FFCE?style=flat-square&labelColor=0C0E16) | [**Theory.jl**](https://github.com/AdjointAntics/Theory.jl) | Algebraic theory protocols, ExprF pattern functor, 78 law checkers |
| ![](https://img.shields.io/badge/T1-foundation-4CB8E8?style=flat-square&labelColor=0C0E16) | [**Yoneda.jl**](https://github.com/AdjointAntics/Yoneda.jl) | Representable functors, presheaves, Kan extensions, concrete limits |
| ![](https://img.shields.io/badge/T1-foundation-4CB8E8?style=flat-square&labelColor=0C0E16) | [**YonedaStyle.jl**](https://github.com/AdjointAntics/YonedaStyle.jl) | ANSI styling, tables, trees — display as representability |
| ![](https://img.shields.io/badge/T1-foundation-4CB8E8?style=flat-square&labelColor=0C0E16) | [**HomTime.jl**](https://github.com/AdjointAntics/HomTime.jl) | Hom-functor benchmarking with convergence and trust scores |
| ![](https://img.shields.io/badge/T2-fixed_point-FFBE0B?style=flat-square&labelColor=0C0E16) | [**Initial.jl**](https://github.com/AdjointAntics/Initial.jl) | Catamorphisms, paramorphisms, zygo, histo — the folds |
| ![](https://img.shields.io/badge/T2-fixed_point-FFBE0B?style=flat-square&labelColor=0C0E16) | [**Terminal.jl**](https://github.com/AdjointAntics/Terminal.jl) | Anamorphisms, futu, chrono, streams, sinks — the unfolds |
| ![](https://img.shields.io/badge/T3-adjunction-AA78C8?style=flat-square&labelColor=0C0E16) | [**Free.jl**](https://github.com/AdjointAntics/Free.jl) | Algebraic effects, schema DSL, 11 code-gen backends, monad transformers |
| ![](https://img.shields.io/badge/T3-adjunction-AA78C8?style=flat-square&labelColor=0C0E16) | [**Cofree.jl**](https://github.com/AdjointAntics/Cofree.jl) | Cofree comonad, property testing, 22 algebraic law suites |
| ![](https://img.shields.io/badge/T3-adjunction-AA78C8?style=flat-square&labelColor=0C0E16) | [**Poly.jl**](https://github.com/AdjointAntics/Poly.jl) | Polynomial functors, profunctor optics, wiring diagrams, SVG rendering |
| ![](https://img.shields.io/badge/T4-application-33DD66?style=flat-square&labelColor=0C0E16) | [**PolyModes.jl**](https://github.com/AdjointAntics/PolyModes.jl) | TUI framework — widgets as Moore machines |
| ![](https://img.shields.io/badge/App-tool-D4D4D4?style=flat-square&labelColor=0C0E16) | [**Strict.jl**](https://github.com/AdjointAntics/Strict.jl) | Julia linter — 118 rules, functor architecture, autofixes |
| ![](https://img.shields.io/badge/Util-scaffold-D4D4D4?style=flat-square&labelColor=0C0E16) | [**StrictTemplate.jl**](https://github.com/AdjointAntics/StrictTemplate.jl) | Package scaffold — every other package factors through it |

## Dualities

Every construction has a dual. This halves the design space.

| Left | | Right | Relationship |
|:--|:--|:--|:--|
| **Free.jl** | ↔ | **Cofree.jl** | syntax ↔ observation |
| **Initial.jl** | ↔ | **Terminal.jl** | fold ↔ unfold |
| **Poly.jl** | ↔ | **HomTime.jl** | interface ↔ measurement |
| **Theory.jl** | ↔ | **Theory.jl** | self-dual: protocols |

## Design System

<p>
  <img src="https://img.shields.io/badge/Void-%20-0C0E16?style=flat-square&labelColor=0C0E16" alt="Void"/>
  <img src="https://img.shields.io/badge/Elevation-%20-181B24?style=flat-square&labelColor=0C0E16" alt="Elevation"/>
  <img src="https://img.shields.io/badge/Counit-%20-666666?style=flat-square&labelColor=0C0E16" alt="Counit"/>
  <img src="https://img.shields.io/badge/Morphism-%20-D4D4D4?style=flat-square&labelColor=0C0E16" alt="Morphism"/>
  <img src="https://img.shields.io/badge/Left_Adjoint-%20-00FFCE?style=flat-square&labelColor=0C0E16" alt="Left Adjoint"/>
  <img src="https://img.shields.io/badge/Right_Adjoint-%20-AA78C8?style=flat-square&labelColor=0C0E16" alt="Right Adjoint"/>
  <img src="https://img.shields.io/badge/Unit-%20-FF3366?style=flat-square&labelColor=0C0E16" alt="Unit"/>
  <img src="https://img.shields.io/badge/Comonad-%20-FFBE0B?style=flat-square&labelColor=0C0E16" alt="Comonad"/>
  <img src="https://img.shields.io/badge/Hom-%20-4CB8E8?style=flat-square&labelColor=0C0E16" alt="Hom"/>
  <img src="https://img.shields.io/badge/Isomorphism-%20-33DD66?style=flat-square&labelColor=0C0E16" alt="Isomorphism"/>
</p>

Ten colors. Categorically named. WCAG AA minimum. See the [full palette](../docs/design/color-palette.md).

## Open Questions

- Can the Para construction give Julia a categorical interface to gradient-based learning?
- What's the right comonadic semantics for streaming data and online inference?
- When does the free-forgetful pattern in type systems actually buy you performance?
- What's the right API surface for profunctor optics in Julia?

If any of these keep you up at night — [open a discussion](https://github.com/orgs/AdjointAntics/discussions).

## Standing on the Shoulders of

**Organizations**
- [AlgebraicJulia](https://github.com/AlgebraicJulia) — Applied category theory in Julia
- [nLab](https://ncatlab.org) — The community wiki for higher category theory
- [Statebox](https://github.com/statebox) — Categorical process theory and verified smart contracts
- [Topos Institute](https://github.com/ToposInstitute) — Research at the intersection of computation, category theory, and society

**Repositories**
- [ACSets.jl](https://github.com/AlgebraicJulia/ACSets.jl) — Acyclic colimit sets for structured data
- [Catlab.jl](https://github.com/AlgebraicJulia/Catlab.jl) — Categorical modeling framework
- [idris-ct](https://github.com/statebox/idris-ct) — Verified category theory in Idris
- [Oscar.jl](https://github.com/oscar-system/Oscar.jl) — Computer algebra in Julia
- [Typedefs](https://github.com/typedefs/typedefs) — Algebraic type definitions as a language

---

<p align="center"><em>Seeking the universal property of good software.</em></p>
