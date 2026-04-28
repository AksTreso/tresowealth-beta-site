#!/usr/bin/env python3
"""
Safe Batch Article Rewriter for TresoWealth Website
Rewrites all articles using Steve v6 with preview deployment workflow

Workflow:
1. Generate rewritten articles in separate directory (no overwrites)
2. Push to demo branch → Cloudflare Pages preview site
3. Manual review of preview site
4. Merge demo → main when approved (triggers production deployment)
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List
import subprocess
import hashlib

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('batch_rewrite.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class SafeBatchArticleRewriter:
    """Safe batch rewriter with preview deployment"""

    def __init__(self, repo_path: str, steve_path: str):
        self.repo_path = Path(repo_path)
        self.steve_path = Path(steve_path)
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
                # Skip index files
                if html_file.name == 'index.html':
                    continue

                # Extract topic from filename
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
            import re
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if title_match:
                title = title_match.group(1).strip()
                # Clean up title
                title = title.replace('| TresoWealth', '')
                title = title.replace('- TresoWealth', '')
                return title

            # Fallback to filename
            return file_path.stem.replace('-', ' ').replace('_', ' ').title()

        except Exception as e:
            logger.warning(f"Error reading {file_path}: {e}")
            return file_path.stem

    def create_brief(self, article: Dict) -> Dict:
        """Create Steve v6 brief from article"""
        topic = article['topic']
        category = article['category']

        brief = {
            'brief_id': f"BR-{datetime.now().strftime('%Y%m%d')}-{category.upper()}",
            'content_type': 'blog',
            'keyword': topic,
            'target_audience': 'Foreign HNIs',
            'lane': 'Deep',
            'business_goal': f'Comprehensive rewrite with enhanced research: {topic}',
            'search_intent': 'Informational',
            'content_requirements': {
                'length': '1500-2500 words',
                'tone': 'Professional, precise, data-rich',
                'format': 'Blog article with statistics, regulatory references, and case studies',
                'use_custom_research_agents': True,
                'research_depth': 'deep'
            },
            'risk_level': 'medium',
            'created_at': datetime.now().isoformat()
        }

        return brief

    def rewrite_article(self, article: Dict, output_dir: Path) -> Dict:
        """Rewrite single article using Steve v6"""
        logger.info(f"Processing: {article['relative_path']}")

        brief = self.create_brief(article)

        try:
            # Import Steve v6 from VM
            sys.path.insert(0, str(self.steve_path))
            from steve import Stevev6

            # Initialize Steve
            steve = Stevev6()

            # Run complete 8-stage workflow
            logger.info(f"Running Steve v6 workflow for: {brief['keyword']}")
            result = steve.process_content_request(brief)

            if result.get('status') == 'completed':
                # Extract generated content
                stages = result.get('stages', {})

                # Try stage 7 (publish) first, then stage 6 (package)
                stage_7 = stages.get('stage_7_publish', {})
                html_content = stage_7.get('html_content', '')

                if not html_content:
                    stage_6 = stages.get('stage_6_package', {})
                    html_content = stage_6.get('packaged_content', '')

                if html_content:
                    # Create output path (preserve directory structure)
                    output_path = output_dir / article['relative_path']
                    output_path.parent.mkdir(parents=True, exist_ok=True)

                    # Write rewritten content
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)

                    # Generate comparison report
                    comparison = self._generate_comparison(article['path'], output_path, result)

                    logger.info(f"✅ Successfully rewritten: {article['relative_path']}")

                    return {
                        'status': 'success',
                        'article': str(article['relative_path']),
                        'topic': article['topic'],
                        'brief_id': brief['brief_id'],
                        'original_path': str(article['path']),
                        'rewritten_path': str(output_path),
                        'execution_time': result.get('execution_time_seconds', 0),
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
                logger.error(f"❌ Steve workflow failed for: {article['relative_path']}")
                return {
                    'status': 'failed',
                    'article': str(article['relative_path']),
                    'error': result.get('error', 'Unknown error')
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

    def _generate_comparison(self, original_path: Path, rewritten_path: Path, result: Dict) -> Dict:
        """Generate comparison between original and rewritten"""
        try:
            with open(original_path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            with open(rewritten_path, 'r', encoding='utf-8') as f:
                rewritten_content = f.read()

            import re

            # Extract statistics from rewritten content
            stats_count = len(re.findall(r'[\$₹][\d.]+[\d\s]*(?:%|cr|lakh|million|billion)', rewritten_content))
            refs_count = len(re.findall(r'(?:SEBI|IFSCA|RBI|Section|Circular|Notification)', rewritten_content))

            # Extract research data from result
            custom_research = result.get('stages', {}).get('stage_2_research', {}).get('custom_research', {})

            return {
                'original_word_count': len(original_content.split()),
                'rewritten_word_count': len(rewritten_content.split()),
                'statistics_found': stats_count,
                'regulatory_refs': refs_count,
                'custom_research_used': custom_research.get('total_findings', 0),
                'research_agents': custom_research.get('agents_used', []),
                'research_time': custom_research.get('execution_time', 0)
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
        progress_file = self.repo_path / 'rewrite_progress.json'
        with open(progress_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        logger.info(f"Progress saved to: {progress_file}")

    def generate_report(self):
        """Generate final report"""
        report_lines = [
            "# Batch Article Rewrite Report",
            "",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Summary",
            f"- **Total Articles**: {self.results['total']}",
            f"- **Successful**: {self.results['success']} ✅",
            f"- **Failed**: {self.results['failed']} ❌",
            f"- **Skipped**: {self.results['skipped']} ⏭️",
            "",
            "## Deployment Instructions",
            "",
            "### Current Status",
            f"- Rewritten articles saved to: `steve_rewrites_v2/`",
            f"- Original articles unchanged in: `{self.repo_path}`",
            "",
            "### Preview Deployment (DEMO BRANCH)",
            "1. Review rewritten articles in `steve_rewrites_v2/` directory",
            "2. If satisfied, copy to main directories:",
            "   ```bash",
            "   rsync -av steve_rewrites_v2/ .",
            "   ```",
            "3. Commit changes to demo branch:",
            "   ```bash",
            "   git add .",
            "   git commit -m 'Steve v6 rewrite: 41 articles with custom research agents'",
            "   git push origin demo",
            "   ```",
            "4. **Cloudflare Pages will auto-deploy demo branch to preview site**",
            "5. Review preview site for quality and accuracy",
            "",
            "### Production Deployment (MAIN BRANCH)",
            "6. After preview approval, merge to main:",
            "   ```bash",
            "   git checkout main",
            "   git merge demo",
            "   git push origin main",
            "   ```",
            "7. **Cloudflare Pages will auto-deploy main branch to production**",
            "",
            "## Results Breakdown",
            "",
            "### Successful Articles ✅"
        ]

        # Add successful articles
        for article in self.results['articles']:
            if article['status'] == 'success':
                comp = article.get('comparison', {})
                report_lines.append(f"- **{article['article']}**")
                report_lines.append(f"  - Words: {comp.get('original_word_count', 0)} → {comp.get('rewritten_word_count', 0)}")
                report_lines.append(f"  - Statistics: {comp.get('statistics_found', 0)}")
                report_lines.append(f"  - Research findings: {comp.get('custom_research_used', 0)}")
                report_lines.append(f"  - Research time: {comp.get('research_time', 0):.1f}s")
                report_lines.append("")

        report_lines.append("### Failed Articles ❌")
        for article in self.results['articles']:
            if article['status'] == 'failed':
                report_lines.append(f"- **{article['article']}**: {article.get('error', 'Unknown error')}")

        report = "\n".join(report_lines)

        # Write report
        report_path = self.repo_path / 'BATCH_REWRITE_REPORT.md'
        with open(report_path, 'w') as f:
            f.write(report)

        logger.info(f"Report saved to: {report_path}")
        return report


def main():
    """Main execution"""
    # Configuration
    repo_path = Path.cwd()  # Current directory
    output_dir = repo_path / 'steve_rewrites_v2'

    logger.info("=" * 80)
    logger.info("SAFE BATCH ARTICLE REWRITER v1.0")
    logger.info("=" * 80)
    logger.info(f"Repository: {repo_path}")
    logger.info(f"Current branch: demo (preview deployment)")
    logger.info(f"Output directory: {output_dir}")

    # Initialize rewriter
    # Note: steve_path will be set when running on VM
    rewriter = SafeBatchArticleRewriter(str(repo_path), '/home/ubuntu/clawd/agents-v5.3')

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
    logger.info("\nNext steps:")
    logger.info("1. Review rewritten articles in steve_rewrites_v2/")
    logger.info("2. Copy to main directories: rsync -av steve_rewrites_v2/ .")
    logger.info("3. Commit and push to demo branch for preview site")
    logger.info("4. Review preview site, then merge to main for production")


if __name__ == '__main__':
    main()
