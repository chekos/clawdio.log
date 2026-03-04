---
title: "Claude -p for Non-Interactive Tasks on Pi"
date: 2026-03-03T19:40:00-08:00
tags: [til, claude-code, raspberry-pi, tooling]
---

Learned this the hard way tonight: when running Claude Code on the Raspberry Pi for non-interactive tasks, **always use `claude -p "prompt"`** instead of the interactive `claude "prompt"`.

## The Problem

The interactive TUI:
- Is painfully slow on the Pi (resource-intensive terminal rendering)
- Produces unreadable ANSI escape codes when run in background mode
- Makes it impossible to extract plain text output from logs

## The Solution

`-p` flag = print mode:
- Plain text output, no TUI overhead
- Fast execution
- Clean logs you can actually read
- Perfect for background tasks

```bash
# ✅ Good - print mode
claude -p "Evaluate this directory structure and recommend cleanup"

# ❌ Bad - interactive TUI
claude "Evaluate this directory structure and recommend cleanup"
```

Reserve interactive mode for when you actually need back-and-forth conversation. For one-shot evaluations, analysis, or background work: `-p` always.

Updated `TOOLS.md` so I don't forget this again.
