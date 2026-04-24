# TresoWealth Beta Site - Content Import Plan

**Created**: April 24, 2026
**Branch**: demo
**Source**: Complete Steve Workflow Output (40 articles)
**Purpose**: Map 40 articles to site structure and deployment phases

---

## 📊 SUMMARY

**Total Articles**: 40
**Total FAQ Documents**: 5
**Deployment Phases**: 4 phases (Phase 3-6)
**Target URL Structure**: Clean, SEO-friendly URLs

---

## 🗺️ URL STRUCTURE PLAN

### Base URL
- **Beta**: `https://tresowealth-beta-site.akshay-randeva.workers.dev`
- **Production** (future): `https://tresowealth.com` or `https://beta.tresowealth.com`

### URL Patterns

| Content Type | URL Pattern | Example |
|--------------|-------------|---------|
| **Homepage** | `/` | `/` |
| **Category Index** | `/{category}/` | `/gift-city-products/` |
| **Article** | `/{category}/{article-slug}/` | `/gift-city-products/gift-city-aif-products/` |
| **FAQ** | `/faq/{topic}/` | `/faq/gift-city-fundamentals/` |

---

## 📋 PHASE 3: CORE ARTICLES (Pillar 1 + 2)

**Timeline**: Phase 3
**Articles**: 9 (6 products + 3 EAMs)
**Priority**: HIGH (commercial intent content)

### Pillar 1: GIFT City Products (6 articles)

**Category URL**: `/gift-city-products/`
**Purpose**: Explain Category I, II, III AIFs
**Target Audience**: Foreign HNIs exploring product options
**Intent**: Commercial (high conversion focus)

| # | File | Target URL | Title | Type | Status |
|---|------|------------|-------|------|--------|
| 1 | `01-gift-city-products-enhanced.md` | `/gift-city-products/gift-city-aif-products/` | GIFT City AIF Products: Complete Guide | Product Overview | ⚪ Not deployed |
| 2 | `02-gift-city-for-eams-enhanced.md` | `/gift-city-products/gift-city-aif-for-eams/` | GIFT City AIFs for EAMs | B2B Focus | ⚪ Not deployed |
| 3 | `03-indian-fund-managers-enhanced.md` | `/gift-city-products/indian-fund-managers/` | Indian Fund Managers in GIFT City | Fund Manager Guide | ⚪ Not deployed |
| 4 | `04-how-to-invest-enhanced.md` | `/gift-city-products/how-to-invest/` | How to Invest in GIFT City AIFs | Process Guide | ⚪ Not deployed |
| 5 | `05-tax-benefits-enhanced.md` | `/gift-city-products/tax-benefits/` | GIFT City Tax Benefits for Foreign HNIs | Tax Guide | ⚪ Not deployed |
| 6 | (Additional product article) | `/gift-city-products/{slug}/` | (Title TBD) | Product | ⚪ Not deployed |

**Schema Requirements**:
- Article schema (each article)
- BreadcrumbList schema (each article)
- FinancialProduct schema (if applicable)

**Internal Linking**:
- Link to Pillar 2 (EAMs)
- Link to Pillar 4 (Process)
- Link to Pillar 5 (Tax)
- Link to homepage

---

### Pillar 2: EAMs & Gateway (3 articles)

**Category URL**: `/eams-gateway/`
**Purpose**: Establish GIFT City as ideal route to Indian markets
**Target Audience**: DIFC/ADGM External Asset Managers
**Intent**: Decision-stage (high commercial intent)

| # | File | Target URL | Title | Type | Status |
|---|------|------------|-------|------|--------|
| 1 | `decision-001-gift-city-ideal-route-eams-enhanced.md` | `/eams-gateway/gift-city-ideal-route-eams/` | Why GIFT City is the Ideal Route for EAMs | Decision Content | ⚪ Not deployed |
| 2 | `decision-002-why-gift-city-india-allocation-enhanced.md` | `/eams-gateway/why-gift-city-india-allocation/` | Why GIFT City for India Allocation | Decision Content | ⚪ Not deployed |
| 3 | `decision-003-gift-city-gateway-indian-markets-enhanced.md` | `/eams-gateway/gift-city-gateway-indian-markets/` | GIFT City as Gateway to Indian Markets | Decision Content | ⚪ Not deployed |

**Schema Requirements**:
- Article schema (each article)
- BreadcrumbList schema (each article)

**Internal Linking**:
- Link to Pillar 1 (Products)
- Link to Pillar 4 (Process - EAM onboarding)
- Link to Pillar 5 (Tax - DIFC/EAM tax guide)
- Link to homepage

