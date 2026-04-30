#!/usr/bin/env python3
"""
Steve v6 Merge to Production
Merges demo branch to main for production deployment (after preview approval)
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
        logging.FileHandler('/home/ubuntu/clawd/tresowealth-beta-site/steve_production_deployment.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def main():
    """Merge demo to main after preview approval"""
    repo_path = Path('/home/ubuntu/clawd/tresowealth-beta-site')
    
    logger.info('=' * 80)
    logger.info('STEVE V6: PRODUCTION DEPLOYMENT (MERGE DEMO → MAIN)')
    logger.info('=' * 80)
    logger.info(f'Repository: {repo_path}')
    logger.info('This action merges demo branch to main for production deployment')
    logger.info('')
    
    try:
        # Step 1: Verify we're on demo branch
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
            logger.warning(f'Not on demo branch (current: {current_branch})')
        
        # Step 2: Switch to main branch
        logger.info('')
        logger.info('Step 2: Switching to main branch...')
        subprocess.run(['git', 'checkout', 'main'],
                      cwd=repo_path,
                      capture_output=True,
                      text=True,
                      check=True)
        logger.info('✓ Switched to main branch')
        
        # Step 3: Merge demo branch
        logger.info('')
        logger.info('Step 3: Merging demo branch into main...')
        commit_message = 'Merge demo branch: Steve v6 rewrite with custom research agents - Approved after preview site review - 41 articles rewritten with enhanced research - Custom agents: Statistics, Regulatory, Benchmark, Case Study - Ready for production deployment'
        
        result = subprocess.run(
            ['git', 'merge', 'demo', '-m', commit_message],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        logger.info('✓ Merged demo → main')
        
        # Step 4: Push to main (triggers production deployment)
        logger.info('')
        logger.info('Step 4: Pushing to main branch (triggers Cloudflare Pages production)...')
        result = subprocess.run(
            ['git', 'push', 'origin', 'main'],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        logger.info('✓ Pushed to main branch')
        
        # Step 5: Switch back to demo branch
        logger.info('')
        logger.info('Step 5: Switching back to demo branch...')
        subprocess.run(['git', 'checkout', 'demo'],
                      cwd=repo_path,
                      capture_output=True,
                      text=True,
                      check=True)
        logger.info('✓ Switched back to demo branch')
        
        logger.info('')
        logger.info('=' * 80)
        logger.info('PRODUCTION DEPLOYMENT COMPLETE!')
        logger.info('=' * 80)
        logger.info('')
        logger.info('✓ demo branch merged to main')
        logger.info('✓ Cloudflare Pages is deploying to production')
        logger.info('✓ Live site will be updated within 1-2 minutes')
        logger.info('')
        logger.info('VERIFY:')
        logger.info('1. Check Cloudflare Dashboard for deployment status')
        logger.info('2. Visit production site: https://tresowealth.com')
        logger.info('3. Verify articles are live and working correctly')
        logger.info('')
        
        return {
            'status': 'success',
            'merged_branches': ['demo', 'main'],
            'production_deployed': True,
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
    with open('/home/ubuntu/clawd/tresowealth-beta-site/steve_production_result.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['status'] == 'success' else 1)
