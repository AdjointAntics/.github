# AdjointAntics — Engineering Standards

Org-wide conventions for all AdjointAntics Julia packages. For the categorical design principles behind these conventions, see [categorical.md](categorical.md).

## Code Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Functions, variables | `snake_case` | `compute_left_kan`, `run_state` |
| Types, modules | `PascalCase` | `MonoidalCategory`, `TambaraModule` |
| Filenames | `TitleCase.jl` | `Monoidal.jl`, `Profunctor.jl` |
| Internal helpers | `_prefix` | `_children_and_rebuild`, `_apply_continuation` |
| Constants | `SCREAMING_CASE` | `BOX_SINGLE`, `PALETTE` |

## Structs

- **Immutable by default.** All structs are `struct`, not `mutable struct`.
- **All fields must have explicit type annotations.** No untyped fields.
- **Mutable structs require justification.** Valid reasons: codata pattern (Moore machines, sinks, buffers), accumulators, screen state. Document the justification in a comment above the struct.

## Docstrings

Every public symbol gets a docstring. Format:

```julia
"""
    function_name(arg1::Type1, arg2::Type2) -> ReturnType

One-sentence summary.

Detailed explanation of behavior, invariants, and laws.
"""
```

## Dependencies

- **Foundation packages** (Theory, YonedaStyle, HomTime): zero external dependencies.
- **Tier 2+ packages:** minimal deps, prefer local path deps via `[sources]` in Project.toml.
- **Never add dependencies that duplicate stdlib functionality.**
- **Test-only dependencies** (Aqua.jl, Documenter.jl) are acceptable in test environments.

## Testing

- Test files: `test/test_*.jl`
- Runner: `test/runtests.jl`
- Julia 1.10+ compatibility required
- **Algebraic laws MUST be tested for every categorical abstraction**
- **Round-trip properties** (`project`/`embed`, `encode`/`decode`, `tabulate`/`index`) MUST be tested
- Use `check_code(rule, code_string)` for linter rule doctests (Strict.jl convention)

## Quality Gates

- All tests pass: `julia --project=. -e 'using Pkg; Pkg.test()'`
- No type instabilities in hot paths
- No unnecessary allocations in inner loops
- Algebraic laws verified (not just unit tests — law suites from Cofree.jl)

## Versioning

- SemVer for all packages
- `v0.1.0` for initial release
- Breaking changes require major version bump
- Changelog maintained per package (`CHANGELOG.md`)

## Performance

- Benchmark with HomTime.jl (`hom()` auto-calibrates, disables GC during samples)
- **No premature optimization** — measure first, then optimize
- `compose_temporal` for sequential pipeline benchmarks (sum times)
- `tensor_temporal` for parallel pipeline benchmarks (max time, sum allocations)
- GC control in benchmarks (`GC.enable(false)` during measurement windows)

## Mathematical Conventions

- **Diagrammatic order** for composition: `compose(f, g)` = "first f, then g"
- **Law checkers take operations as function arguments** (not dispatch) — enables testing any instance without subtyping
- **Package names are theorems, not features** — the name declares what structure the package models
