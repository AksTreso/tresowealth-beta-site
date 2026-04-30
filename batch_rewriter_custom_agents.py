#!/usr/bin/env python3
"""
Simple Batch Article Rewriter for TresoWealth Website
Uses Steve v6's Enhanced Researcher v4 with custom agents to rewrite articles

Workflow:
1. Extract topic from existing article
2. Run custom research agents (Statistics, Regulatory, Benchmark, Case Study)
3. Generate new article with enhanced research
4. Save to steve_rewrites_v2/ directory
5. Push to demo branch for preview
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List
import subprocess
import re

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('batch_rewrite_simple.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class SimpleBatchRewriter:
    """Simple batch rewriter using custom research agents"""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.steve_path = Path('/home/ubuntu/clawd/agents-v5.3')
        self.articles = []
        self.results = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'skipped': 0,
            'articles': []
        }

    def discover_articles(self) -> List[Dict]:
        """Discover all articles in the repository"""
        logger.info(f"Scanning repository: {self.repo_path}")

        article_patterns = [
            'gift-city-products/*.html',
            'investment-process/*.html',
            'tax-regulatory/*.html',
            'why-india/*.html',
            'faq/*.html',
            'eams-gateway/*.html',
            'why-tresowealth/*.html'
        ]

        discovered = []
        for pattern in article_patterns:
            for html_file in self.repo_path.glob(pattern):
                if html_file.name == 'index.html':
                    continue

                topic = self._extract_topic_from_file(html_file)

                discovered.append({
                    'path': html_file,
                    'relative_path': html_file.relative_to(self.repo_path),
                    'topic': topic,
                    'category': html_file.parent.name
                })

        logger.info(f"Discovered {len(discovered)} articles")
        self.articles = discovered
        self.results['total'] = len(discovered)
        return discovered

    def _extract_topic_from_file(self, file_path: Path) -> str:
        """Extract topic from HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Try to extract title
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip()
                title = title.replace('| TresoWealth', '')
                title = title.replace('- TresoWealth', '')
                return title

            # Fallback to filename
            return file_path.stem.replace('-', ' ').replace('_', ' ').title()

        except Exception as e:
            logger.warning(f"Error reading {file_path}: {e}")
            return file_path.stem

    def rewrite_article(self, article: Dict, output_dir: Path) -> Dict:
        """Rewrite single article using enhanced research"""
        logger.info(f"Processing: {article['relative_path']}")

        topic = article['topic']

        try:
            # Import Enhanced Researcher v4
            sys.path.insert(0, str(self.steve_path))
            from steve.skills.research.enhanced_researcher import EnhancedResearcher

            # Import web search
            sys.path.insert(0, '/home/ubuntu/clawd/agents-v5.3/shared-skills/web-search-plus')
            from skill import execute as web_search_func
            
            # Import ClawRouter
            sys.path.insert(0, '/home/ubuntu/infrastructure')
            try:
                from clawrouter_client import ClawRouterClient as CR
                client = CR(base_url='http://localhost:4000')
            except:
                client = None
            
            # Initialize researcher
            researcher = EnhancedResearcher(
                web_search=web_search_func,
                clawrouter_client=client
            )

            # Run enhanced research with custom agents
            logger.info(f"Running enhanced research for: {topic}")
            research_result = researcher.research_topic(
                topic=topic,
                target_audience="Foreign HNIs",
                research_depth="deep"
            )

            if research_result.get('metadata'):
                # Generate rewritten article using research
                article_content = self._generate_article_from_research(topic, research_result)

                if article_content:
                    # Create output path
                    output_path = output_dir / article['relative_path']
                    output_path.parent.mkdir(parents=True, exist_ok=True)

                    # Write article
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(article_content)

                    # Generate comparison
                    comparison = self._generate_comparison(article['path'], output_path, research_result)

                    logger.info(f"✅ Successfully rewritten: {article['relative_path']}")

                    return {
                        'status': 'success',
                        'article': str(article['relative_path']),
                        'topic': article['topic'],
                        'original_path': str(article['path']),
                        'rewritten_path': str(output_path),
                        'comparison': comparison
                    }
                else:
                    logger.warning(f"⚠️  No content generated for: {article['relative_path']}")
                    return {
                        'status': 'failed',
                        'article': str(article['relative_path']),
                        'error': 'No content generated'
                    }
            else:
                logger.error(f"❌ Research failed for: {article['relative_path']}")
                return {
                    'status': 'failed',
                    'article': str(article['relative_path']),
                    'error': 'Research returned no metadata'
                }

        except Exception as e:
            logger.error(f"❌ Error processing {article['relative_path']}: {e}")
            import traceback
            traceback.print_exc()
            return {
                'status': 'failed',
                'article': str(article['relative_path']),
                'error': str(e)
            }

    def _generate_article_from_research(self, topic: str, research_result: Dict) -> str:
        """Generate article HTML from enhanced research"""
        try:
            # Import ClawRouter for content generation
            from clawrouter_client import ClawRouterClient, Tier

            client = ClawRouterClient()

            statistics = research_result.get('statistics', [])
            regulatory_refs = research_result.get('regulatory_refs', [])
            benchmarks = research_result.get('benchmarks', [])
            case_studies = research_result.get('case_studies', [])

            # Build research brief for LLM
            research_brief = f"""
Topic: {topic}

Key Statistics:
{chr(10).join([f"- {s.get('value', '')}: {s.get('context', '')}" for s in statistics[:5]])}

Regulatory References:
{chr(10).join([f"- {r.get('reference', '')}: {r.get('context', '')}" for r in regulatory_refs[:3]])}

Industry Benchmarks:
{chr(10).join([f"- {b.get('benchmark', '')}" for b in benchmarks[:2]])}

Case Studies:
{chr(10).join([f"- {c.get('title', '')}: {c.get('snippet', '')}" for c in case_studies[:1]])}
"""

            # Generate article using ClawRouter
            prompt = f"""
You are an expert fintech content writer for TresoWealth, writing for Foreign HNIs investing in India.

Rewrite the following article topic with enhanced research:

{research_brief}

Requirements:
1. Write a comprehensive 1500-2000 word article
2. Use professional, precise tone suitable for investment professionals
3. Include all statistics with proper citations
4. Reference regulatory framework accurately
5. Provide actionable insights
6. Use specific numbers, not generic statements
7. Follow TresoWealth brand voice: precise, skeptical, structured, protective

Output: Return only the article body content in markdown format (no HTML tags, no meta tags).
"""

            result = client.query(prompt=prompt, tier=Tier.HIGH, temperature=0.7)

            # Convert markdown to basic HTML
            html_content = self._markdown_to_html(result, topic, statistics, regulatory_refs)

            return html_content

        except Exception as e:
            logger.error(f"Error generating article: {e}")
            return None

    def _markdown_to_html(self, markdown_content: str, title: str, statistics: List, regulatory_refs: List) -> str:
        """Convert markdown content to HTML with TresoWealth template"""
        try:
            # Basic markdown to HTML conversion
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

            # Wrap in TresoWealth HTML template
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
                        {chr(10).join([f'<li>{s.get("value", "")}: {s.get("context", "")}</li>' for s in statistics[:5]])}
                    </ul>
                </div>

                <div class="regulatory">
                    <h3>Regulatory Framework</h3>
                    <ul>
                        {chr(10).join([f'<li>{r.get("reference", "")}: {r.get("context", "")}</li>' for r in regulatory_refs[:3]])}
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
            logger.error(f"Error converting to HTML: {e}")
            return None

    def _generate_comparison(self, original_path: Path, rewritten_path: Path, research_result: Dict) -> Dict:
        """Generate comparison between original and rewritten"""
        try:
            with open(original_path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            with open(rewritten_path, 'r', encoding='utf-8') as f:
                rewritten_content = f.read()

            stats_count = len(re.findall(r'[\$₹][\d.]+[\d\s]*(?:%|cr|lakh|million|billion)', rewritten_content))
            refs_count = len(re.findall(r'(?:SEBI|IFSCA|RBI|Section|Circular|Notification)', rewritten_content))

            return {
                'original_word_count': len(original_content.split()),
                'rewritten_word_count': len(rewritten_content.split()),
                'statistics_found': stats_count,
                'regulatory_refs': refs_count,
                'custom_research_used': research_result.get('metadata', {}).get('total_findings', 0),
                'research_agents': research_result.get('metadata', {}).get('agents', []),
                'research_time': research_result.get('metadata', {}).get('execution_time_seconds', 0)
            }

        except Exception as e:
            logger.warning(f"Could not generate comparison: {e}")
            return {}

    def process_batch(self, output_dir: Path, batch_size: int = 10):
        """Process all articles in batches"""
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)

        logger.info(f"Starting batch rewrite of {len(self.articles)} articles")
        logger.info(f"Output directory: {output_dir}")

        for i, article in enumerate(self.articles, 1):
            logger.info(f"\n[{i}/{len(self.articles)}] Processing article")

            result = self.rewrite_article(article, output_dir)
            self.results['articles'].append(result)

            if result['status'] == 'success':
                self.results['success'] += 1
            elif result['status'] == 'failed':
                self.results['failed'] += 1
            else:
                self.results['skipped'] += 1

            # Periodic saves
            if i % batch_size == 0:
                self.save_progress()
                logger.info(f"Progress saved: {i}/{len(self.articles)} articles processed")

        # Final save
        self.save_progress()

    def save_progress(self):
        """Save progress to JSON file"""
        progress_file = self.repo_path / 'rewrite_progress_simple.json'
        with open(progress_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        logger.info(f"Progress saved to: {progress_file}")

    def generate_report(self):
        """Generate final report"""
        report_lines = [
            "# Simple Batch Article Rewrite Report",
            "",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Summary",
            f"- **Total Articles**: {self.results['total']}",
            f"- **Successful**: {self.results['success']} ✅",
            f"- **Failed**: {self.results['failed']} ❌",
            f"- **Skipped**: {self.results['skipped']} ⏭️",
            "",
            "## Results Breakdown",
            "",
            "### Successful Articles ✅"
        ]

        for article in self.results['articles']:
            if article['status'] == 'success':
                comp = article.get('comparison', {})
                report_lines.append(f"- **{article['article']}**")
                report_lines.append(f"  - Words: {comp.get('original_word_count', 0)} → {comp.get('rewritten_word_count', 0)}")
                report_lines.append(f"  - Statistics: {comp.get('statistics_found', 0)}")
                report_lines.append(f"  - Research findings: {comp.get('custom_research_used', 0)}")
                report_lines.append("")

        report_lines.append("### Failed Articles ❌")
        for article in self.results['articles']:
            if article['status'] == 'failed':
                report_lines.append(f"- **{article['article']}**: {article.get('error', 'Unknown error')}")

        report = "\n".join(report_lines)

        report_path = self.repo_path / 'BATCH_REWRITE_SIMPLE_REPORT.md'
        with open(report_path, 'w') as f:
            f.write(report)

        logger.info(f"Report saved to: {report_path}")
        return report


def main():
    """Main execution"""
    repo_path = Path.cwd()
    output_dir = repo_path / 'steve_rewrites_v2'

    logger.info("=" * 80)
    logger.info("SIMPLE BATCH ARTICLE REWRITER v1.0")
    logger.info("=" * 80)
    logger.info(f"Repository: {repo_path}")
    logger.info(f"Output directory: {output_dir}")

    rewriter = SimpleBatchRewriter(str(repo_path))

    # Discover articles
    articles = rewriter.discover_articles()

    if not articles:
        logger.error("No articles found!")
        return

    # Process batch
    rewriter.process_batch(output_dir, batch_size=10)

    # Generate report
    report = rewriter.generate_report()
    print("\n" + report)

    logger.info("\n" + "=" * 80)
    logger.info("BATCH REWRITE COMPLETE")
    logger.info("=" * 80)


if __name__ == '__main__':
    main()
