# 🖤 BlackRoad Foundation — Community Hub

> **Open development. Autonomous AI infrastructure. Community-driven.**

## Status: 🟢 GREEN LIGHT — Production Ready

**Last Updated:** 2026-03-01 | **Maintained By:** BlackRoad OS, Inc.

---

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [npm Packages](#npm-packages)
4. [Stripe Integration](#stripe-integration)
5. [Community Resources](#community-resources)
6. [Contributing](#contributing)
7. [Programs](#programs)
8. [Events](#events)
9. [Community Guidelines](#community-guidelines)
10. [Recognition](#recognition)
11. [Repository Index](#repository-index)
12. [Contact](#contact)

---

## Overview

The **BlackRoad Foundation Community Hub** is the central resource for contributors, users, and partners of the BlackRoad OS ecosystem. This repository provides onboarding documentation, community programs, events, and links to all BlackRoad Foundation resources.

BlackRoad OS is a production-grade, open autonomous AI infrastructure platform. All packages listed here are available on npm and billing/payments are powered by Stripe.

---

## Quick Start

```bash
# Install the BlackRoad OS CLI
npm install -g @blackroad/cli

# Verify installation
blackroad --version
```

For full documentation visit [docs.blackroad.io](https://docs.blackroad.io).

---

## npm Packages

All official BlackRoad OS packages are published to npm under the `@blackroad` scope.

| Package | Description | Version |
|---------|-------------|---------|
| `@blackroad/cli` | Command-line interface for BlackRoad OS | [![npm](https://img.shields.io/npm/v/@blackroad/cli)](https://www.npmjs.com/package/@blackroad/cli) |
| `@blackroad/sdk` | Core SDK for building BlackRoad OS integrations | [![npm](https://img.shields.io/npm/v/@blackroad/sdk)](https://www.npmjs.com/package/@blackroad/sdk) |
| `@blackroad/agents` | Agent runner and orchestration toolkit | [![npm](https://img.shields.io/npm/v/@blackroad/agents)](https://www.npmjs.com/package/@blackroad/agents) |

### Installing a Package

```bash
npm install @blackroad/sdk
```

```js
const { BlackRoadClient } = require('@blackroad/sdk');

const client = new BlackRoadClient({ apiKey: process.env.BLACKROAD_API_KEY });
```

> **Note:** All packages require Node.js 18 or higher.

---

## Stripe Integration

BlackRoad OS uses **Stripe** for all billing, subscriptions, and payments.

### Setup

1. Add your Stripe keys to your environment:

   ```bash
   STRIPE_PUBLISHABLE_KEY=pk_live_...
   STRIPE_SECRET_KEY=sk_live_...
   STRIPE_WEBHOOK_SECRET=whsec_...
   ```

2. Install the Stripe package:

   ```bash
   npm install stripe
   ```

3. Initialize the Stripe client:

   ```js
   const Stripe = require('stripe');
   const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
   ```

### Plans & Pricing

| Plan | Price | Features |
|------|-------|----------|
| **Community** | Free | Open-source access, community support |
| **Pro** | $29/month | Priority support, advanced features |
| **Enterprise** | Custom | Dedicated support, SLAs, custom integrations |

Visit [blackroad.ai/pricing](https://blackroad.ai/pricing) to subscribe or manage your billing.

> ⚠️ **Security:** Never commit Stripe secret keys to source control. Use environment variables or a secrets manager.

---

## Community Resources

- 📖 [Documentation](https://docs.blackroad.io)
- 💬 [Discord](https://discord.gg/blackroad) _(coming soon)_
- 🐦 [Twitter/X](https://x.com/blackroadOS)
- 📧 [Email](mailto:blackroad.systems@gmail.com)
- 💬 [GitHub Discussions](https://github.com/BlackRoad-Foundation/community/discussions)

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for full guidelines, brand standards, and the legal contributor agreement.

**Summary:**
1. Fork the repository (for testing purposes only)
2. Create a feature branch
3. Follow [BlackRoad brand guidelines](./CONTRIBUTING.md)
4. Submit a PR with a detailed description
5. All contributions become the property of BlackRoad OS, Inc.

---

## Programs

| Program | Description | Details |
|---------|-------------|---------|
| 🎓 Developer Fellowship | 3-month paid contribution program ($3,000/month) | [fellowship.md](./programs/fellowship.md) |
| 🏆 Community Champions | Recognition + early access perks | _(coming soon)_ |
| 💰 Foundation Grants | Funding for ecosystem projects ($500–$50,000) | [grants.md](./programs/grants.md) |

---

## Events

| Event | Schedule | Description |
|-------|----------|-------------|
| Community Standup | Every Monday, 9am PT | Discord voice |
| Open Office Hours | First Friday of each month | Q&A with core team |
| BlackRoad Dev Day | TBD | Virtual conference |
| Pi Fleet Hackathon | TBD | Agent hackathon |

See the full [Events Calendar](./events/CALENDAR.md).

---

## Community Guidelines

1. Be respectful and inclusive
2. No spam or self-promotion without permission
3. Keep discussions on-topic
4. Report issues via GitHub Issues
5. Follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/)

---

## Recognition

Top contributors are featured in our monthly newsletter and receive:

- Early access to new features
- BlackRoad swag
- Credits in release notes
- Eligibility for [Developer Fellowship](./programs/fellowship.md)

---

## Repository Index

| File / Directory | Description |
|-----------------|-------------|
| [`README.md`](./README.md) | This file — Community Hub overview and index |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | Contribution guidelines, brand standards, and legal |
| [`TRAFFIC_LIGHT_SYSTEM.md`](./TRAFFIC_LIGHT_SYSTEM.md) | Project status indicator standards |
| [`BLACKROAD_EMOJI_DICTIONARY.md`](./BLACKROAD_EMOJI_DICTIONARY.md) | Official emoji usage standards |
| [`LICENSE`](./LICENSE) | License information |
| [`docs/ONBOARDING.md`](./docs/ONBOARDING.md) | New contributor onboarding guide |
| [`programs/fellowship.md`](./programs/fellowship.md) | Developer Fellowship program details |
| [`programs/grants.md`](./programs/grants.md) | Foundation grants program details |
| [`events/CALENDAR.md`](./events/CALENDAR.md) | Community events calendar |
| [`.github/workflows/`](./.github/workflows/) | CI/CD and automation workflows |

---

## Contact

| Role | Contact |
|------|---------|
| **General Inquiries** | [blackroad.systems@gmail.com](mailto:blackroad.systems@gmail.com) |
| **Foundation** | [foundation@blackroad.ai](mailto:foundation@blackroad.ai) |
| **CEO** | Alexa Amundson |
| **Organization** | BlackRoad OS, Inc. |

---

**© 2025–2026 BlackRoad OS, Inc. All Rights Reserved.**
