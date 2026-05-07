# Project: danse-et-musique-de-laille.github.io

Nuxt 3 static site for an association. Content lives in Notion + S3 and is cached at build time; the deployed site is fully static (`nuxt generate`).

## Stack

- Nuxt 3, Vue 3, TypeScript
- Tailwind v3 via `@nuxtjs/tailwindcss`
- Pinia (`@pinia/nuxt`)
- `@nuxt/content`, `@nuxt/image`, `@nuxt/icon`
- `@notionhq/client` + `aws-sdk` (S3) — used at prebuild only
- `fuse.js` for client-side search
- `zod` for schema validation
- No test framework installed yet. Do not assume Vitest exists.

## Build flow

`npm run build` runs `prebuild` first, which:
1. `replace:notion:urls` — rewrites internal Notion URLs to S3 public URLs
2. `cache:notion:databases` — snapshots Notion data to local cache
3. `cache:s3:photos` — caches album photos from S3

Then `nuxt build` consumes the cached data. Production uses `nuxt generate` (static).

Source of truth for content is Notion. Code should read from the cached snapshots, not call Notion at runtime.

## Project layout

```
src/
├── app.vue              # root layout (Header / NuxtPage / Footer)
├── pages/               # file-based routing
├── components/          # presentation components
├── composables/         # screen orchestration (useDanses, ...)
├── models/              # typed domain shapes (Album, Cours, Danse)
├── server/              # Nitro server routes (currently minimal)
├── public/
└── nuxt.config.ts
scripts/                 # prebuild Notion/S3 sync scripts
```

## Reference material under `.claude/`

The `.claude/rules/` and `.claude/skills/` content was imported from the `letstream` project, which is a **C# / .NET 9 / DDD / xUnit** codebase. Treat it as **inspiration, not literal instructions** — the high-level principles transfer; the concrete syntax and tooling do not.

### `.claude/skills/vue-project-guidelines/`

Written for a Vite + heavy Clean-Architecture app. For this repo:

- **Folder mapping**: the skill's `Presentation/components`, `Presentation/composables`, `Presentation/views` correspond here to Nuxt's flat `components/`, `composables/`, `pages/`. Do not introduce a `Presentation/` directory — it fights Nuxt auto-imports.
- **`App.vue` vs `app.vue`**: Nuxt uses lowercase `app.vue` and there is no `main.ts`. The "thin App.vue" rule still applies.
- **BusinessLogic / SecondaryAdapters / UseCases**: overkill for a content site. Apply only if a feature genuinely warrants it (e.g., a real interactive flow). Default split here is `models/` (types) + `composables/` (orchestration) + `server/` (Nitro adapters) + `scripts/` (build-time adapters).
- **CommandHandler naming convention**: skip. Use plain function names (`fetchDanses`, `buildAgenda`) consistent with existing `useDanses.ts`.
- **Pinia vs composable**: skill's rule applies as-is. Pinia is already installed; reach for it only when state is shared across pages.
- **Vue Query**: not installed. Don't suggest it without a real reason — most data is build-time cached, not runtime-fetched.
- **Testing strategy**: the skill assumes Vitest. There is no test setup here yet. Don't write tests until the framework is added; if asked to add tests, set up Vitest first and confirm the approach.
- **`erasableSyntaxOnly` / parameter properties**: not configured here, but the explicit-field style is fine to follow anyway.

### `.claude/rules/`

| File | Transfers to TS/Nuxt? | Notes |
|------|----------------------|-------|
| `IDENTITY.md` | **partially** — ignore the literal "C# / .NET 9" framing. The mindset (craftsman, domain-first, simplicity) transfers. |
| `ARCHITECTURE.md` | **partially** — the dependency rule, ports/adapters, and "infrastructure adapts to domain" generalize. The specific layer names map to the folder split above. Don't introduce CQRS or transaction boundaries on a static content site. |
| `CODE-STYLE.md` | **mostly C#-only** — `record struct`, `IReadOnlyList<T>`, `ArgumentNullException.ThrowIfNull`, `internal` visibility, `[Fact]` test bodies are not relevant here. The conceptual rules (immutability by default, no anemic models, no primitive obsession, single-responsibility, small methods) transfer. |
| `ANTI-PATTERNS.md` | **mostly transferable** — anemic models, smart controllers, primitive obsession, god classes, long parameter lists all apply to TS too. Skip the EF Core / aggregate-reference items. |
| `ENFORCEMENT.md` | **do not apply literally** — describes a TDD state machine with mandatory user gates ("go red" / "go green"). It only makes sense alongside the TDD skills + agents and a real test harness. Ignore unless the user explicitly opts into the TDD workflow. |

### `.claude/skills/tdd-*/`, `.claude/agents/tdd-*.md`, `.claude/commands/tdd-*.md`

The TDD skills, the agents that orchestrate them, and the matching slash commands have all been imported. The set is internally consistent (agents reference skills that exist; commands invoke agents that exist), so the workflow is structurally complete.

**What still does not fit this project:**

- Assertion libraries (Shouldly, FluentAssertions), `[Fact]`, sociable-test fakes, and Result patterns are C#-specific.
- The skills assume `dotnet test` and a hexagonal C# layout. This repo has no test framework installed at all (no Vitest, no Playwright).
- The integration/E2E patterns target ASP.NET / TestContainers; nothing here can run them.

**Default behaviour**: do not invoke `/tdd*` commands or the `tdd-*` agents on this project as-is. If the user asks for TDD here:
1. First agree on a TS testing stack (Vitest minimum, optionally Playwright for E2E) and install it.
2. Translate the conventions worth keeping — Given/When/Then helpers, no inline assertions in test bodies, outside-in cycles, RED/GREEN gates — to that TS stack.
3. Borrow the *philosophy* from the skills; do not paste C# patterns verbatim.

## Conventions specific to this repo

- Notion-derived data flows through `models/` types validated with `zod` where appropriate.
- The `Config` class (recently introduced) centralizes runtime configuration — prefer extending it over scattering `process.env` reads.
- Cache files produced by prebuild scripts must not be committed; check `.gitignore` before adding outputs.