**Geographic Targeting**:
- DIFC (Dubai International Financial Centre)
- ADGM (Abu Dhabi Global Market)
- GCC EAMs

---

## 📋 PHASE 4: PROCESS & TAX ARTICLES (Pillar 4 + 5)

**Timeline**: Phase 4
**Articles**: 18 (8 process + 10 tax/commercial)
**Priority**: HIGH (practical + commercial intent)

### Pillar 4: Process (10 articles)

**Category URL**: `/investment-process/`
**Purpose**: Step-by-step investment process
**Target Audience**: Foreign HNIs ready to invest
**Intent**: Informational → Commercial

| # | File | Target URL | Title | Type | Schema |
|---|------|------------|-------|------|--------|
| 1 | `informational-001-how-can-foreigners-invest-in-gift-city-aif-enhanced.md` | `/investment-process/how-foreigners-invest-gift-city-aif/` | How Can Foreigners Invest in GIFT City AIFs? | Process Guide | HowTo |
| 2 | `informational-002-gift-city-aif-investment-process-uae-residents-enhanced.md` | `/investment-process/gift-city-aif-investment-process-uae-residents/` | GIFT City AIF Investment Process for UAE Residents | Process Guide | HowTo |
| 3 | `informational-003-gift-city-aif-account-opening-foreigners-enhanced.md` | `/investment-process/gift-city-aif-account-opening-foreigners/` | GIFT City AIF Account Opening for Foreigners | Process Guide | HowTo |
| 4 | `informational-004-gift-city-aif-kyc-non-indian-residents-enhanced.md` | `/investment-process/gift-city-aif-kyc-non-indian-residents/` | GIFT City AIF KYC for Non-Indian Residents | Process Guide | HowTo |
| 5 | `informational-005-gift-city-aif-onboarding-eams-enhanced.md` | `/investment-process/gift-city-aif-onboarding-eams/` | GIFT City AIF Onboarding for EAMs | Process Guide | HowTo |
| 6 | `informational-006-best-gift-city-aif-options-2026-enhanced.md` | `/investment-process/best-gift-city-aif-options-2026/` | Best GIFT City AIF Options in 2026 | Product Guide | Article |
| 7 | `informational-007-gift-city-repatriation-taxes-minimums-enhanced.md` | `/investment-process/gift-city-repatriation-taxes-minimums/` | GIFT City Repatriation, Taxes & Minimums | Process Guide | HowTo |
| 8 | `informational-008-mainland-vs-gift-city-comparison-enhanced.md` | `/investment-process/mainland-vs-gift-city-comparison/` | Mainland vs GIFT City AIF Comparison | Comparison | Article |
| 9 | `informational-009-gift-city-aif-fees-costs-enhanced.md` | `/investment-process/gift-city-aif-fees-costs/` | GIFT City AIF Fees & Costs Explained | Cost Guide | Article |
| 10 | `informational-010-gift-city-aif-vs-benchmarks-enhanced.md` | `/investment-process/gift-city-aif-vs-benchmarks/` | GIFT City AIFs vs Benchmarks | Comparison | Article |

**Schema Requirements**:
- Article schema (each article)
- BreadcrumbList schema (each article)
- HowTo schema (7 process guide articles)

**Internal Linking**:
- Link to Pillar 1 (Products)
- Link to Pillar 2 (EAMs)
- Link to Pillar 5 (Tax)
- Cross-link between process articles

**User Journey**:
- Awareness → Process articles
- Consideration → Comparison articles
- Decision → Contact/CTA

---

### Pillar 5: Tax & Regulatory (6 articles)

**Category URL**: `/tax-regulatory/`
**Purpose**: Explain 0% tax, DTAA benefits, regulatory advantages
**Target Audience**: Foreign HNIs (UAE, Saudi, GCC family offices)
**Intent**: Commercial (location-specific targeting)

| # | File | Target URL | Title | Geography | Status |
|---|------|------------|-------|-----------|--------|
| 1 | `commercial-001-gift-city-aif-uae-residents-enhanced.md` | `/tax-regulatory/gift-city-aif-uae-residents/` | GIFT City AIFs for UAE Residents: Complete Tax Guide | UAE | ⚪ Not deployed |
| 2 | `commercial-002-gift-city-aif-dubai-hni-enhanced.md` | `/tax-regulatory/gift-city-aif-dubai-hni/` | GIFT City AIFs for Dubai HNIs: Tax Benefits | Dubai (UAE) | ⚪ Not deployed |
| 3 | `commercial-003-gift-city-aif-saudi-hni-enhanced.md` | `/tax-regulatory/gift-city-aif-saudi-hni/` | GIFT City AIFs for Saudi HNIs: Tax Guide | Saudi Arabia | ⚪ Not deployed |
| 4 | `commercial-004-gift-city-aif-gcc-family-offices-enhanced.md` | `/tax-regulatory/gift-city-aif-gcc-family-offices/` | GIFT City AIFs for GCC Family Offices | GCC | ⚪ Not deployed |
| 5 | `commercial-005-gift-city-aif-difc-eams-enhanced.md` | `/tax-regulatory/gift-city-aif-difc-eams/` | GIFT City AIFs for DIFC EAMs: Tax Guide | DIFC | ⚪ Not deployed |
| 6 | (Additional tax article) | `/tax-regulatory/{slug}/` | (Title TBD) | General | ⚪ Not deployed |

