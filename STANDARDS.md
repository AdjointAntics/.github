# AdjointAntics — Standards

Canonical versions live in the [.github org repo](https://github.com/AdjointAntics/.github/tree/main/docs/standards). This file summarizes the key principles for quick reference.

## Engineering Standards

> Full version: [engineering.md](https://github.com/AdjointAntics/.github/blob/main/docs/standards/engineering.md)

- **Naming:** `snake_case` functions, `PascalCase` types, `TitleCase.jl` files, `_prefix` internals
- **Structs:** immutable by default; mutable only with documented codata justification
- **Docstrings:** signature line, blank line, substantive explanation — on every public symbol
- **Dependencies:** zero external for foundations (Theory, YonedaStyle, HomTime); local path deps via `[sources]`
- **Testing:** `test/test_*.jl` naming, `runtests.jl` runner, Aqua quality gates, algebraic laws MUST be tested
- **Commits:** [Conventional Commits](https://www.conventionalcommits.org/) — `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `perf:`

## Categorical Design Standards

> Full version: [categorical.md](https://github.com/AdjointAntics/.github/blob/main/docs/standards/categorical.md)

1. **Protocol-then-model** — Theory.jl declares abstract types and function stubs; downstream packages implement
2. **Duality discipline** — every construction has a dual; implement one side, the other falls out
3. **Tier system** — deps flow strictly downward (T0 → T1 → T2 → T3 → T4)
4. **Codata justification** — mutable only for codata patterns (Moore machines, buffers, sinks)
5. **Law verification** — 39 checkers in Theory.jl, 22 suites in Cofree.jl; laws that aren't tested don't exist
6. **Compositionality** — if two things don't compose cleanly, the abstraction boundary is wrong
7. **Iterative safety** — explicit stacks, type-aligned queues; no naive recursion on unbounded structures
8. **Zero-dep foundations** — Theory.jl, YonedaStyle.jl, HomTime.jl have zero external dependencies
