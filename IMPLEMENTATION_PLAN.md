# TresoWealth Beta Site - Steve Workflow Implementation Plan

**Created**: April 24, 2026
**Status**: PHASE 1 (Foundation)
**Branch**: demo
**Source**: Complete Steve Workflow Output (88 files, 40 articles)

---

## 📊 EXECUTIVE SUMMARY

This plan maps the complete Steve workflow output (~37,500 words, 88 files, 40 articles) into practical implementation phases for the TresoWealth static beta site. The workflow produces a comprehensive content marketing system for GIFT City AIF investments targeting foreign HNIs.

**Critical Market Context**:
- Two new competitors (SBNRI, GetBelong) entered 2024
- 254 keywords completely untapped (100% market gap)
- 3-6 month window to establish first-mover advantage
- **Recommendation from workflow**: PUBLISH IMMEDIATELY

---

## 🎯 IMPLEMENTATION STRATEGY

### Core Principles

1. **Conservative & Safe**: Work on demo branch only, preserve working site
2. **Phased Approach**: Implement in logical phases, not all at once
3. **Non-Coder Friendly**: Simple explanations, clear commits, reversible changes
4. **No Rebuilds**: Enhance existing static site, don't rebuild from scratch
5. **Always Working**: Site must function at all times

### Branch Workflow

- **main**: Stable beta (production)
- **demo**: Experiments and phase implementations
- **Process**: Implement on demo → Test → Review → Merge to main after approval

---

## 📋 PHASE BREAKDOWN

### PHASE 1: Foundation & Audit ✅ CURRENT

**Goal**: Audit current site, create inventory, improve technical foundation

**Timeline**: 1-2 hours
**Risk**: Low (safe improvements only)

**Deliverables**:
- ✅ IMPLEMENTATION_PLAN.md (this file)
- ✅ PAGE_INVENTORY.md (current site structure)
- ✅ SCHEMA-INVENTORY.md (what exists vs needed)
- ✅ CONTENT-IMPORT-PLAN.md (40 articles mapped to site structure)
- ✅ Improve canonical tags (relative → absolute URLs)
- ✅ Enhance robots.txt (add crawl-delay, clean up)
- ✅ Update sitemap.xml (fix URLs, add priority)
- ✅ Verify Organization schema (check for duplicates)

**Changes**:
- Technical SEO improvements only
- No content published yet
- No structural changes
- Site works exactly as before (better SEO)

**Review Points**:
- Check canonical tags are absolute URLs
- Verify robots.txt allows crawling
- Test sitemap.xml in browser
- Validate Organization schema with Google SDTT

---

### PHASE 2: Content Structure Setup

**Goal**: Create URL structure and page templates for 40 articles

**Timeline**: 2-3 hours
**Risk**: Medium (new pages, no content yet)

**Deliverables**:
- Create clean URL structure: `/gift-city-products/`, `/eams-gateway/`, etc.
- Create article page templates (HTML with proper SEO)
- Add breadcrumb navigation
- Create category/index pages for each pillar
- Set up internal linking framework

**Changes**:
- New empty/placeholder pages
- URL structure created
- Navigation added
- No actual content published

**Review Points**:
- Check all new pages load (404 if empty is OK)
- Verify breadcrumb structure
- Test navigation links
- Confirm no broken links

---

### PHASE 3: Publish Core Articles (Pillar 1 + 2)

**Goal**: Publish first 9 high-priority articles (6 products + 3 EAMs)

**Timeline**: 3-4 hours
**Risk**: Medium (first real content)

**Articles to Publish**:
- **Pillar 1: Products** (6 articles) - Category I/II/III AIFs, comparisons
- **Pillar 2: EAMs & Gateway** (3 articles) - DIFC/ADGM route to India

**Deliverables**:
- 9 published articles with full SEO
- Article schema for each page
- BreadcrumbList schema for each page
- Internal linking between articles
- FAQ sections added

**Changes**:
- 9 new content pages live
- Sitemap updated with 9 new URLs
- Schema markup deployed
- Internal links created

