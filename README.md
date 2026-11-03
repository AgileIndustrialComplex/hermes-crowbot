# hermes-crowbot

[Hermes Agent](https://github.com/NousResearch/hermes-agent) model-provider plugin for
**[crowbot.sh](https://crowbot.sh/)**: frontier models plus the uncensored open models
with their refusals removed. Balance top-ups accept crypto or card.

The API is OpenAI-compatible at `https://api.crowbot.sh/v1`; your 16-digit account
number is the API key. One install covers every Hermes surface — CLI, TUI, desktop
app, and gateway all load provider plugins from the shared agent core.

## What the plugin does

- Registers `crowbot` as a native provider: `hermes -m crowbot/kimi-k3` — no
  `custom:` config blocks, no base-URL juggling
- Pins the default reasoning effort to `medium` (kimi-k3 behind a relay otherwise
  defaults to `max` — ~3× the reasoning tokens and latency)
- Exposes the full effort ladder (`none` … `max`) without clamping
- Ships `kimi-k3` as a fallback model so the picker works offline

## Install

```bash
git clone https://github.com/AgileIndustrialComplex/hermes-crowbot.git \
  ~/.hermes/plugins/model-providers/crowbot
```

## Configure

Set your 16-digit crowbot account number in `~/.hermes/.env`:

```bash
CROWBOT_API_KEY=xxx
```

(`HERMES_CUSTOM_API_CROWBOT_SH_API_KEY` is also accepted, for configs migrated from
the generic `custom` provider.)

Then:

```bash
hermes model        # pick crowbot / kimi-k3
# or
hermes -m crowbot/kimi-k3
```

Migrating from `custom`: remove the `custom_providers:` entry and the
`model.base_url`/`model.api_key` lines from `config.yaml`, set `model.provider: crowbot`.

## License

MIT