**Schema Requirements**:
- Article schema (each article)
- BreadcrumbList schema (each article)

**Internal Linking**:
- Link to Pillar 1 (Products)
- Link to Pillar 4 (Process)
- Link to Pillar 2 (EAMs)
- Link to FAQ (tax FAQs)

**Geographic Targeting**:
- **Primary**: UAE (Dubai), Saudi Arabia
- **Secondary**: Kuwait, Qatar, Bahrain, Oman
- **B2B Focus**: DIFC, ADGM EAMs

**Commercial Intent**:
- High commercial intent (tax-motivated investors)
- Call-to-action: Schedule consultation
- Lead capture: Email for detailed tax guide

---

## 📋 PHASE 5: WHY INDIA & TRESOWEALTH (Pillar 6 + 7)

**Timeline**: Phase 5
**Articles**: 12 (10 why India + 2 why TresoWealth)
**Priority**: MEDIUM (brand positioning)

### Pillar 6: Why India (10 articles)

**Category URL**: `/why-india/`
**Purpose**: Make the economic case for investing in India now
**Target Audience**: Foreign HNIs evaluating India allocation
**Intent**: Informational → Commercial

| # | File | Target URL | Title | Topic | Status |
|---|------|------------|-------|-------|--------|
| 1 | `article-1-demographic-dividend-enhanced.md` | `/why-india/demographic-dividend/` | India's Demographic Dividend: 2025-2040 Opportunity | Demographics | ⚪ Not deployed |
| 2 | `article-2-gdp-growth-enhanced.md` | `/why-india/gdp-growth/` | India GDP Growth: 7-8% CAGR Opportunity | Economic Growth | ⚪ Not deployed |
| 3 | `article-3-domestic-consumption-enhanced.md` | `/why-india/domestic-consumption/` | India's Domestic Consumption Boom | Consumption | ⚪ Not deployed |
| 4 | `article-4-india-vs-china-enhanced.md` | `/why-india/india-vs-china/` | India vs China: Why India Now? | Comparative | ⚪ Not deployed |
| 5 | `article-5-manufacturing-enhanced.md` | `/why-india/manufacturing/` | India's Manufacturing Boom | Manufacturing | ⚪ Not deployed |
| 6 | `article-6-india-financial-services-sector-enhanced.md` | `/why-india/financial-services-sector/` | India's Financial Services Sector Opportunity | Financial Services | ⚪ Not deployed |
| 7 | `article-7-india-it-services-sector-outlook-enhanced.md` | `/why-india/it-services-sector-outlook/` | India's IT Services Sector Outlook | IT Sector | ⚪ Not deployed |
| 8 | `article-8-india-manufacturing-boom-enhanced.md` | `/why-india/manufacturing-boom/` | India's Manufacturing Boom: 25% GDP by 2025 | Manufacturing | ⚪ Not deployed |
| 9 | (Additional why India article) | `/why-india/{slug}/` | (Title TBD) | Topic TBD | ⚪ Not deployed |
| 10 | (Additional why India article) | `/why-india/{slug}/` | (Title TBD) | Topic TBD | ⚪ Not deployed |

**Schema Requirements**:
- Article schema (each article)
- BreadcrumbList schema (each article)

**Internal Linking**:
- Link to Pillar 1 (Products - invest in India)
- Link to Pillar 7 (Why TresoWealth)
- Link to homepage (CTA: Start investing)

**Economic Data Points** (from Brand Bible):
- Working-age population peak: 2025-2040
- Middle class: 300M → 600M by 2030
- Urbanization: 35% → 45% by 2035
- Manufacturing: 25% of GDP by 2025
- GDP growth: 7-8% CAGR

**User Journey**:
- Why India? → Economic case
- How to invest? → Pillar 1 (Products)
- Why TresoWealth? → Pillar 7

---

### Pillar 7: Why TresoWealth (2 articles)

