# Contributing to AdjointAntics

Every construction has a dual. Every contribution has a home.

## Choose Your Entry Point

| If you care about... | Start with... |
|:--|:--|
| Category theory foundations | [Theory.jl](https://github.com/AdjointAntics/Theory.jl) |
| Representable functors / limits | [Yoneda.jl](https://github.com/AdjointAntics/Yoneda.jl) |
| Terminal styling / rendering | [YonedaStyle.jl](https://github.com/AdjointAntics/YonedaStyle.jl) |
| Benchmarking / measurement | [HomTime.jl](https://github.com/AdjointAntics/HomTime.jl) |
| Recursion schemes / AST folds | [Initial.jl](https://github.com/AdjointAntics/Initial.jl) + [Terminal.jl](https://github.com/AdjointAntics/Terminal.jl) |
| Effects / code generation | [Free.jl](https://github.com/AdjointAntics/Free.jl) |
| Property testing / algebraic laws | [Cofree.jl](https://github.com/AdjointAntics/Cofree.jl) |
| Polynomial functors / optics | [Poly.jl](https://github.com/AdjointAntics/Poly.jl) |
| TUI / interactive apps | [PolyModes.jl](https://github.com/AdjointAntics/PolyModes.jl) |
| Linting / static analysis | [Strict.jl](https://github.com/AdjointAntics/Strict.jl) |

## How the Pieces Fit

Dependencies flow strictly downward through tiers:

```
Theory (T0) → Yoneda, YonedaStyle, HomTime (T1) → Initial, Terminal (T2) → Free, Cofree, Poly (T3) → PolyModes (T4)
```

A package at tier N depends only on tiers 0 through N-1. Never on its own tier or above.

## Getting Started

1. Clone the package you want to work on
2. `make test` — run the full test suite
3. Read the package's `CLAUDE.md` for architecture details
4. Read the package's `CONTRIBUTING.md` for package-specific guidance

## Development Workflow

1. Fork the repository
2. Create a feature branch (`feat/your-feature`) or bugfix branch (`fix/your-fix`)
3. Write tests first — commutativity is correctness
4. Implement — follow the conventions below
5. `make test` — everything must pass
6. Submit a pull request

## Conventions

- **Naming:** `snake_case` functions, `PascalCase` types, `TitleCase.jl` files, `_prefix` internals
- **Structs:** immutable by default; mutable only with codata justification (document why)
- **Docstrings:** signature line, blank line, substantive explanation — on every public symbol
- **Testing:** algebraic laws MUST be tested for every categorical abstraction
- **Commits:** [Conventional Commits](https://www.conventionalcommits.org/) — `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `perf:`

## Standards

- [Engineering Standards](https://github.com/AdjointAntics/.github/blob/main/docs/standards/engineering.md)
- [Categorical Design Standards](https://github.com/AdjointAntics/.github/blob/main/docs/standards/categorical.md)

## Duality Check

When adding a new construction, ask: *what is its dual?* If it doesn't exist yet, plan for it. Every fold has an unfold. Every syntax has an observation. If your contribution breaks a duality, something is missing.

---

*Seeking the universal property of good software.*
