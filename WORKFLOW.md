# TresoWealth Beta Site - Git Workflow

## Branch Strategy

### `main` Branch
- **Purpose**: Stable beta site (production-ready)
- **When to use**: Deployed to Cloudflare at https://tresowealth-beta-site.akshay-randeva.workers.dev/
- **Protection**: Only merge approved changes after testing

### `demo` Branch
- **Purpose**: Experiments, previews, team demos
- **When to use**: Test new features, show team before going live
- **Workflow**: Create feature branches from `demo`, merge back to `demo`

## Safe Change Process

### For New Features or Experiments
1. Create a new branch from `demo`:
   ```bash
   git checkout demo
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit
3. Push to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Test on Cloudflare Pages preview
5. If approved, merge to `demo`:
   ```bash
   git checkout demo
   git merge feature/your-feature-name
   git push origin demo
   ```

### For Merging `demo` to `main` (Only After Approval!)
1. Ensure changes work correctly on `demo` branch
2. Get team approval
3. Merge to main:
   ```bash
   git checkout main
   git pull origin main
   git merge demo
   git push origin main
   ```

## Important Rules

- ✅ **DO**: Test everything on `demo` branch first
- ✅ **DO**: Keep commits clear and descriptive
- ✅ **DO**: Create backup branches before risky changes
- ❌ **DON'T**: Push directly to `main` without testing on `demo`
- ❌ **DON'T**: Merge to `main` without team approval

## Quick Commands

```bash
# See current branch
git branch

# Switch branches
git checkout main
git checkout demo

# See what changed
git status
git diff

# See commit history
git log --oneline
```

## Deployment

- `main` branch → Auto-deploys to production URL
- `demo` branch → Available for preview URLs
- Feature branches → Get automatic Cloudflare preview URLs


---

**Preview deployment trigger**: 2026-04-24