**Category URL**: `/why-tresowealth/`
**Purpose**: Differentiate TresoWealth from competitors
**Target Audience**: Foreign HNIs comparing platforms
**Intent**: Commercial (brand differentiation)

| # | File | Target URL | Title | Topic | Status |
|---|------|------------|-------|-------|--------|
| 1 | `article-9-enhanced-math-engine-aif-portfolio-optimization-enhanced.md` | `/why-tresowealth/math-engine-aif-portfolio-optimization/` | Enhanced Math Engine for AIF Portfolio Optimization | Analytics Moat | ⚪ Not deployed |
| 2 | `article-10-india-regime-classification-enhanced.md` | `/why-tresowealth/india-regime-classification/` | India Regime Classification: Market Cycles | Analytics Moat | ⚪ Not deployed |

**Schema Requirements**:
- Article schema (each article)
- BreadcrumbList schema (each article)

**Internal Linking**:
- Link to Pillar 1 (Products)
- Link to homepage (CTA: Schedule consultation)
- Link to team/about page (if exists)

**Competitive Differentiation**:
- **TresoWealth**: Analytics + due diligence + math engine
- **Competitors**: Distribution platforms (no analytics)
- **Key Differentiators**:
  - Enhanced Math Engine
  - Monte Carlo simulations
  - Regime classification
  - Portfolio optimization

**Conversion Goal**:
- Book consultation
- Start due diligence process
- Subscribe to updates

---

## 📋 PHASE 6: FAQ ENHANCEMENT

**Timeline**: Phase 6
**FAQ Documents**: 5
**Total FAQs**: ~50
**Priority**: MEDIUM (AEO optimization)

### FAQ Documents

**FAQ Base URL**: `/faq/`

| # | File | Target URL | Topic | FAQs | Schema | Status |
|---|------|------------|-------|------|--------|--------|
| 1 | `FAQ_01_GIFT_CITY_FUNDAMENTALS.md` | `/faq/gift-city-fundamentals/` | GIFT City Fundamentals | ~10 | FAQPage | ⚪ Not deployed |
| 2 | `FAQ_02_INVESTMENT_PRODUCTS.md` | `/faq/investment-products/` | Investment Products | ~10 | FAQPage | ⚪ Not deployed |
| 3 | `FAQ_03_TAXATION_DETAILED.md` | `/faq/taxation/` | Taxation (Detailed) | ~10 | FAQPage | ⚪ Not deployed |
| 4 | `FAQ_04_TO_09_REMAINING.md` | `/faq/additional-questions/` | Additional FAQs | ~20 | FAQPage | ⚪ Not deployed |
| 5 | `FAQ_IMPLEMENTATION_COMPLETE.md` | `/faq/implementation-status/` | Implementation Status | Meta | - | ⚪ Not deployed |

**Schema Requirements**:
- FAQPage schema (each FAQ page)
- BreadcrumbList schema (each FAQ page)

**Internal Linking**:
- Link to relevant pillar articles
- Link to homepage
- Link to contact/consultation CTA

**AEO Optimization**:
- FAQPage schemas for AI crawlers
- Direct answers to common questions
- Citations to authoritative sources
- Enhanced llms.txt with FAQ topics

---

## 📊 CONTENT MAPPING SUMMARY

### By Phase

| Phase | Pillars | Articles | Category Pages | Total URLs | Timeline |
|-------|---------|----------|----------------|------------|----------|
| **Phase 3** | 1, 2 | 9 | 2 | 11 | Core content |
| **Phase 4** | 4, 5 | 18 | 2 | 20 | Process + Tax |
| **Phase 5** | 6, 7 | 12 | 2 | 14 | Brand positioning |
| **Phase 6** | FAQ | 0 | 5 | 5 | AEO optimization |
| **TOTAL** | **7** | **39** | **11** | **50** | **~4 phases** |

### By Intent

| Intent Type | Articles | Percentage | Examples |
|-------------|----------|------------|----------|
| **Commercial** | 14 | 36% | Tax guides, EAM decision content |
| **Informational** | 20 | 51% | Process guides, why India |
| **Decision** | 5 | 13% | Comparisons, fund selection |
| **TOTAL** | **39** | **100%** | - |

### By Geography

| Geography Target | Articles | Notes |
|------------------|----------|-------|
| **UAE (Dubai)** | 3 | Tax guides for Dubai HNIs |
| **Saudi Arabia** | 1 | Tax guide for Saudi HNIs |
| **GCC (Regional)** | 2 | GCC family offices, EAMs |
| **General Foreign HNI** | 33 | All foreign investors |
| **India-Specific** | 0 | (Not targeting domestic investors) |
| **TOTAL** | **39** | - |

