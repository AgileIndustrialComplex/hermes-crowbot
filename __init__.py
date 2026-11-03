"""Crowbot provider profile — crowbot.sh (OpenAI-compatible API at api.crowbot.sh/v1).

Frontier models plus uncensored open models with refusals removed; balance top-ups
accept crypto or card. Auth: the 16-digit account number is the API key.
"""

from providers import register_provider
from providers.base import ProviderProfile

# Widest OpenAI-compatible wire effort set, mirroring the bundled custom profile
# (kept as a literal so the plugin imports no private core modules).
_OPENAI_COMPAT_WIRE_EFFORTS = ("none", "minimal", "low", "medium", "high", "xhigh", "max")


class CrowbotProfile(ProviderProfile):
    """api.crowbot.sh — OpenAI-compatible relay (kimi-k3, …)."""

    def supported_reasoning_efforts(self, model: str | None) -> tuple[str, ...]:
        """Widest OpenAI-compat wire set (relay vocabulary is undiscoverable), mirroring the
        bundled custom profile — without this, the Responses transport clamps onto the
        OpenAI per-model ladder and silently demotes a configured ``max`` to ``xhigh``."""
        return _OPENAI_COMPAT_WIRE_EFFORTS

    def default_reasoning_config(self, model: str | None = None) -> dict | None:
        """Unset ``agent.reasoning_effort`` → ``medium``.

        kimi-k3 behind an OpenAI-compatible relay defaults to ``max`` — ~3x the
        reasoning tokens and latency of medium. Pin a sane default instead of
        inheriting the endpoint's ceiling.
        """
        return {"enabled": True, "effort": "medium"}


crowbot = CrowbotProfile(
    name="crowbot",
    aliases=("crowbot.sh", "api.crowbot.sh"),
    display_name="Crowbot",
    description="crowbot.sh — frontier + uncensored models (refusals removed), crypto or card top-ups",
    signup_url="https://crowbot.sh/",
    env_vars=("CROWBOT_API_KEY", "HERMES_CUSTOM_API_CROWBOT_SH_API_KEY"),
    base_url="https://api.crowbot.sh/v1",
    hostname="api.crowbot.sh",
    fallback_models=("kimi-k3",),
)

register_provider(crowbot)
