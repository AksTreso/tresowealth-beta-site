#!/usr/bin/env python3
"""
Steve v6 Batch Rewrite Deployment
Deploys rewritten articles to demo branch for preview
"""

import os
import sys
import subprocess
import json
import logging
from pathlib import Path
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/home/ubuntu/clawd/tresowealth-beta-site/steve_deployment.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def main():
    """Execute deployment as Steve v6"""
    repo_path = Path('/home/ubuntu/clawd/tresowealth-beta-site')
    
    logger.info('=' * 80)
    logger.info('STEVE V6: BATCH REWRITE DEPLOYMENT TO DEMO BRANCH')
    logger.info('=' * 80)
    logger.info(f'Repository: {repo_path}')
    logger.info(f'Target: demo branch (preview site)')
    logger.info('')
    
    try:
        # Step 1: Verify current branch
        logger.info('Step 1: Verifying current branch...')
        result = subprocess.run(
            ['git', 'branch', '--show-current'],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        current_branch = result.stdout.strip()
        logger.info(f'✓ Current branch: {current_branch}')
        
        if current_branch != 'demo':
            logger.error(f'Wrong branch! Expected demo, got {current_branch}')
            return {'status': 'error', 'error': f'Wrong branch: {current_branch}'}
        
        # Step 2: Backup original articles
        logger.info('')
        logger.info('Step 2: Backing up original articles...')
        backup_count = 0
        for html_file in repo_path.rglob('*.html'):
            if (html_file.is_file() and 
                'steve_rewrites_v2' not in str(html_file) and
                not str(html_file).endswith('.backup.html')):
                backup_path = str(html_file) + '.backup.html'
                subprocess.run(['cp', str(html_file), backup_path], 
                             capture_output=True, check=True)
                backup_count += 1
        logger.info(f'✓ Backed up {backup_count} original articles')
        
        # Step 3: Copy rewritten articles
        logger.info('')
        logger.info('Step 3: Copying rewritten articles to main directories...')
        result = subprocess.run(
            ['rsync', '-av', '--exclude=*.backup.html',
             'steve_rewrites_v2/', './'],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Count copied files
        copied_count = len([line for line in result.stdout.split('\n') 
                           if '.html' in line and not line.endswith('/')])
        logger.info(f'✓ Copied {copied_count} rewritten articles')
        
        # Step 4: Stage changes
        logger.info('')
        logger.info('Step 4: Staging changes for commit...')
        subprocess.run(['git', 'add', '.'],
                      cwd=repo_path,
                      capture_output=True,
                      text=True,
                      check=True)
        logger.info('✓ Changes staged')
        
        # Step 5: Commit changes
        logger.info('')
        logger.info('Step 5: Committing changes...')
        commit_message = '''Steve v6 rewrite: 39 articles with custom research agents

- Used custom research agents (Statistics, Regulatory, Benchmark, Case Study)
- Parallel execution: ~7-10s research per article  
- Enhanced research quality: 3-15 findings per article
- Word count: 1500-2100 words per article
- Statistics: 5-22 per article
- Generated: 2026-04-28
- Ready for preview site review

Report: BATCH_REWRITE_SIMPLE_REPORT.md'''
        
        result = subprocess.run(
            ['git', 'commit', '-m', commit_message],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        logger.info('✓ Changes committed')
        
        # Step 6: Push to demo branch
        logger.info('')
        logger.info('Step 6: Pushing to demo branch (triggers Cloudflare Pages preview)...')
        result = subprocess.run(
            ['git', 'push', 'origin', 'demo'],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        logger.info('✓ Pushed to demo branch')
        
        logger.info('')
        logger.info('=' * 80)
        logger.info('DEPLOYMENT COMPLETE!')
        logger.info('=' * 80)
        logger.info('')
        logger.info('✓ Rewritten articles deployed to demo branch')
        logger.info('✓ Cloudflare Pages is auto-deploying preview site')
        logger.info('')
        logger.info('NEXT STEPS:')
        logger.info('1. Go to Cloudflare Dashboard → Pages → tresowealth-beta-site')
        logger.info('2. Find latest deployment for demo branch')
        logger.info('3. Click preview URL to review rewritten articles')
        logger.info('4. After approval, merge to main:')
        logger.info('   git checkout main && git merge demo && git push origin main')
        logger.info('')
        
        return {
            'status': 'success',
            'branch': 'demo',
            'files_deployed': copied_count,
            'backups_created': backup_count,
            'timestamp': datetime.now().isoformat()
        }
        
    except subprocess.CalledProcessError as e:
        logger.error(f'Deployment failed: {e}')
        logger.error(f'stderr: {e.stderr}')
        return {
            'status': 'error',
            'error': str(e),
            'stderr': e.stderr
        }
    except Exception as e:
        logger.error(f'Deployment error: {e}')
        return {
            'status': 'error',
            'error': str(e)
        }


if __name__ == '__main__':
    result = main()
    
    # Save result
    with open('/home/ubuntu/clawd/tresowealth-beta-site/steve_deploy_result.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['status'] == 'success' else 1)
