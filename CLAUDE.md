# CLAUDE.md

This file provides guidance for AI assistants working with the BlackRoad-Foundation community repository.

## Project Overview

**Repository**: `BlackRoad-Foundation/community`
**Purpose**: Community guidelines and engagement tools for the BlackRoad ecosystem
**Status**: Early development phase (newly initialized)

## Codebase Structure

```
community/
├── .git/              # Git repository data
├── .gitignore         # Git ignore rules
├── README.md          # Project overview and quick start
└── CLAUDE.md          # This file - AI assistant guidance
```

### Key Files

- **README.md**: Public-facing documentation with project description and quick start guide
- **.gitignore**: Standard ignores for Node.js projects (node_modules/, .env files, dist/, build/, logs)

## Development Workflows

### Getting Started

This project is in early development. The codebase structure will evolve as features are added.

### Git Workflow

1. **Branch naming**: Use descriptive branch names prefixed by type:
   - `feature/` - New features
   - `fix/` - Bug fixes
   - `docs/` - Documentation updates
   - `claude/` - AI-assisted development branches

2. **Commit messages**: Follow conventional commits format:
   - `feat:` - New features
   - `fix:` - Bug fixes
   - `docs:` - Documentation changes
   - `chore:` - Maintenance tasks
   - `refactor:` - Code refactoring

3. **Push commands**: Always use `git push -u origin <branch-name>`

### Environment Configuration

- Environment files (`.env`, `.env.local`) are gitignored for security
- Never commit secrets or API keys to the repository

## Conventions for AI Assistants

### Code Style

- Keep solutions simple and focused on the task at hand
- Avoid over-engineering or adding unnecessary abstractions
- Follow existing patterns in the codebase when they exist

### File Operations

- Prefer editing existing files over creating new ones
- Read files before modifying them to understand context
- Use descriptive, conventional commit messages

### Documentation

- Keep documentation concise and actionable
- Update relevant docs when making significant changes
- Don't create unnecessary markdown files

### Security

- Never commit sensitive data (API keys, credentials, tokens)
- Be cautious with command injection, XSS, SQL injection risks
- Validate input at system boundaries

## Organization Context

This repository is part of the **BlackRoad-Foundation** organization within the **BlackRoad Ecosystem**.

### Related Resources

- Organization: [github.com/BlackRoad-Foundation](https://github.com/BlackRoad-Foundation)

## Future Development Areas

As this project grows, expect development in:

- Community guidelines documentation
- Engagement tools and utilities
- Contribution templates and workflows
- Community management resources

---

*Last updated: January 2026*