**Review Points**:
- Read 2-3 articles for quality
- Check schema with Google SDTT
- Verify all links work
- Test mobile view

---

### PHASE 4: Publish Process & Tax Articles (Pillar 4 + 5)

**Goal**: Publish 14 articles (8 process + 6 tax)

**Timeline**: 3-4 hours
**Risk**: Medium (more content)

**Articles to Publish**:
- **Pillar 4: Process** (8 articles) - KYC, onboarding, repatriation
- **Pillar 5: Tax & Regulatory** (6 articles) - UAE, Saudi, GCC tax guides

**Deliverables**:
- 14 published articles with HowTo schemas
- FAQPage schemas for tax FAQs
- Enhanced internal linking
- Commercial intent optimization

**Changes**:
- 14 new content pages live
- Process guide schemas added
- Tax calculators referenced
- Regional targeting (UAE, Saudi, GCC)

**Review Points**:
- Check process articles are clear
- Verify tax claims have citations
- Test FAQ schemas
- Confirm regional targeting works

---

### PHASE 5: Publish Why India & TresoWealth (Pillar 6 + 7)

**Goal**: Publish 12 articles (10 why India + 2 why TresoWealth)

**Timeline**: 2-3 hours
**Risk**: Low (brand positioning content)

**Articles to Publish**:
- **Pillar 6: Why India** (10 articles) - GDP growth, demographics, sectors
- **Pillar 7: Why TresoWealth** (2 articles) - Analytics moat, differentiation

**Deliverables**:
- 12 published articles
- Enhanced Organization schema
- FinancialProduct schemas referenced
- Brand positioning complete

**Changes**:
- 12 new content pages live
- Economic data cited
- Competitive differentiation clear
- Full topical authority established

**Review Points**:
- Verify economic claims are cited
- Check competitive differentiation is clear
- Test all internal links
- Confirm brand consistency

---

### PHASE 6: FAQ Enhancement

**Goal**: Deploy 5 comprehensive FAQ documents with FAQPage schemas

**Timeline**: 1-2 hours
**Risk**: Low (FAQ content)

**Deliverables**:
- 5 FAQ pages published
- FAQPage schemas deployed (50 FAQs total)
- Enhanced internal linking to FAQs
- AEO optimization complete

**Changes**:
- FAQ pages live
- Rich snippets enabled
- AI crawler optimization complete

**Review Points**:
- Test FAQ rich snippets preview
- Verify FAQ answers match articles
- Check internal links to FAQs
- Validate FAQPage schemas

---

### PHASE 7: Tool Implementation (Future)

**Goal**: Build interactive tax calculator and eligibility checker

**Timeline**: 8-12 hours (development)
**Risk**: High (requires development)

**Tools to Build**:
- Combined Tax & Cost Analyzer (lead generation)
- Eligibility Checker (qualification)

**Deliverables**:
- Interactive calculators
- Lead capture forms
- Integration with CRM
- Conversion tracking

**Status**: SPECIFICATION ONLY (not building in this plan)

---

### PHASE 8: CMS Migration (Future)

**Goal**: Migrate from static HTML to Directus CMS

**Timeline**: 15-20 hours (setup + migration)
**Risk**: High (infrastructure change)

**Deliverables**:
- Directus CMS installed
- Content migrated
- Workflow automation
- Non-coder editing enabled

**Status**: FUTURE PHASE (not in current scope)

---

## 📊 CONTENT INVENTORY SUMMARY

### Total Articles: 40

| Pillar | Count | Priority | Phase |
|--------|-------|----------|-------|
| Pillar 1: Products | 6 | HIGH | Phase 3 |
| Pillar 2: EAMs & Gateway | 3 | HIGH | Phase 3 |
| Pillar 3: Fund Managers | 0 | MEDIUM | Future |
| Pillar 4: Process | 8 | HIGH | Phase 4 |
| Pillar 5: Tax & Regulatory | 6 | HIGH | Phase 4 |
| Pillar 6: Why India | 10 | MEDIUM | Phase 5 |
| Pillar 7: Why TresoWealth | 2 | MEDIUM | Phase 5 |
| FAQ | 5 | MEDIUM | Phase 6 |

