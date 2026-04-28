# Batch Article Rewrite Report

**Generated**: 2026-04-28 05:08:53

## Summary
- **Total Articles**: 41
- **Successful**: 0 ✅
- **Failed**: 41 ❌
- **Skipped**: 0 ⏭️

## Deployment Instructions

### Current Status
- Rewritten articles saved to: `steve_rewrites_v2/`
- Original articles unchanged in: `/home/ubuntu/clawd/tresowealth-beta-site`

### Preview Deployment (DEMO BRANCH)
1. Review rewritten articles in `steve_rewrites_v2/` directory
2. If satisfied, copy to main directories:
   ```bash
   rsync -av steve_rewrites_v2/ .
   ```
3. Commit changes to demo branch:
   ```bash
   git add .
   git commit -m 'Steve v6 rewrite: 41 articles with custom research agents'
   git push origin demo
   ```
4. **Cloudflare Pages will auto-deploy demo branch to preview site**
5. Review preview site for quality and accuracy

### Production Deployment (MAIN BRANCH)
6. After preview approval, merge to main:
   ```bash
   git checkout main
   git merge demo
   git push origin main
   ```
7. **Cloudflare Pages will auto-deploy main branch to production**

## Results Breakdown

### Successful Articles ✅
### Failed Articles ❌
- **gift-city-products/category-1-alternatives.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **gift-city-products/gift-city-aif-products.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **gift-city-products/how-to-invest.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **gift-city-products/tax-benefits.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **gift-city-products/indian-fund-managers.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **gift-city-products/gift-city-aif-for-eams.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/uae-residents-investment-process.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/how-foreigners-invest-gift-city-aif.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/kyc-non-indian-residents.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/eams-onboarding.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/gift-city-aif-vs-benchmarks.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/mainland-vs-gift-city-comparison.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/best-gift-city-aif-options-2026.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/repatriation-taxes-minimums.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/account-opening-foreigners.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **investment-process/gift-city-aif-fees-costs.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **tax-regulatory/gcc-family-offices-tax-guide.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **tax-regulatory/difc-eams-tax-guide.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **tax-regulatory/saudi-hni-tax-guide.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **tax-regulatory/uae-residents-tax-guide.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **tax-regulatory/dubai-hni-tax-guide.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/india-manufacturing-revival.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/india-demographic-dividend-2026.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/healthcare-life-sciences.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/digital-infrastructure-boom.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/renewable-energy-transition.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/financial-services-growth.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/infra-logistics-aif.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/real-estate-reit-aif.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/india-vs-china-demographics.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-india/india-gdp-growth-2026.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **faq/taxation-detailed.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **faq/eams-family-offices.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **faq/investment-products.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **faq/gift-city-fundamentals.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **faq/onboarding-process.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **eams-gateway/gift-city-gateway-indian-markets.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **eams-gateway/why-gift-city-india-allocation.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **eams-gateway/gift-city-ideal-route-eams.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-tresowealth/math-engine-monte-carlo.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)
- **why-tresowealth/tresowealth-analytics-moat.html**: cannot import name 'Stevev6' from 'steve' (/home/ubuntu/clawd/agents-v5.3/steve/__init__.py)