# TresoWealth Beta Site - Next Steps

This checklist tracks what needs to be done next to improve the beta site.

## Phase 1: Domain & Deployment ✅ IN PROGRESS

- [x] Fix site structure (served from root, not /tresowealth.com/)
- [x] Set up Git workflow (main = stable, demo = experiments)
- [x] Add foundational SEO files (robots.txt, llms.txt, sitemap.xml, 404.html)
- [x] Add Organization schema for SEO
- [ ] **Connect custom domain: beta.tresowealth.com**
  - Get Cloudflare to work with custom domain
  - Update URLs in schema files when domain is live

## Phase 2: SEO Improvements

- [ ] Add canonical tags to all pages
  - Currently: index.html has `<link rel="canonical" href="index.html">`
  - Should be: proper absolute URLs
- [ ] Generate full sitemap.xml
  - Add all pages as they're created
  - Include proper lastmod dates
- [ ] Add meta descriptions to all pages
- [ ] Optimize page titles for search

## Phase 3: Schema Expansion

- [ ] Add Article schema to blog/content pages
- [ ] Add FAQPage schema for FAQ sections
- [ ] Add FinancialProduct schema for investment products
- [ ] Add LocalBusiness schema for office locations

## Phase 4: CMS Integration

- [ ] Connect Directus CMS
  - Set up content management for easy updates
  - Migrate static content to Directus
  - Enable non-technical team to edit content

## Phase 5: Content Workflow

- [ ] Connect Steve v6 content system
  - Set up brief templates
  - Configure approval workflows
  - Enable automated publishing
- [ ] Connect OpenClaw agents
  - Automated content generation
  - SEO optimization
  - Compliance checking

## Phase 6: Performance & Security

- [ ] Enable HTTPS on custom domain
- [ ] Add security headers
- [ ] Optimize images and assets
- [ ] Add analytics tracking

## Notes

- Always test on `demo` branch before merging to `main`
- Get team approval before major changes
- Keep the Framer production site (tresowealth.com) untouched until beta is approved
- All changes should be deployed to beta URL first

---

**Last Updated**: 2026-04-23
**Current Status**: Phase 1 (Foundation) nearly complete
