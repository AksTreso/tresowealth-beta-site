#!/usr/bin/env python3
'''
Steve v6: Retry Failed Articles
Retries articles that failed due to ClawRouter timeout
'''

import os
import sys
import logging
from pathlib import Path
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('steve_retry_failed.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def retry_failed_articles():
    '''Retry the 2 failed articles with optimized approach'''
    
    # Articles that failed
    failed_articles = [
        {
            'path': 'investment-process/how-foreigners-invest-gift-city-aif.html',
            'topic': 'How Can Foreigners Invest in GIFT CITY AIFs?'
        },
        {
            'path': 'investment-process/kyc-non-indian-residents.html',
            'topic': 'GIFT CITY AIF KYC for Non-Indian Residents'
        }
    ]
    
    repo_path = Path('/home/ubuntu/clawd/tresowealth-beta-site')
    steve_path = Path('/home/ubuntu/clawd/agents-v5.3')
    output_dir = repo_path / 'steve_rewrites_v2_retry'
    
    logger.info('=' * 80)
    logger.info('STEVE V6: RETRYING FAILED ARTICLES')
    logger.info('=' * 80)
    logger.info(f'Articles to retry: {len(failed_articles)}')
    logger.info(f'Output directory: {output_dir}')
    logger.info('')
    
    results = []
    
    for i, article in enumerate(failed_articles, 1):
        logger.info(f'[{i}/{len(failed_articles)}] Retrying: {article["path"]}')
        
        try:
            # Import Enhanced Researcher v4
            sys.path.insert(0, str(steve_path))
            from steve.skills.research.enhanced_researcher_v4 import EnhancedResearcher
            
            # Initialize researcher
            researcher = EnhancedResearcher()
            
            # Run enhanced research with custom agents
            logger.info(f'Running enhanced research for: {article["topic"]}')
            research_result = researcher.research_topic(
                topic=article['topic'],
                target_audience='Foreign HNIs',
                research_depth='deep'
            )
            
            if research_result.get('metadata'):
                # Generate article with OPTIMIZED prompt (shorter)
                article_content = generate_article_optimized(
                    article['topic'], 
                    research_result,
                    max_prompt_length=8000  # Limit prompt size
                )
                
                if article_content:
                    # Create output path
                    output_path = output_dir / article['path']
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Write article
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(article_content)
                    
                    logger.info(f'✅ Successfully rewritten: {article["path"]}')
                    
                    results.append({
                        'status': 'success',
                        'article': article['path'],
                        'topic': article['topic'],
                        'output_path': str(output_path)
                    })
                else:
                    logger.warning(f'⚠️  No content generated for: {article["path"]}')
                    results.append({
                        'status': 'failed',
                        'article': article['path'],
                        'error': 'No content generated (optimized)'
                    })
            else:
                logger.error(f'❌ Research failed for: {article["path"]}')
                results.append({
                    'status': 'failed',
                    'article': article['path'],
                    'error': 'Research returned no metadata'
                })
                
        except Exception as e:
            logger.error(f'❌ Error processing {article["path"]}: {e}')
            import traceback
            traceback.print_exc()
            results.append({
                'status': 'failed',
                'article': article['path'],
                'error': str(e)
            })
    
    # Generate summary
    logger.info('')
    logger.info('=' * 80)
    logger.info('RETRY SUMMARY')
    logger.info('=' * 80)
    
    success_count = sum(1 for r in results if r['status'] == 'success')
    logger.info(f'Successful: {success_count}/{len(failed_articles)}')
    
    for result in results:
        if result['status'] == 'success':
            logger.info(f'  ✅ {result["article"]}')
        else:
            logger.info(f'  ❌ {result["article"]}: {result["error"]}')
    
    return results


def generate_article_optimized(topic: str, research_result: dict, max_prompt_length: int = 8000) -> str:
    '''Generate article with optimized (shorter) prompt to avoid timeout'''
    try:
        from clawrouter_client import ClawRouterClient, Tier
        
        client = ClawRouterClient()
        
        # Extract only TOP findings to reduce prompt size
        statistics = research_result.get('statistics', [])[:3]  # Top 3 only
        regulatory_refs = research_result.get('regulatory_refs', [])[:2]  # Top 2 only
        benchmarks = research_result.get('benchmarks', [])[:2]  # Top 2 only
        
        # Build compact research brief
        research_brief = f"""Topic: {topic}

Key Statistics:
- {'; '.join([s.get('value', '') for s in statistics])}

Regulatory References:
- {'; '.join([r.get('reference', '') for r in regulatory_refs])}

Industry Benchmarks:
- {'; '.join([b.get('benchmark', '')[:100] for b in benchmarks])}
"""
        
        # Use shorter prompt to avoid timeout
        prompt = f"""You are an expert fintech content writer for TresoWealth.

Write a 1500-2000 word article on: {topic}

Key research findings:
{research_brief}

Requirements:
1. Professional tone suitable for investment professionals
2. Include specific statistics and regulatory references
3. Provide actionable insights
4. Use precise language, avoid generic statements
5. Follow TresoWealth brand: precise, skeptical, structured

Output: Article in markdown format (no HTML tags)."""
        
        # Use shorter timeout
        result = client.query(prompt=prompt, tier=Tier.HIGH, temperature=0.7, timeout=240)
        
        # Convert to HTML
        html_content = markdown_to_html(result, topic, statistics, regulatory_refs)
        
        return html_content
        
    except Exception as e:
        logger.error(f'Error generating article: {e}')
        return None


def markdown_to_html(markdown_content: str, title: str, statistics: list, regulatory_refs: list) -> str:
    '''Convert markdown to HTML with TresoWealth template'''
    try:
        lines = markdown_content.split('\n')
        html_lines = []
        in_list = False
        
        for line in lines:
            line = line.strip()
            if not line:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                continue
            
            # Headers
            if line.startswith('# '):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append(f'<h1>{line[2:]}</h1>')
            elif line.startswith('## '):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append(f'<h2>{line[3:]}</h2>')
            elif line.startswith('### '):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append(f'<h3>{line[4:]}</h3>')
            # Lists
            elif line.startswith('- ') or line.startswith('* '):
                if not in_list:
                    html_lines.append('<ul>')
                    in_list = True
                html_lines.append(f'<li>{line[2:]}</li>')
            # Paragraphs
            else:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append(f'<p>{line}</p>')
        
        if in_list:
            html_lines.append('</ul>')
        
        # Wrap in template
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | TresoWealth</title>
    <meta name="description" content="Comprehensive guide on {title} for Foreign HNIs investing in India through GIFT City.">
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <header>
        <nav>
            <div class="container">
                <a href="/" class="logo">TresoWealth</a>
                <ul class="nav-menu">
                    <li><a href="/gift-city-products/">Products</a></li>
                    <li><a href="/investment-process/">Process</a></li>
                    <li><a href="/tax-regulatory/">Tax & Regulatory</a></li>
                    <li><a href="/why-india/">Why India</a></li>
                    <li><a href="/faq/">FAQ</a></li>
                </ul>
            </div>
        </nav>
    </header>

    <main class="container">
        <article>
            <h1>{title}</h1>
            <div class="article-content">
                {''.join(html_lines)}
            </div>

            <aside class="research-highlights">
                <h2>Research Highlights</h2>
                <div class="statistics">
                    <h3>Key Statistics</h3>
                    <ul>
                        {chr(10).join([f'<li>{s.get("value", "")}</li>' for s in statistics])}
                    </ul>
                </div>

                <div class="regulatory">
                    <h3>Regulatory Framework</h3>
                    <ul>
                        {chr(10).join([f'<li>{r.get("reference", "")}</li>' for r in regulatory_refs])}
                    </ul>
                </div>
            </aside>
        </article>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2026 TresoWealth. All rights reserved.</p>
            <p>Invest in India, from anywhere.</p>
        </div>
    </footer>
</body>
</html>"""
        
        return html_template
        
    except Exception as e:
        logger.error(f'Error converting to HTML: {e}')
        return None


if __name__ == '__main__':
    import json
    
    results = retry_failed_articles()
    
    # Save results
    with open('/home/ubuntu/clawd/tresowealth-beta-site/steve_retry_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(json.dumps(results, indent=2))
    
    # Exit with error code if any failed
    sys.exit(0 if all(r['status'] == 'success' for r in results) else 1)