### Total Pages After Implementation: ~55

- Homepage: 1 (exists)
- Article pages: 40 (new)
- FAQ pages: 5 (new)
- Category/index pages: 7 (new)
- Tool pages: 2 (future)
- **Total**: ~55 pages

---

## 🔍 TECHNICAL AUDIT FINDINGS

### Current Site Status (from workflow)

**Technical Score**: 100/100 (Phase 0 audit)
**Status**: Ready for content production

**What Works** ✅:
- Mobile optimization: 85/100
- SSL/HTTPS: 100/100
- Robots.txt: 100/100
- Sitemap.xml: 100/100
- URL structure: 90/100
- Image optimization: 80/100
- Caching: 85/100

**What Needs Improvement** ⚠️:
- Canonical tags: 50/100 (relative URLs, need absolute)
- Schema markup: Was 0/100 (now fixed with Organization schema)
- llms.txt: Was 0/100 (now fixed)
- Internal linking: 40/100 (will improve with content)

---

## 📈 EXPECTED IMPACT

### SEO Impact (3-6 months after Phase 5)

- **Keyword Rankings**: 254 keywords targeted
- **Organic Traffic**: 500+ monthly visitors expected
- **Domain Authority**: 7-pillar system builds authority
- **Engagement**: >3 min avg time, <60% bounce rate

### Lead Generation

- **Tax Calculator**: 5-10% conversion rate (Phase 7)
- **Commercial Articles**: High-intent content (Phases 3-5)
- **Eligibility Checker**: Qualifies leads (Phase 7)

### Competitive Moat

- **First-Mover Advantage**: Publish before SBNRI/GetBelong expand
- **Content Depth**: 55 pages vs competitors' 1-5 pages
- **Audience Focus**: Foreign HNIs (not NRIs like competitors)

---

## ✅ PHASE 1 DELIVERABLES CHECKLIST

### Documentation (4 files)
- [x] IMPLEMENTATION_PLAN.md - This file
- [ ] PAGE_INVENTORY.md - Current site structure audit
- [ ] SCHEMA-INVENTORY.md - Schema deployment status
- [ ] CONTENT-IMPORT-PLAN.md - 40 articles mapped to URLs

### Technical Improvements
- [ ] Fix canonical tags (relative → absolute)
- [ ] Enhance robots.txt (clean up, add crawl-delay)
- [ ] Update sitemap.xml (fix URLs, add changefreq/priority)
- [ ] Verify Organization schema (check for duplicates, validate)

### Git Workflow
- [ ] All commits on demo branch only
- [ ] Logical commit messages (one per improvement)
- [ ] Push demo branch at end
- [ ] Summary of changes provided

---

## 🚀 NEXT STEPS AFTER PHASE 1

### Immediate (After Approval)
1. Review Cloudflare preview of Phase 1 changes
2. Test all technical improvements
3. Validate schema with Google SDTT
4. Approve merge to main

### Phase 2 Preparation
1. Plan URL structure for articles
2. Design page templates
3. Set up navigation framework
4. Create breadcrumb system

---

## 📝 NOTES

### Important Constraints

- **Do NOT rebuild site**: Enhance existing static structure
- **Do NOT publish all 40 articles at once**: Phased approach
- **Do NOT break existing site**: Always working
- **Do NOT merge to main without approval**: Demo branch first

### Workflow Source Documents

This plan is based on complete Steve workflow output:
- 88 files total
- ~37,500 words
- 40 enhanced articles
- 174 schema files generated
- Quality gate framework ready

### Market Urgency

From workflow: **"PUBLISH IMMEDIATELY"** to establish first-mover advantage before SBNRI/GetBelong expand into AIF content (3-6 month window).

---

**Status**: ✅ PHASE 1 IN PROGRESS
**Next Phase**: PHASE 2 (Content Structure Setup)
**Branch**: demo
**Last Updated**: April 24, 2026