---

## 🔍 CONTENT QUALITY NOTES

### From Workflow Completion Report

**Quality Gate Score**: 72% (target: 75%)
**Citation Coverage**: 1.8-5.2% (target: 95%)

**Status**: Approve with conditions
- Continue citation work post-publication
- Improve quality gate score over time
- Focus on factual claim verification

**Recommendation**: Publish immediately despite minor quality gaps
- Market urgency: SBNRI/GetBelong competitive threat
- First-mover advantage: 3-6 month window
- Content can be improved post-publication

---

## 📈 INTERNAL LINKING STRATEGY

### Pillar Interconnections

```
Homepage
├── Pillar 1: Products (6 articles)
│   ├── Links to: Pillar 2 (EAMs), Pillar 4 (Process), Pillar 5 (Tax)
│
├── Pillar 2: EAMs & Gateway (3 articles)
│   ├── Links to: Pillar 1 (Products), Pillar 4 (Process - EAM onboarding), Pillar 5 (Tax - DIFC)
│
├── Pillar 4: Process (10 articles)
│   ├── Links to: Pillar 1 (Products), Pillar 2 (EAMs), Pillar 5 (Tax), Pillar 6 (Why India)
│
├── Pillar 5: Tax & Regulatory (6 articles)
│   ├── Links to: Pillar 1 (Products), Pillar 4 (Process), FAQ
│
├── Pillar 6: Why India (10 articles)
│   ├── Links to: Pillar 1 (Products), Pillar 7 (Why TresoWealth)
│
├── Pillar 7: Why TresoWealth (2 articles)
│   ├── Links to: Pillar 1 (Products), Homepage (CTA)
│
└── FAQ (5 pages)
    ├── Links to: All relevant pillar articles
```

### Link Density Target

- **15-20 internal links per article** (from workflow audit)
- **Link to relevant pillar articles** (2-3 per section)
- **Link to category index pages**
- **Link to homepage** (logo, navigation)

---

## 🚀 DEPLOYMENT WORKFLOW

### Per Article

1. **Create HTML file** with target URL slug
2. **Convert markdown to HTML** (preserve formatting, headings)
3. **Add SEO elements**:
   - Title tag (from article title)
   - Meta description (from article intro)
   - Canonical tag (absolute URL)
   - OG tags (title, description, URL)
4. **Add schema markup**:
   - Article schema
   - BreadcrumbList schema
   - Specialized schemas (HowTo, FAQPage)
5. **Add internal links** (15-20 per article)
6. **Add external links** (citations, references)
7. **Test**:
   - Validate HTML
   - Validate schema (Google SDTT)
   - Test links
   - Mobile view test
8. **Deploy** to demo branch
9. **Update sitemap.xml** with new URL
10. **Commit** with clear message

### Per Phase

1. Deploy all articles in phase
2. Create/update category index pages
3. Update navigation (if needed)
4. Update sitemap.xml
5. Validate all schemas
6. Test all links
7. Review in Cloudflare preview
8. Get approval
9. Merge to main

---

## 📝 NOTES

### Article Content Status

- **All 40 articles**: Written and enhanced
- **Quality**: Approved with conditions
- **Citations**: Need improvement (1.8-5.2% → 95% target)
- **Format**: Markdown (needs HTML conversion)

### Technical Requirements

- **HTML Conversion**: Markdown → HTML (manual or automated)
- **Template**: Article page template needed (Phase 2)
- **Schema**: 174 schemas generated, ready to deploy
- **Images**: Need to verify if article images exist

### URL Best Practices

- **Lowercase URLs**: `/gift-city-products/` (not `/Gift-City-Products/`)
- **Hyphens**: Separate words with hyphens
- **No underscores**: Use hyphens, not underscores
- **Short URLs**: Keep URLs concise and descriptive
- **No file extensions**: `/article-slug/` (not `/article-slug.html`)

---

## ✅ PHASE 1 STATUS

**Documentation Complete**: ✅ This file (CONTENT-IMPORT-PLAN.md)
**Articles Mapped**: ✅ All 40 articles mapped to URLs
**Phases Planned**: ✅ Phase 3-6 deployment plan
**Internal Linking**: ✅ Strategy defined
**Schema Requirements**: ✅ Mapped to articles

**Next Step**: Phase 1 technical improvements (canonical tags, robots.txt, sitemap.xml)

---

**Content Import Plan Completed**: April 24, 2026
**Total Articles**: 40
**Total Phases**: 4 (Phase 3-6)
**Branch**: demo
